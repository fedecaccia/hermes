import definitions
import config

from world import EmulatedExchangeWorld, RealExchangeWorld, Oracle
from data_module import Candles, Orderbook, Tickers, Tweets
from algorithm import CrossingMA, Volume, TwitterAnalysis, VirtualTransfer
from strategy import Strategy
from portfolio import Portfolio
from trade import Trade
from strategy import Strategy

from pprint import pprint


class Hermes(object):

    """
    Hermes: the brain of the whole system. It could be replaced by an interface in future.
    """

    def __init__(self):

        """
        + Description: Constructor. Builds main system.
        + Input:
        -
        + Output:
        -
        """

        self._load_config()
        self._unique_exchanges()
        self._connect_to_world()
        self._create_oracle()
        self._build_data_modules()
        self._build_algorithms()        
        self._build_portfolio()
        self._build_trading_platform()
        self._build_strategies()

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
        self._load_algorithms_elements()
        self._load_strategies_elements()

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

    def _unique_exchanges(self):
        
        """
        + Description: unique list of exchanges.
        + Input:
        -
        + Output:
        -
        """

        self.exchanges_names = set()
        for element in self.data_elements:
            if element[definitions.source] in definitions.all_exchanges:
                self.exchanges_names.update([element[definitions.source]])

        print("Unique list of exchanges")
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
            self.world = EmulatedExchangeWorld(self.data_elements)

        else:            
        
            if self.mode == definitions.paper:
                self.world = RealExchangeWorld(self.mode, self.exchanges_names)
            
            else:
                self.world = RealExchangeWorld(self.mode, self.exchanges_names, config.api_keys_files)

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
        for element in self.data_elements:

            key = element[definitions.data_id]
            
            if element[definitions.data_type] == definitions.candles:                
                self.data_modules[key] = Candles(element, self.world)
            
            elif element[definitions.data_type] == definitions.orderbook:
                self.data_modules[key] = Orderbook(element, self.world)
            
            elif element[definitions.data_type] == definitions.tickers:
                self.data_modules[key] = Tickers(element, self.world)
            
            elif element[definitions.data_type] == definitions.tweets_histogram:
                self.data_modules[key] = Tweets(element, self.world)

            else:
                raise ValueError("Bad data_type: '"
                +element[definitions.data_type]
                +' in module id: '+str(element[definitions.data_id])) 
        
        print("Data modules:")
        pprint(self.data_modules)     

    def _build_algorithms(self):

        """
        + Description: build algorithms based on data modules.
        + Input:
        -
        + Output:
        -
        """

        self.algorithms = {}
        for element in self.algorithms_elements:

            key = element[definitions.algorithm]
            data_ids = element[definitions.data_modules_array]
            data_modules = [self.data_modules[data_id] for data_id in data_ids]

            if element[definitions.algorithm] == definitions.crossing_ma:
                self.algorithms[key] = CrossingMA(data_modules)

            elif element[definitions.algorithm] == definitions.volume:
                self.algorithms[key] = Volume(data_modules)

            elif element[definitions.algorithm] == definitions.twitter_analysis:
                self.algorithms[key] = TwitterAnalysis(data_modules)

            elif element[definitions.algorithm] == definitions.virtual_transfer:
                self.algorithms[key] = VirtualTransfer(data_modules) 

            else:
                raise ValueError("Bad algorithm: '"
                +element[definitions.data_type])

        print("Algorithms:")
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

        pass

    def _build_trading_platform(self):

        """
        + Description: build trading platform.
        + Input:
        -
        + Output:
        -
        """

        self.trading = Trade(self.world, self.portfolio)

    def _build_strategies(self):

        """
        + Description: build strategies based on algorithms.
        + Input:
        -
        + Output:
        -
        """
        
        self.strategies = {}
        for element in self.strategies_elements:

            key = element[definitions.strategy_id]
            algorithm_ids = element[definitions.algorithms_array]
            algorithms = [self.algorithms[algo_id] for algo_id in algorithm_ids]

            self.strategies[key] = Strategy(algorithms, self.portfolio, self.trading)

        print("Strategies:")
        pprint(self.strategies) 

    def run(self):

        """
        + Description: execute loop on strategies.
        + Input:
        -
        + Output:
        -
        """

        pass