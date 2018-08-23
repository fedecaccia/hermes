import definitions
import config

from world import EmulatedWorld, RealWorld, PaperWorld, Oracle
from data_module import Candles, Orderbook, Tickers, Tweets
from asset import Asset
from crossing_sma import CrossingSMA
from volume import Volume
from twitter_analysis import TwitterAnalysis
from virtual_transfer import VirtualTransfer
from strategy import Strategy
from portfolio import Portfolio
from trade import Trade
from strategy import Strategy
from request_worker import RequestWorker

from pprint import pprint
from queue import Queue
from threading import Lock


class Hermes(object):

    """
    Hermes: the brain of the whole system. It could be replaced by an interface in future.
    """

    def __init__(self):

        """
        + Description: Constructor. Hermes initialization.
        + Input:
        -
        + Output:
        -
        """

        self._load_config()
        self._build_systems()

    def _load_config(self):

        """
        + Description: load configuration from user's input.
        + Input:
        -
        + Output:
        -
        """

        self._load_trading_mode()
        self._load_data_elements()
        self._load_assets_elements()
        self._load_algorithms_elements()
        self._load_strategies_elements()
        self._load_other_parameters()

    def _load_trading_mode(self):

        """
        + Description: load trading mode and mode specifics.
        + Input:
        -
        + Output:
        -
        """
        
        try:
            self.mode = config.trading_mode
        except:
            raise ValueError("Error trying to read trading_mode from config.py.")
        if self.mode not in [definitions.backtest, definitions.paper, definitions.real]:
            raise ValueError("Bad trading mode.")

    def _load_data_elements(self):
        
        """
        + Description: load data elements.
        + Input:
        -
        + Output:
        -
        """

        self.data_elements = config.data_elements
        self._check_data_elements_consistency()

    def _check_data_elements_consistency(self):

        """
        + Description: check consistency in data elements.
        + Input:
        -
        + Output:
        -
        """
        pass

    def _load_assets_elements(self):
        
        """
        + Description: load asset elements.
        + Input:
        -
        + Output:
        -
        """

        self.assets_elements = config.assets_elements
        self._check_assets_elements_consistency()

    def _check_assets_elements_consistency(self):

        """
        + Description: check consistency in asset elements.
        + Input:
        - 
        + Output:
        - 
        """
        pass

    def _load_algorithms_elements(self):
        
        """
        + Description: load algorithms elements.
        + Input:
        -
        + Output:
        -
        """

        self.algorithms_elements = config.algorithms_elements
        self._check_algorithms_elements_consistency()

    def _check_algorithms_elements_consistency(self):

        """
        + Description: check consistency in algorithms elements.
        + Input:
        - 
        + Output:
        - 
        """
        pass
        
    def _load_strategies_elements(self):
        
        """
        + Description: load strategies elements.
        + Input:
        -
        + Output:
        -
        """

        self.strategies_elements = config.strategies_elements
        self._check_strategies_elements_consistency()

    def _check_strategies_elements_consistency(self):

        """
        + Description: check consistency in strategies elements.
        + Input:
        -
        + Output:
        -
        """
        pass

    def _load_other_parameters(self):
        
        """
        + Description: check consistency in strategies elements.
        + Input:
        -
        + Output:
        -
        """
        self.n_request_threads = config.n_request_threads
        self.max_delay_in_data = config.max_delay_in_data
        if self.mode == definitions.backtest:
            try:
                self._time_step = config.time_step
            except:
                raise ValueError("'time_step' must be definied in config.py using backtest mode.")

            try:
                self._virtual_portfolio = config.virtual_portfolio
            except:
                raise ValueError("'time_step' must be definied in config.py using backtest mode.")
                
            try:
                self._virtual_tickers = config.virtual_tickers
            except:
                raise ValueError("'time_step' must be definied in config.py using backtest mode.")

        elif self.mode == definitions.paper:
            try:
                self._virtual_portfolio = config.virtual_portfolio
            except:
                raise ValueError("'virtual_portfolio' must be definied in config.py using paper mode.")


    def _build_systems(self):

        """
        + Description: Builds main system.
        + Input:
        -
        + Output:
        -
        """

        self._unique_exchanges()
        self._connect_to_world()
        self._create_oracle()
        self._build_data_modules()
        self._build_assets()
        self._build_algorithms()        
        self._build_portfolio()
        self._build_request_structure()
        self._build_trading_platform()        
        self._build_strategies()

    def _unique_exchanges(self):
        
        """
        + Description: unique list of exchanges.
        + Input:
        -
        + Output:
        -
        """

        sources = [e[definitions.source] for e in self.data_elements.values()]
        self.exchanges_names = set([s for s in sources if s in definitions.all_exchanges])

        print("\nUnique list of exchanges")
        print(self.exchanges_names)

    def _connect_to_world(self):

        """
        + Description: initialize connections.
        + Input:
        -
        + Output:
        -
        """

        self.world = None

        if self.mode == definitions.backtest:
            self.world = EmulatedWorld(self.data_elements,
                                       self.exchanges_names,
                                       self._time_step,
                                       self._virtual_portfolio,
                                       self._virtual_tickers)

        else:            
        
            if self.mode == definitions.paper:
                self.world = PaperWorld(self.data_elements,
                                       self.exchanges_names,
                                       self.mode,
                                       self._virtual_portfolio)
            
            else:
                self.world = RealWorld(self.data_elements,
                                       self.exchanges_names,
                                       self.mode,                                       
                                       config.api_keys_files)

    def _create_oracle(self):

        """
        + Description: initialize oracle to fast queries.
        + Input:
        -
        + Output:
        -
        """

        self.oracle = Oracle(self.world)

    def _build_data_modules(self):
        
        """
        + Description: build data modules.
        + Input:
        -
        + Output:
        -
        """        
        
        self.data_modules = {}
        for data_id, data_values in self.data_elements.items():
            
            if data_values[definitions.data_type] == definitions.candles:                
                self.data_modules[data_id] = Candles(self.mode, data_id, data_values, self.world)
            
            elif data_values[definitions.data_type] == definitions.orderbook:
                self.data_modules[data_id] = Orderbook(self.mode, data_id, data_values, self.world)
            
            elif data_values[definitions.data_type] == definitions.tickers:
                self.data_modules[data_id] = Tickers(self.mode, data_id, data_values, self.world)
            
            elif data_values[definitions.data_type] == definitions.tweets_count:
                self.data_modules[data_id] = Tweets(self.mode, data_id, data_values, self.world)

            else:
                raise ValueError("Bad data_type: '"
                +data_values[definitions.data_type]
                +' in module id: '+data_id+"'.") 
        
        print("\nData modules:")
        pprint(self.data_modules)

    def _build_assets(self):

        """
        + Description: build assets.
        + Input:
        -
        + Output:
        -
        """
        self.assets = {}
        for asset_id, asset_values in self.assets_elements.items():
            self.assets[asset_id] = Asset(asset_id, asset_values)


    def _build_algorithms(self):

        """
        + Description: build algorithms based on data modules.
        + Input:
        -
        + Output:
        -
        """

        self.algorithms = {}
        for algo_id, algo_values in self.algorithms_elements.items():

            if algo_values[definitions.algorithm] == definitions.crossing_sma:
                self.algorithms[algo_id] = CrossingSMA(algo_id, algo_values, self.data_modules, self.oracle)

            elif algo_values[definitions.algorithm] == definitions.volume:
                self.algorithms[algo_id] = Volume(algo_id, algo_values, self.data_modules, self.oracle)

            elif algo_values[definitions.algorithm] == definitions.twitter_analysis:
                self.algorithms[algo_id] = TwitterAnalysis(algo_id, algo_values, self.data_modules, self.oracle)

            elif algo_values[definitions.algorithm] == definitions.virtual_transfer:
                self.algorithms[algo_id] = VirtualTransfer(algo_id, algo_values, self.data_modules, self.oracle)

            else:
                raise ValueError("Bad algorithm: '"
                +algo_id+"'.")

        print("\nAlgorithms:")
        pprint(self.algorithms) 

    def _build_portfolio(self):

        """
        + Description: build portfolio based on individual wallets.
        + Input:
        -
        + Output:
        -
        """
        self.portfolio = Portfolio(self.world, self.exchanges_names)
        print("\nPortfolio")
        pprint(self.portfolio.balance)

    def _build_trading_platform(self):

        """
        + Description: build trading platform.
        + Input:
        -
        + Output:
        -
        """

        self.trading = Trade(
            self.world,
            self.oracle,
            self.assets,
            self.portfolio,
            self.request_pile,
            self.request_flag
        )
        print("\nTrading platform")
        pprint(self.trading)

    def _build_request_structure(self):

        """
        + Description: build pile and threads to perform parallel request.
        + Input:
        -
        + Output:
        -
        """
        
        print("\nBuilding request structure")
        self.request_pile = Queue()
        self.request_flag = [0]
        self.request_workers = [RequestWorker(i, self.request_pile, self.request_flag, Lock()) 
                                for i in range(self.n_request_threads)]
      
        _ = list(map(lambda x: x.start(), self.request_workers))

    def _build_strategies(self):

        """
        + Description: build strategies based on algorithms.
        + Input:
        -
        + Output:
        -
        """
        
        self.strategies = {}
        for strategy_id, strategy_values in self.strategies_elements.items():
            
            self.strategies[strategy_id] = Strategy(strategy_id,
                                            strategy_values,
                                            self.assets,
                                            self.request_pile,
                                            self.request_flag,
                                            self.algorithms,
                                            self.data_modules,
                                            self.portfolio,
                                            self.trading,
                                            self.oracle)

        print("\nStrategies:")
        pprint(self.strategies)

    def run(self):

        """
        + Description: execute loop on strategies.
        + Input:
        -
        + Output:
        -
        """

        while self.world.is_connected():
            
            self.world.show_time()
        
            for strategy in self.strategies.values():                
                strategy.execute()
            
            self.world.advance_step()

        self._stop_workers()

        print("\nExecution finished")

        self.portfolio.show()

    def _stop_workers(self):

        """
        + Description: Final function that kill workers propertly.
        + Input:
        -
        + Output:
        -
        """       
		
        # send a 'None signal' to finish workers        
        for _ in range(self.n_request_threads):
            self.request_pile.put(None)

        for worker in self.request_workers:
            worker.join()
