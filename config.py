import settings

class Config (object):

    """
    Config: Load parameters from settings.py input file.
    """

    def __init__(self):

        self._load_definitions()
        self._load_from_settings()
        self._build_useful_variables()

    def _load_definitions(self):

        self.backtest_trading = "backtest_trading"
        self.paper_trading = "paper_trading"
        self.real_trading = "real_trading"

        self.csv = "csv"
        self.sql = "sql"
        self.nosql = "nosql"

    def _load_from_settings(self):

        # mode
        
        if settings.mode == self.backtest_trading:
            self.mode = self.backtest_trading
            self.data_format = settings.data_format

            if self.data_format == self.csv:
                self.csv_dir = settings.csv_dir
            
            elif self.data_format == self.sql:
                self.db_file = settings.db_file

            elif self.data_format == self.nosql:
                self.mongo_port = settings.mongo_port

        elif settings.mode == self.paper_trading:
            self.mode = self.paper_trading

        elif settings.mode == self.real_trading:
            self.mode = self.real_trading

        else:
            raise ValueError("Bad mode.")

        # strategies

        self.strategies = settings.strategies

        # exchange names by id
        
        try:
            self.exchange_name_by_id = {}
            for exchange in settings.exchanges:
                self.exchange_name_by_id[exchange["id"]] = exchange["name"]
        except Exception as err:
            print(err)
            raise ValueError("I can't build exchange_name_by_id from settings.exchanges")

        # exchange fees by id

        try:
            self.exchange_fees_by_id = {}
            for exchange in settings.exchanges:
                self.exchange_fees_by_id[exchange["id"]] = exchange["fees"]
        except Exception as err:
            print(err)
            raise ValueError("I can't build exchange_fees_by_id from settings.exchanges")

        # data type by id

        try:
            self.data_type_by_id = {}
            for data_type in settings.data_type:
                self.data_type_by_id[data_type["id"]] = data_type["name"]
        except Exception as err:
            print(err)
            raise ValueError("I can't build data_type_by_id from settings.data_type")
        

    def _build_useful_variables(self):

        # tickers

        try:
            self.tickers = set()
            for strategy in self.strategies:
                self.tickers.update(elem["ticker"] for elem in self.strategies[strategy].values())
        except Exception as err:
            print(err)
            raise ValueError("I can't build tickers from settings.strategy")

        # exchange ids per ticker
        
        self.exchange_ids = {
            ticker:set() for ticker in self.tickers
        }
        try:
            for strategy in self.strategies:
                self.exchange_ids[strategy["ticker"]].update(strategy["exchange_ids"])
        except Exception as err:
            print(err)
            raise ValueError("I can't build exchange_ids from settings.strategies")

        # data type per ticker and per exchange id

        self.data_type_ids = {
            ticker: {
                exchange_id: set() for exchange_id in self.exchange_ids[ticker]
            } for ticker in self.tickers
        }
        try:
            for strategy in self.strategies:
                for ticker in self.data_type_ids.keys():
                    for exchange_id in self.data_type_ids[ticker].keys():
                        self.data_type_ids[ticker][exchange_id].update(strategy["data_type_id"])
        except Exception as err:
            print(err)
            raise ValueError("I can't build data_type_ids from settings.strategies")
