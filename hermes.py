import definitions
import config

from world import EmulatedWorld, RealWorld, Oracle
from portfolio import Portfolio
from trade import Trade
from strategy import Strategy


class Hermes(object):

    """
    Hermes: the brain of the whole system. It could be replaced by an interface in future.
    """

    def __init__(self):

        """
        + Description: constructor.
        + Input:
        -
        + Output:
        -
        """

        self._load_config()
        self._build_system()
        self._connect_to_world()
        self._create_portfolio()
        self._create_trading_platform()
        self._build_tables()
        self._build_algorithms()
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
        self._load_data_modules()
        self._load_algorithms()
        self._load_strategies()

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

        if self.mode == definitions.backtest:
            self._load_backtesting_parameters()
        
        elif self.mode in [definitions.paper, definitions.real]:
            pass


    def _load_backtesting_parameters(self):

        """
        + Description: load backtesting parameters from user's input.
        + Input:
        -
        + Output:
        -
        """

        self._load_backtest_datatype()
        self._load_table_name_format()
        self._load_db_format()

    def _load_backtest_datatype(self):

        """
        + Description: load backtest data type.
        + Input:
        -
        + Output:
        -
        """

        try:
            self.backtest_datatype = config.backtest_datatype
        except:
            raise ValueError("Error trying to read backtest_datatype from config.py.")
        if self.backtest_datatype not in [definitions.csv, definitions.sql, definitions.nosql]:
            raise ValueError("Bad backtest_datatype.")

        if self.backtest_datatype == definitions.csv:
            try:
                self.csv_dir = config.csv_dir
            except:
                raise ValueError("Error trying to read csv_dir from config.py.")
        
        elif self.backtest_datatype == definitions.sql:
            try:
                self.sql_dir = config.sql_dir
            except:
                raise ValueError("Error trying to read sql_dir from config.py.")

        elif self.backtest_datatype == definitions.nosql:
            try:
                self.mogo_port = config.mongo_port
            except:
                raise ValueError("Error trying to read mongo_port from config.py.")

    def _load_table_name_format(self):

        """
        + Description: load table name format.
        + Input:
        -
        + Output:
        -
        """

        try:
            self.table_name_format = config.table_name_format
        except:
            raise ValueError("Error trying to read table_name_format from config.py.")
        if self.table_name_format not in [definitions.cdm]:
            raise ValueError("Bad table_name_format.")


    def _load_db_format(self):

        """
        + Description: load data base format.
        + Input:
        -
        + Output:
        -
        """

        try:
            self.db_format = config.db_format
        except:
            raise ValueError("Error trying to read table_name_format from config.py.")
        if self.db_format not in [definitions.cdm]:
            raise ValueError("Bad db_format.")

    def _load_data_modules(self):
        
        """
        + Description: load data modules.
        + Input:
        -
        + Output:
        -
        """
        
        self.data_modules = config.data_modules
        self._check_data_modules_consistency()

    def _check_data_modules_consistency(self):

        """
        + Description: check consistency in data modules.
        + Input:
        -
        + Output:
        -
        """
        pass


    def _load_algorithms(self):
        
        """
        + Description: load algorithms.
        + Input:
        -
        + Output:
        -
        """

        self.algorithms = config.algorithms
        self._check_algorithms_consistency()

    def _check_algorithms_consistency(self):

        """
        + Description: check consistency in algorithms.
        + Input:
        - 
        + Output:
        - 
        """
        pass
        
    def _load_strategies(self):
        
        """
        + Description: load strategies.
        + Input:
        -
        + Output:
        -
        """

        self.strategies = config.strategies
        self._check_strategies_consistency()

    def _check_strategies_consistency(self):

        """
        + Description: check consistency in strategies.
        + Input:
        -
        + Output:
        -
        """
        pass


    def _build_system(self):

        """
        + Description: build userful variables from config, like list of all exchanges, tickers, etc.
        + Input:
        -
        + Output:
        -
        """

        self.exchanges = set()
        for module in self.data_modules:
            if module[definitions.source] in definitions.all_exchanges:
                self.exchanges.update([module[definitions.source]])

    def _connect_to_world(self):

        """
        + Description: initialize connections.
        + Input:
        -
        + Output:
        -
        """

        if self.mode == definitions.backtest:
            self.world = EmulatedWorld()
        
        else:
            self.world = RealWorld(self.mode)
        
        self.oracle = Oracle(self.world)
        

    def _create_portfolio(self):

        """
        + Description: create portfolio based on individual wallets.
        + Input:
        -
        + Output:
        -
        """
        self.portfolio = Portfolio(self.world)

        pass

    def _create_trading_platform(self):

        """
        + Description: create trading platform.
        + Input:
        -
        + Output:
        -
        """

        self.trading = Trade(self.world, self.portfolio)

    def _build_tables(self):

        """
        + Description: create tables from data modules.
        + Input:
        -
        + Output:
        -
        """

        pass

    def _build_algorithms(self):

        """
        + Description: create algorithms based on tables.
        + Input:
        -
        + Output:
        -
        """

        pass

    def _build_strategies(self):

        """
        + Description: create strategies based on algorithms.
        + Input:
        -
        + Output:
        -
        """

        pass

    def run(self):

        """
        + Description: execute loop on strategies.
        + Input:
        -
        + Output:
        -
        """

        pass