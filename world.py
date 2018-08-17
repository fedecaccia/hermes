import definitions
import exchange

import dataset
import ccxt
import datetime

import numpy as np
import pandas as pd

from abc import ABC, abstractmethod


class World(ABC):

    """
    World: Connection with external services which provides exchange information and also receive trading orders.
    """

    def __init__(self, data_elements):

        """
        + Description: constructor
        + Input:
        - data_elements: Dictionary of data elements.
        + Output:
        -
        """

        self.data = data_elements

    @abstractmethod
    def advance_step(self):
        pass

    @abstractmethod
    def is_connected(self):
        pass

    @abstractmethod
    def get_time(self):
        pass

    @abstractmethod
    def request_data(self, data_module_id):
        pass

    @abstractmethod
    def request_balance(self, exchange):
        pass


class EmulatedWorld(World):

    """
    EmulatedWorld: Connection with databases and ficticious accounts.
    Inherit from World.
    """

    def __init__(self, data_elements, time_step):

        """
        + Description: constructor. Initializes corresponding data.
        + Input:
        - data_elements: Dictionary of data elements.
        - time_step: string time step to advance in each step.
        + Output:
        -
        """

        super().__init__(data_elements)
        self._initialize_data(data_elements)        
        self._time_step = time_step
        self._initialize_time_bounds()
        self._initialize_time()

    def _initialize_data(self, data_elements):

        """
        + Description: Initializes backtest data.
        + Input:
        - data_elements: Dictionary of data elements.
        + Output:
        -
        """

        for data_key, data_params in data_elements.items():
            self.data[data_key].update({
                definitions.values:self._load_data(data_params)
            })

    def _load_data(self, data_params):

        """
        + Description: Load particular data.
        + Input:
        - data_params: data module description.
        + Output:
        - data: Pandas element.
        """

        print("\nInitializing data module:")
        print("Description:", data_params[definitions.description])
        print("Source:", data_params[definitions.source])
        print("Data type:", data_params[definitions.data_type])
        if data_params[definitions.data_format] == definitions.csv:
            return self._load_data_from_csv(data_params)

        elif data_params[definitions.data_format] == definitions.sql:
            return  self._load_data_from_sql(data_params)

        elif data_params[definitions.data_format] == definitions.nosql:
            return  self._load_data_from_nosql(data_params)

        else:
            raise ValueError("Bad data_format.")

    def _load_data_from_csv(self, data_params):

        """
        Description: load data from csv into a dict of pandas elements.
        + Input:
        - data_params: data module description.
        + Output:
        - data values: a pandas object or a None object.
        """

        filename = data_params[definitions.file_name]
        data = None
        try:
            data = pd.read_csv(filename, parse_dates=True)
        except:
            raise ValueError("ERROR trying to find csv file: "+filename+".")
        else:
            data["datetime"] = pd.to_datetime(data["datetime"])
            data.set_index("datetime", inplace=True)
        return data

    def _load_data_from_sql(self, data_params):

        """
        Description: load data from sql into a dict of pandas elements.
        + Input:
        - data_params: data module description.
        + Output:
        - data values: a pandas object or a None object.
        """

        db = dataset.connect(data_params[definitions.db_path])
        table_name = data_params[definitions.table_name]
        header_format = data_params[definitions.header_format]   
        table = None     
        if header_format == definitions.cdm:
            table = pd.read_sql(sql=table_name,
                                con=db,
                                parse_dates="datetime",
                                index_col="datetime")
            table["datetime"] = pd.to_datetime(table["datetime"])
            table.set_index("datetime", inplace=True)
        else:
            raise ValueError("ERROR trying to read sql tables with header_format: '"
                            +header_format+"'.")
        return table
    
    def _load_data_from_nosql(self, data_params):

        """
        Description: load data from nosql into a dict of pandas elements.
        + Input:
        - data_params: data module description.
        + Output:
        - data values: a pandas object or a None object.
        """
        
        data = None
        return data

    def _initialize_time_bounds(self):

        """
        Description: Creates self._min_time and self._max_time
        + Input:
        - data_params: data module description.
        + Output:
        -
        """

        sample = list(self.data.values())[0][definitions.values]
        self._min_time = self._get_min_datetime(sample)
        self._max_time = self._get_max_datetime(sample)

        for data_val in self.data.values():

            dataframe = data_val[definitions.values]

            min_time = self._get_min_datetime(dataframe)
            max_time = self._get_max_datetime(dataframe)

            if min_time<self._min_time:
                self._min_time = min_time

            if max_time>self._max_time:
                self._max_time = max_time

    def _initialize_time(self):

        """
        Description: Start world time as the minor time in database.
        + Input:
        -
        + Output:
        -
        """

        self._time = self._min_time

    def _get_min_datetime(self, dataframe):

        """
        Description: return min timestamp in dataframe index.
        + Input:
        - dataframe: Pandas dataframe object.
        + Output:
        - min timestamp.
        """

        return pd.to_datetime(dataframe.index.min())

    def _get_max_datetime(self, dataframe):

        """
        Description: return max timestamp in dataframe index.
        + Input:
        - dataframe: Pandas dataframe object.
        + Output:
        - max timestamp.
        """

        return pd.to_datetime(dataframe.index.max())

    def is_connected(self):

        """
        Description: world connected is defined as true if there is more backtest data to evaluate.
        + Input:
        -
        + Output:
        - Connection: Bool
        """

        if self._time<self._max_time:
            return True
        return False

    def advance_step(self):

        """
        Description: Advance a time step in the simulated world time.
        + Input:
        -
        + Output:
        -
        """

        self._time += self._get_timedelta()

    def _get_timedelta(self):

        """
        Description: Return a deltatime object based on self._time_step.
        + Input:
        -
        + Output:
        - timedelta: datetime.timedelta object.
        """

        if self._time_step == definitions.one_sec:
            return datetime.timedelta(seconds=1)
        
        elif self._time_step == definitions.one_min:
            return datetime.timedelta(minutes=1)
        
        elif self._time_step == definitions.five_min:
            return datetime.timedelta(minutes=5)

        elif self._time_step == definitions.thirty_min:
            return datetime.timedelta(minutes=30)
        
        elif self._time_step == definitions.one_hour:
            return datetime.timedelta(hours=1)
        
        elif self._time_step == definitions.four_hour:
            return datetime.timedelta(hours=4)
        
        elif self._time_step == definitions.six_hour:
            return datetime.timedelta(hours=6)
        
        elif self._time_step == definitions.one_day:
            return datetime.timedelta(hours=24)

        else:
            raise ValueError("Bad value in step_time: '"+self._time_step+"'.")

    def get_time(self):

        """
        Description: Return world time.
        + Input:
        -
        + Output:
        - self._time: pandas timestamp.
        """

        return self._time

    def request_data(self, data_module_id):

        """
        + Description: request especific data according to data_module_id.
        + Input:
        - data_module_id: data module id integer.
        + Output:
        - requested data.
        """

        data_module = self.data[data_module_id]
        data = data_module[definitions.values]
        try:
            # Slowest approach
            # idx = data.index.get_loc(key=self._time,
            #                          method="pad", # only looks for previous time
            #                          tolerance=datetime.timedelta(seconds=self._max_delay_in_data)

            # Alternative approach
            arr = data.index.astype(int)//10**9 # To convert to Unix time
            world_time = pd.to_datetime(self._time).timestamp() # To convert your search value to Unix time
            idx = np.searchsorted(arr, world_time, side='left') # How many elements smaller
            
            if arr[idx]>world_time: # this case only is false when arr[idx]==world_time
                idx -= 1 # minus one to get previous index

        except:
            return None

        else:

            # if world_time >= arr[idx] and world_time-arr[idx]<=self._max_delay_in_data:
            row = data.iloc[idx]
            #     print("YAHOO")
            # else:
            #     return None

        return row

    def request_balance(self, exchange):

        """
        + Description: query to request exchange balances.
        + Input:
        - exchange: exchange name string
        + Output:
        - balance: dict with accounts balances.
        """

        return self._get_test_balance()

    def _get_test_balance(self):
        
        """
        + Description: test balance.
        + Input:
        -
        + Output:
        - balance: dict with accounts balances.
        """        
        
        balance = {
            definitions.trading:{
                definitions.usd:100,
                definitions.btc:100,
                definitions.eth:100
            },
            definitions.funding:{
                definitions.usd:0
            },
            definitions.margin_trading:{
                definitions.usd:100,
                definitions.btc:100,
                definitions.eth:100,
                definitions.margin:100
            }
        }

        return balance

class RealWorld(World):

    """
    RealWorld: Connection with exchanges.
    Inherit from World.
    """

    def __init__(self, data_elements, mode, exchanges_names, api_keys_files = None):

        """
        + Description: constructor
        + Input:
        - data_elements: Dictionary of data elements.
        - mode: string trading mode.
        - exchanges_names = set cointaining unique string names of exchanges.
        - api_keys_files = lsit of api key files in case private connections are needed.
        + Output:
        -
        """

        super().__init__(data_elements)
        self.mode = mode
        if self.mode == definitions.real:
            self.exchanges = self._create_clients_with_private_connections(exchanges_names, api_keys_files)

    def _create_clients_with_private_connections(self, exchanges_names, api_keys_files):
        
        """
        + Description: create clients which connects whith exchanges using API.
        Clients are connected via private keys to enable using private methods.
        + Input:
        - exchanges_names: list of strings with exchanges names.
        - keys: dict of api keys.
        + Output:
        - list of exchanges clients.
        """

        exchanges = []
        for exchange in exchanges_names:

            keys = self._load_api_keys(api_keys_files[exchange])

            if exchange == definitions.bittrex:
                exchange.append(exchange.Bittrex(keys))
            
            elif exchange == definitions.binance:
                exchange.append(exchange.Binance(keys))
            
            elif exchange == definitions.bitfinex:
                exchange.append(exchange.Bitfinex(keys))
            
            else:
                raise ValueError("Exchange: "+exchange+" has not private connection implemented")
        
        return exchanges

    def _load_api_keys(self, api_key_file):

        """
        + Description: load exchange api keys.
        + Input:
        - api_key_file: string file name where keys are located.
        + Output:
        - dict of api keys, using ccxt format.
        """

        keys = {
            'apiKey':None,
            'secret':None
        }

        try:
            api_key_file = open(api_key_file, "r")
            keys['apiKey'] = api_key_file.readline()
            if(keys['apiKey'][-1]=="\n"):
                keys['apiKey'] = keys['apiKey'][:-1]
            keys['secret'] = api_key_file.readline()
            if(keys['secret'][-1]=="\n"):
                keys['secret'] = keys['secret'][:-1]
            api_key_file.close()
        
        except:
            raise ValueError("ERROR: Trying to read key file: "+api_key_file)

        return keys

    def is_connected(self):

        """
        + Description: In case of real trading, verify private connection.
        + Input:
        -
        + Output:
        - Bool
        """

        return True

    def advance_step(self):

        """
        Description: Dummy function. It's definition only has sense in EmulatedWorld.
        + Input:
        -
        + Output:
        -
        """

        pass

    def get_time(self):

        """
        Description: Return world time.
        + Input:
        -
        + Output:
        - datetime
        """

        return datetime.datetime.now()

    def request_data(self, data_module_id):

        """
        + Description: request especific data according to data_module_id.
        + Input:
        - data_module_id: data module id integer.
        + Output:
        - requested data.
        """

        data_module = self.data[data_module_id]
        data_type = data_module[definitions.data_type]

        if data_type == definitions.orderbook:
            return self._request_orderbook(data_module[definitions.description],
                                           data_module[definitions.source])

        elif data_type == definitions.candles:
            return self._request_candles(data_module[definitions.description],
                                         data_module[definitions.source],
                                         data_module[definitions.timeframe],
                                         since=data_module[definitions.since],
                                         limit=data_module[definitions.limit])

        elif data_type == definitions.tickers:
            return self._request_tickers(data_module[definitions.source])

        elif data_type == definitions.tweets_count:
            return self._request_tweets_count(data_module[definitions.filters])

    def _request_orderbook(self, ticker, exchange):

        """
        + Description: query to request orderboooks for a given ticker.
        + Input:
        - ticker: string
        - exchange: exchange name string
        + Output:
        - orderbook: array of dicts
        """
        
        pass

    def _request_candles(self, ticker, exchange, timeframe, since=None, limit=1000):

        """
        + Description: query to request candles for a given ticker.
        + Input:
        - ticker: string
        - exchange: exchange name string
        - timeframe: string        
        - since: seconds passed since the first required candle
        - limit: maximum amount of candles
        + Output:
        - candles: array of dicts
        """

        client = getattr(ccxt, exchange)()
        tickers = client.fetch_ohlcv(ticker, timeframe, since, limit)
        return tickers

    def _request_tickers(self, exchange):
        
        """
        + Description: query to request tickers data.
        + Input:
        - ticker: string
        - exchange: exchange name string
        + Output:
        - tickers: array of dicts
        """

        pass

    def _request_tweets_count(self, filter):

        """
        + Description: query to request actual tweets filtered count.
        + Input:
        - filter: array of keyword strings to filter twitter stream.
        + Output:
        - tweets_count: Dictionary with datetime and integer twitter count.
        """

        tweets_count = {datetime.datetime.now(), 1000}
        return tweets_count

    def request_balance(self, exchange):

        """
        + Description: query to request exchange balances.
        + Input:
        - exchange: exchange name string
        + Output:
        - balance: dict with accounts balances.
        """

        pass

class Oracle(object):

    """
    Oracle: Fast information from databases or real world.
    """

    def __init__(self, world):

        """
        + Description: constructor
        + Input:
        - current world
        + Output:
        -
        """

        super().__init__()
        self.world = world
