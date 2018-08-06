import os
import pandas as pd
from abc import ABCMeta, abstractmethod


class Source (object):

    """
    Source: Retrieve data from specified source: database in backtesting mode or online data in paper_trading or real_trading modes.
    """

    def __init__(self, config):
        self.config = config

    @abstractmethod
    def request_order_books(self, ticker, exchanges):
        pass

    @abstractmethod
    def request_candles(self, ticker, exchanges):
        pass

    @abstractmethod
    def request_tickers(self, exchanges):
        pass


class DBSource(Source):

    """
    DBSource class: Retrieve data from database.
    Source's child.
    """

    def __init__(self, config):

        super(Source, self).__init__(config)
        self._initialize_data()
        
        if self.config.data_format == self.config.csv:
            self._load_data_from_csv()

        elif self.config.data_format == self.config.sql:
            self._load_data_from_sql()

        elif self.config.data_format == self.config.nosql:
            self._load_data_from_nosql()

        else:
            raise ValueError("Bad data_type.")

    def _initialize_data(self):

        """
        _initialize_data:
        build data structure.
        input: -
        output: -
        """

        # data as object per data type, per exchange id, per ticker

        self.data = {
            ticker:{
                exchange_id:{
                    data_type_id:None for data_type_id in self.config.data_type_ids[ticker].values()
                } for exchange_id in self.config.data_type_ids[ticker].keys()
            } for ticker in self.config.data_type_ids.keys()
        }

    def _load_data_from_csv(self):

        """
        _load_data_from_csv:
        load data from csv into a dict of pandas elements.
        input: config object.
        output: dict data. For each data[ticker][exchange] a pandas object or a None object is saved.
        Eeach element is a pandas dataframe or a None
        """

        for ticker, ticker_content in zip(self.data.keys(), self.data.values()):
            for exchange_id, data_types in zip(ticker_content.keys(), ticker_content.values()):
                for data_type_id in data_types:
                    filename = self.config.csv_dir\
                            + self.config.data_type_by_id[data_type_id]\
                            + self.config.exchange_name_by_id[exchange_id]\
                            + ticker.replace("/", "")\
                            + ".csv"
                    if os.path.exists(filename):
                        self.data[ticker][exchange_id][data_type_id]\
                        = pd.read_csv(filename, parse_dates=True)
                        self.data[ticker][exchange_id][data_type_id]["datetime"]\
                        = pd.to_datetime(self.data[ticker][exchange_id][data_type_id]["datetime"])
                        self.data[ticker][exchange_id][data_type_id].set_index("datetime", inplace=True)
                    else:
                        raise ValueError("I can't find csv file: "+filename+".")

    def _load_data_from_sql(self, config):

        """
        _load_data_from_sql:
        load data from sql into a dict of pandas elements.
        input: config object.
        output: dict data. For each data[ticker][exchange] a pandas object or a None object is saved.
        Eeach element is a pandas dataframe or a None
        """

        pass
    
    def _load_data_from_nosql(self, config):

        """
        _load_data_from_nosql:
        load data from mongodb into a dict of pandas elements.
        input: config object.
        output: dict data. For each data[ticker][exchange] a pandas object or a None object is saved.
        Eeach element is a pandas dataframe or a None
        """

        pass

    def request_order_books(self, ticker, exchanges, time):
        pass

    def request_candles(self, ticker, exchanges, time):
        pass

    def request_tickers(self, exchanges, time):
        pass


class OnlineSource(Source):

    """
    OnlineSource: Request data from exchanges online.
    Source's child.
    """

    def __init__(self, config):
        super(Source, self).__init__(config)

    def request_order_books(self, ticker, exchanges, time):
        pass

    def request_candles(self, ticker, exchanges, time):
        pass

    def request_tickers(self, exchanges, time):
        pass