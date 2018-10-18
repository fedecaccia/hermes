import definitions
import time

import numpy as np

from threading import Barrier


class Strategy(object):

    """
    Strategy: a class to implement data reception and algorithm evaluation.
    Based on a sum over individual algorithm punctuation values, takes a trading decision.
    """

    def __init__(self,
                 strategy_id,
                 strategy_values,
                 assets,
                 request_pile,
                 request_flag,
                 algorithms,
                 data_modules,
                 portfolio,
                 trading,
                 oracle):

        """
        + Description: constructor
        + Input:
        - id: Strategy id.
        - strategy_values: Dictionary of strategy parameters values.        
        - assets: Array of asset objects.
        - request_pile: A pile where request_workers look functions to evaluate.
        - request_flag: List of 1 flag ([flag]) to indicate how many workers are bussy.
        - algorithms: Dictionary of algorithm objects.
        - data_modules: Dictionary of data_modules objects.
        - portfolio: Portfolio object.
        - trading: Trading platform object.
        - oracle: Oracle object.
        + Output:
        -
        """

        self.id = strategy_id
        self._assets = assets
        self.request_pile = request_pile
        self.request_flag = request_flag        
        self._portfolio = portfolio
        self._trading = trading
        self._oracle = oracle
        self._is_trading = False
        self._valuation = 0
        self._thresholds = strategy_values[definitions.thresholds]
        self._order_type = strategy_values[definitions.order_type]      
        self._set_algorithms(algorithms, strategy_values)
        self._set_data_modules(data_modules)

    def _set_algorithms(self, algorithms, strategy_values):
        
        """
        + Description: Find algorithms objects needed in strategy.
        + Input:
        - algorithms: Dictionary of algorithms objects.
        - strategy_values: Dictionary of strategy parameters.
        + Output:
        -
        """
    
        algo = set()
        for algo_id, algorithm in algorithms.items():
            if algo_id in strategy_values[definitions.algorithms_array]:
                algo.update([algorithm])
        self._algorithms = list(algo)

    def _set_data_modules(self, data_modules):
        
        """
        + Description: Find data modules objects needed in strategy.
        + Input:
        - data_modules: Dictionary of data modules objects.
        + Output:
        -
        """

        modules = set()
        for module_id, module in data_modules.items():
            for algo in self._algorithms:
                if module_id in algo.data_modules_ids:
                    modules.update([module])
        self._data_modules = list(modules)

        self._n_data_modules = len(self._data_modules)

    def execute(self):

        """
        + Description: Strategy executor.
        + Input:
        - 
        + Output:
        -
        """

        print("\nExecuting strategy id: "+str(self.id))
        self._update_oracle()
        self._check_portfolio_update()
        # we can't check funds availability here, because yet we don't know if we're buying or selling
        self._restart_valuation()
        self._restart_params()
        self._request_update_in_data_modules()
        self._evaluate_algorithms()
        self._analyze_valuation()
        if self._trading:
            self._check_orders()
            self._portfolio_update()
            pass

    def _update_oracle(self):

        """
        + Description: Call oracle update function who checks if it's necessary to update.
        + Input:
        - 
        + Output:
        -
        """
        
        self._oracle.update()

    def _check_portfolio_update(self):

        """
        + Description: Check if it's needed to update portfolio.
        + Input:
        - 
        + Output:
        -
        """
        
        self._portfolio.check_update()

    def _restart_valuation(self):

        """
        + Description: Function to reinitialize valuation.
        + Input:
        - 
        + Output:
        -
        """

        self._valuation = {}
        for asset in self._thresholds.keys():
            self._valuation[asset] = 0
    
    def _restart_params(self):

        """
        + Description: Function to reinitialize order parameters.
        + Input:
        - 
        + Output:
        -
        """

        self._is_trading = False
        self._params = {}
        for asset in self._thresholds.keys():
            self._params[asset] = {}

    def _request_update_in_data_modules(self):

        """
        + Description: Function to update all data modules in strategy.
        + Input:
        - 
        + Output:
        -
        """

        print("Updating data modules")
        self.request_flag[0] = self._n_data_modules # all workers are flagged as working
        barrier = Barrier(self._n_data_modules)

        for module in self._data_modules:
            # request update slow in backtesting because looks to closest time
            self.request_pile.put({
                definitions.function:module.update,
                definitions.params:{
                    definitions.barrier:barrier
                }                
            })

        print("All modules have requested update")
        while self.request_flag[0] > 0: # some worker is still working
            pass
        print("All modules have been updated")

    def _evaluate_algorithms(self):

        """
        + Description: Run algorithms.
        + Input:
        - 
        + Output:
        -
        """

        for algorithm in self._algorithms:
            signals, params = algorithm.evaluate()

            for asset, signal in signals.items():
                self._valuation[asset] += signal

            for asset, param in params.items():
                self._params[asset].update(param)

    def _analyze_valuation(self):

        """
        + Description: Shoots trade order in case that valuation is greater than threshold.
        + Input:
        - 
        + Output:
        -
        """
        
        print("Checking if funds are available...", self._valuation)

        have_funds = {asset_id:False for asset_id in self._valuation.keys()}
        
        for asset_id, signal in self._valuation.items():

            try:
                amount = self._params[asset_id][definitions.amount]
            except:
                raise ValueError("Bad formulation in algorithm. Amount not returned for asset id: '"+asset_id+"'.")

            if signal >= self._thresholds[asset_id][definitions.long_threshold]:
                self._is_trading = True
                
                have_funds[asset_id] = self._trading.check_funds(
                                            asset_id=asset_id,
                                            order_type=self._order_type,
                                            side=definitions.buy,
                                            amount=amount,
                                            params=self._params[asset_id]
                                        )

            elif signal <= self._thresholds[asset_id][definitions.short_threshold]:
                self._is_trading = True
                    
                have_funds[asset_id] = self._trading.check_funds(
                                            asset_id=asset_id,
                                            order_type=self._order_type,
                                            side=definitions.sell,
                                            amount=amount,
                                            params=self._params[asset_id]
                                        )

        have_funds = np.all(list(have_funds.values()))

        if have_funds and self._is_trading:
            
            print("Executing orders...")

            for asset_id, signal in self._valuation.items():       
                    
                if signal >= self._thresholds[asset_id][definitions.long_threshold]:
                    self._is_trading = True
                    print("LONG SIGNAL SHOOTED")
                    
                    self._trading.execute_order(
                        asset_id=asset_id,
                        order_type=self._order_type,
                        side=definitions.buy,
                        amount=amount,
                        params=self._params[asset_id]
                    )

                elif signal <= self._thresholds[asset_id][definitions.short_threshold]:
                    self._is_trading = True
                    print("SHORT SIGNAL SHOOTED")
                        
                    self._trading.execute_order(
                        asset_id=asset_id,
                        order_type=self._order_type,
                        side=definitions.sell,
                        amount=amount,
                        params=self._params[asset_id]
                    )

        elif not have_funds and self._is_trading:
            print("WARNING: Algorithm has shooted signals but funds are not enough")
            # notify to algo that orders are not going to be executed
            pass

    def _check_orders(self):

        """
        + Description: Check order status from last trades
        + Input:
        - 
        + Output:
        -
        """
        
        self._trading.check_orders()

    def _portfolio_update(self):
        
        """
        + Description: Update balances in portfolio.
        + Input:
        - 
        + Output:
        -
        """

        self._portfolio.update()