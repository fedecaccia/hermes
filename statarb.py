import definitions

import datetime

import numpy as np

from algorithm import Algorithm


class StatArb(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules, assets, oracle, world):

        """
        + Description: Statistical arbitrage constructor.
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - assets: Dictionary of all assets objetcs. Super only saves what here cares.
        - oracle: Oracle object.
        - world: World object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, assets, oracle)
        self._world = world
        self._initialize_variables()

    def _check_data_modules(self):

        """
        + Description: check that data module received is right.
        + Input:
        -
        + Output:
        -
        """
        
        self._check_data_modules_amount()
        self._check_data_modules_description()
        self._check_data_modules_source()
        self._check_data_type()

    def _check_data_modules_amount(self):

        """
        + Description: check that amonut data modules received is right.
        + Input:
        -
        + Output:
        -
        """

        if len(self.data_modules)!=2:
            raise ValueError("Error using: "+str(len(self.data_modules))+" data modules in algorithm with id: '"
                             +str(self.id)+"'. You can only use 2.")

    def _check_data_modules_description(self):

        """
        + Description: check that data modules description received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.description not in definitions.all_tickers:
                raise ValueError("Bad description in data module id: "
                +str(module.id))

    def _check_data_modules_source(self):

        """
        + Description: check that data modules source received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.source not in definitions.all_exchanges:
                raise ValueError("Bad source in data module id: "
                +str(module.id))

    def _check_data_type(self):

        """
        + Description: check that data type in modules received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.data_type != definitions.orderbook:
                raise ValueError("Bad data type in data module id: "
               +str(module.id)
                +". Expected: "+definitions.orderbook)

    def _check_parameters(self, algo_values):

        """
        + Description: Check parameters received in algo_values dictionary.
        + Input:
        - algo values: Dictionary containing algorithmic parameters defined in config.py.
        + Output:
        -
        """

        algo_params = algo_values[definitions.algo_params]
        
        try:
            self._limit_buy_pct = algo_params[definitions.limit_buy_pct]
        except:
            raise ValueError("Error trying to parse limit_buy_pct in algorithm: '"+self.id+"' parameters.")
                
        try:
            self._limit_sell_pct = algo_params[definitions.limit_sell_pct]
        except:
            raise ValueError("Error trying to parse limit_sell_pct in algorithm: '"+self.id+"' parameters.")
        

        try:
            self._max_delay_in_data = datetime.timedelta(seconds=algo_params[definitions.max_delay_in_data])
        except:
            raise ValueError("Error trying to parse max_delay_in_data in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._usd_amount_to_trade = algo_params[definitions.usd_amount_to_trade]
        except:
            raise ValueError("Error trying to parse usd_amount_to_trade in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._period = algo_params[definitions.period]
        except:
            raise ValueError("Error trying to parse period in algorithm: '"+self.id+"' parameters.")

    def _initialize_variables(self):
        
        """
        + Description: Initialize useful variables.
        + Input:
        -
        + Output:
        -
        """

        self.p_l0_s1 = np.array(())
        self.p_l1_s0 = np.array(())
        self.status = {
            definitions.long_position: None,
            definitions.short_position: None
        }

    def evaluate(self):

        """
        + Description: Execute algorithm evaluating virtual transfers based on arbitrage.
        + Input:
        -
        + Output:
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """

        # reinitialize signals
        self._reinitialize_signals()

        # reinitialize parameters
        params = {asset:{
            definitions.limit:0,
            definitions.amount:0
        } for asset in list(self._signals.keys())}

        # asset key should be the same as defined in # Assets in config.py
        asset0 = list(self.assets.keys())[0]
        asset1 = list(self.assets.keys())[1]
        
        # quick access to exchange name
        exchange0 = self.assets[asset0].exchange
        exchange1 = self.assets[asset1].exchange

        # quick access to fees
        fee0 = self._fees[exchange0][definitions.trading][definitions.taker]
        fee1 = self._fees[exchange1][definitions.trading][definitions.taker]

        # world_time
        world_time = self._world.get_time()

        if len(self.data_modules[0].data>0) and len(self.data_modules[1].data>0):

            # orderbook0 time
            time0 = self.data_modules[0].data.index[-1]
            # orderbook1 time
            time1 = self.data_modules[1].data.index[-1]
            
            if world_time >= time0 and\
                world_time >= time1 and\
                world_time-time0<=self._max_delay_in_data and\
                world_time-time1<=self._max_delay_in_data:
                
                bid0 = self.data_modules[0].data.iloc[-1]["bid_val_0"]
                ask0 = self.data_modules[0].data.iloc[-1]["ask_val_0"]

                bid1 = self.data_modules[1].data.iloc[-1]["bid_val_0"]
                ask1 = self.data_modules[1].data.iloc[-1]["ask_val_0"]

                # Compute amount to trade

                btc_usd = self._oracle.get_price(
                    definitions.btc,
                    definitions.usd
                )
                            
                asset_usd = ask1*btc_usd # approximated price

                if self._usd_amount_to_trade == definitions.full:
                    raise ValueError("ERROR! You can't use full amount in arbitrage!")
                else:
                    amount = self._usd_amount_to_trade / asset_usd

                # Statistical calculations

                p_l0_s1_actual = -ask0*(1+fee0)+bid1*(1-fee1)
                p_l1_s0_actual = -ask1*(1+fee1)+bid0*(1-fee0)

                self.p_l0_s1 = np.append(self.p_l0_s1, p_l0_s1_actual)
                self.p_l1_s0 = np.append(self.p_l1_s0, p_l1_s0_actual)

                if len(self.p_l0_s1) > self._period: # we have enough data

                    self.p_l0_s1 = np.delete(self.p_l0_s1, 0)
                    self.p_l1_s0 = np.delete(self.p_l1_s0, 0)

                    p_l0_s1_m = np.mean(self.p_l0_s1)
                    p_l1_s0_m = np.mean(self.p_l1_s0)

                    print("asset0:", asset0, "bid0", bid0, "ask0", ask0)
                    print("asset1:", asset1, "bid1", bid1, "ask1", ask1)

                    print("p_l0_s1_actual", p_l0_s1_actual, "p_l0_s1_m", p_l0_s1_m)
                    print("p_l1_s0_actual", p_l1_s0_actual, "p_l1_s0_m", p_l1_s0_m)

                    # Analyze open positions

                    if self._positions_are_closed():

                        if p_l0_s1_actual > -p_l1_s0_m and self._positions_are_closed():
                            
                            self._shoot_long_signal(asset0)                
                            params[asset0] = {
                                definitions.amount:amount,
                                definitions.limit:bid0
                            }

                            self._shoot_short_signal(asset1)
                            params[asset1] = {
                                definitions.amount:amount,
                                definitions.limit:ask1
                            }
                            
                            self.status = {
                                definitions.long_position: asset0,
                                definitions.short_position: asset1
                            }

                            self.min_profit = p_l1_s0_m
                        
                        elif p_l1_s0_actual > -p_l0_s1_m and self._positions_are_closed():
                            
                            self._shoot_short_signal(asset0)
                            params[asset0] = {
                                definitions.amount:amount,
                                definitions.limit:ask0
                            }

                            self._shoot_long_signal(asset1)
                            params[asset1] = {
                                definitions.amount:amount,
                                definitions.limit:bid1
                            }

                            self.status = {
                                definitions.long_position: asset0,
                                definitions.short_position: asset1
                            }

                            self.min_profit = p_l0_s1_m
                    
                    # Analyze close positions
                    else:

                        if p_l0_s1_actual > self.min_profit and self._positions_can_be_closed(long_position=asset1, short_position=asset0):
                            
                            self._shoot_long_signal(asset0)                
                            params[asset0] = {
                                definitions.amount:amount,
                                definitions.limit:bid0
                            }

                            self._shoot_short_signal(asset1)
                            params[asset1] = {
                                definitions.amount:amount,
                                definitions.limit:ask1
                            }
                            
                            self.status = {
                                definitions.long_position: None,
                                definitions.short_position: None
                            }
                        
                        elif p_l1_s0_actual > self.min_profit and self._positions_can_be_closed(long_position=asset0, short_position=asset1):
                            
                            self._shoot_short_signal(asset0)
                            params[asset0] = {
                                definitions.amount:amount,
                                definitions.limit:ask0
                            }

                            self._shoot_long_signal(asset1)
                            params[asset1] = {
                                definitions.amount:amount,
                                definitions.limit:bid1
                            }

                            self.status = {
                                definitions.long_position: None,
                                definitions.short_position: None
                            }
                    
                else:
                    print("Doing nothing. Not enough data yet...")  

        return self._signals, params

    def _positions_are_closed(self):

        """
        + Description: Analyze if actual status allow opend positions.
        + Input:
        -      
        + Output:
        - answer: bool True or False depending on opportunity availability.
        """

        if self.status[definitions.long_position] != None:
            return False
        if self.status[definitions.short_position] != None:
            return False

        return True

    def _positions_can_be_closed(self, long_position, short_position):

        """
        + Description: Analyze if desired trade can be efectuated.
        + Input:
        - long_position: Asset string name to evaluate if it's in a long position.
        - short_position: Asset string name to evaluate if it's in a short position.
        + Output:
        - answer: bool True or False depending on case.
        """
    
        if self.status[definitions.long_position] == long_position and\
            self.status[definitions.short_position] == short_position:
            return True

        return False