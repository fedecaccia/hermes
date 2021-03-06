import definitions
from exchange import *

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
    def request_data(self, data_module_id, barrier):
        pass

    @abstractmethod
    def request_balance(self, exchange):
        pass

    @abstractmethod
    def post_order(self, params):
        pass

    @abstractmethod
    def update_tickers(self):
        pass

    @abstractmethod
    def get_tickers(self):
        pass

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

    def _load_uid(self, uid_file):

        """
        + Description: load exchange uid (required in some exchanges, like Bitstamp).
        + Input:
        - uid_file: string file name where uid is located.
        + Output:
        - uid: string.
        """

        try:
            uid_file = open(uid_file, "r")
            uid = uid_file.readline()
            uid_file.close()
        
        except:
            raise ValueError("ERROR: Trying to read uid file: "+uid_file)

        return uid

    def _create_clients(self, exchanges_names, api_keys_files, uid_files):
        
        """
        + Description: create clients which connects whith exchanges using API.
        Clients could be connected via private keys to enable using private methods.
        + Input:
        - exchanges_names: List of strings with exchanges names.
        - api_keys_files: List of api key files in case private connections are needed
        - uid_files: List of uid files in case private connections are needed (requested by Bitsamp)
        + Output:
        -
        """

        self._exchanges = {}
        for exchange in exchanges_names:

            keys = None
            if api_keys_files is not None:
                keys = self._load_api_keys(api_keys_files[exchange])
            
            if exchange == definitions.binance:
                self._exchanges[exchange] = Binance(exchange, keys)
            
            elif exchange == definitions.bitfinex:
                self._exchanges[exchange] = Bitfinex(exchange, keys)
            
            elif exchange == definitions.bitstamp:
                uid = self._load_uid(uid_files[exchange])
                keys[definitions.uid] = uid
                self._exchanges[exchange] = Bitstamp(exchange, keys)
            
            elif exchange == definitions.bittrex:
                self._exchanges[exchange] = Bittrex(exchange, keys)
            
            elif exchange == definitions.cex:
                self._exchanges[exchange] = Cex(exchange, keys)
            
            elif exchange == definitions.coinex:
                self._exchanges[exchange] = Coinex(exchange, keys)
            
            elif exchange == definitions.exmo:
                self._exchanges[exchange] = Exmo(exchange, keys)
            
            elif exchange == definitions.gatecoin:
                self._exchanges[exchange] = Gatecoin(exchange, keys)
            
            elif exchange == definitions.gateio:
                self._exchanges[exchange] = Gateio(exchange, keys)
            
            elif exchange == definitions.gdax:
                self._exchanges[exchange] = Gdax(exchange, keys)
            
            elif exchange == definitions.gemini:
                self._exchanges[exchange] = Gemini(exchange, keys)
            
            elif exchange == definitions.hitbtc:
                self._exchanges[exchange] = Hitbtc(exchange, keys)
            
            elif exchange == definitions.huobipro:
                self._exchanges[exchange] = Huobipro(exchange, keys)
            
            elif exchange == definitions.kraken:
                self._exchanges[exchange] = Kraken(exchange, keys)
            
            elif exchange == definitions.kucoin:
                self._exchanges[exchange] = Kucoin(exchange, keys)
            
            elif exchange == definitions.okex:
                self._exchanges[exchange] = Okex(exchange, keys)
            
            elif exchange == definitions.poloniex:
                self._exchanges[exchange] = Poloniex(exchange, keys)
            
            elif exchange == definitions.yobit:
                self._exchanges[exchange] = Yobit(exchange, keys)
            
            else:
                raise ValueError("Exchange: "+exchange+" has not private connection implemented")

    def _initialize_fees(self):

        """
        + Description: Initialize a dictionary of fees to quick public access.
        + Input:
        -
        + Output:
        -
        """

        self.fees = {}
        for exchange_key, client in self._exchanges.items():
                maker = client.fees[definitions.trading][definitions.maker]
                taker = client.fees[definitions.trading][definitions.taker]
                self.fees[exchange_key] = {
                    definitions.trading:{
                        definitions.taker:taker,
                        definitions.maker:maker,
                    }
                }


class EmulatedWorld(World):

    """
    EmulatedWorld: Connection with databases and ficticious accounts.
    Inherit from World.
    """

    def __init__(
        self,
        data_elements,
        exchanges_names,
        time_step,
        virtual_portfolio,
        virtual_tickers):

        """
        + Description: constructor. Initializes corresponding data.
        + Input:
        - data_elements: Dictionary of data elements.
        - exchanges_names: List of exchange string names.
        - time_step: String time step to advance in each step.
        - virtual_portfolio: Dictionary containing virtual portfolio.
        - virtual_tickers: Dictionary containing virtual tickers.
        + Output:
        -
        """

        super().__init__(data_elements)
        self._initialize_data(data_elements)        
        self._time_step = time_step
        self._initialize_time_bounds()
        self._initialize_time()
        self._initialize_virtual_portfolio(virtual_portfolio)
        self._create_clients(exchanges_names, None, None)
        self._initialize_fees()
        self.virtual_tickers = virtual_tickers
        self.last_idx = 0

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

    def show_time(self):

        """
        Description: Print world time.
        + Input:
        -
        + Output:
        -
        """

        print("\nWORLD TIME: "+str(self._time))

    def _initialize_virtual_portfolio(self, virtual_portfolio):

        """
        Description: Initialize a virtual portfolio.
        + Input:
        -
        + Output:
        -
        """

        self._virtual_portfolio = virtual_portfolio

    def request_data(self, data_module_id, barrier):

        """
        + Description: request especific data according to data_module_id.
        + Input:
        - data_module_id: data module id integer.
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        + Output:
        - requested data.
        """

        barrier.wait() # this function has not sense in backtesting
        
        data_module = self.data[data_module_id]
        data = data_module[definitions.values]
        try:

            # Slowest approach
            # idx = data.index.get_loc(key=self._time,
            #                          method="pad", # only looks for previous time
            #                          tolerance=datetime.timedelta(seconds=self._max_delay_in_data)

            # Alternative approach
            # arr = data.index.astype(int)//10**9 # To convert to Unix time
            # arr = pd.to_datetime(data.index).timestamp() # To convert to Unix time
            
            arr = [x.timestamp() for x in data.index[:]]

            world_time = pd.to_datetime(self._time).timestamp() # To convert your search value to Unix time
            idx = np.searchsorted(arr, world_time, side='left') # How many elements smaller
            
            if arr[idx]>world_time and idx>0: # arr[idx]>world_time only is false when arr[idx]==world_time
                idx -= 1 # minus one to get previous index
            
            if arr[idx]>world_time and idx==0: # initial case, when current data is the first, newer than world_time
                return None # data is younger than the world_time

        except:
            return None

        else:

            # if world_time >= arr[idx] and world_time-arr[idx]<=self._max_delay_in_data:
            #     return data.iloc[idx]
            #     print("YAHOO")
            # else:
            #     return None
            if data_module[definitions.data_type] == definitions.candles:
                limit = data_module[definitions.limit]
                idx0 = max(0,idx-(limit-1))

                request = []
                for i in range(idx0, idx+1):
                    request.append(np.insert(np.array(data.iloc[i]), 0, arr[i], axis=0))
                    
            elif data_module[definitions.data_type] == definitions.orderbook:
                request = dict(data.iloc[idx])                
                request["datetime"] = data.index[idx]

            else:
                request = np.insert(np.array(data.iloc[idx]), 0, arr[idx], axis=0)

        return request

    def request_balance(self, exchange):

        """
        + Description: query to request exchange balances.
        + Input:
        - exchange: Exchange string name.
        + Output:
        - balance: Dictionary with asset balances per account type.
        """

        return self._virtual_portfolio[exchange]

    def post_order(self, params):

        """
        + Description: Constructor.
        + Input:
        - params: Dictionary containing order parameters.
        + Output:
        -
        """

        symbol = params[definitions.symbol]
        exchange = params[definitions.exchange]
        account = params[definitions.account]
        side = params[definitions.side]
        amount = params[definitions.amount]
        order_type = params[definitions.order_type]
        params = params[definitions.params]

        print("Executing order:", symbol, exchange, account, side, amount, order_type, params)
        order_id = 0

        self._virtual_operation(symbol, exchange, account, side, amount, order_type, params)

    def _virtual_operation(self, symbol, exchange, account, side, amount, order_type, params):

        """
        + Description: Update virtual portfolio.
        + Input:
        - symbol: Symbol string.
        - exchange: Exchange string name.
        - account: Account type string name.
        - side: "sell" or "buy" strings.
        - amount: Float amount of the operations.
        - order_type: String type of order.
        - params: Dictionary of order parameters.
        + Output:
        -
        """

        if order_type==definitions.limit:
            try:
                price = params[definitions.limit]                
            except:
                raise ValueError("Bad dictionary in params of operation.")
            try:
                fee = self.fees[exchange][definitions.trading][definitions.maker]
            except:
                raise ValueError("Fees have not been loaded propertly.")
        
        elif order_type==definitions.market:
            try:
                price = params[definitions.last]
            except:
                raise ValueError("Bad dictionary in params of operation.")
            try:
                fee = self.fees[exchange][definitions.trading][definitions.taker]
            except:
                raise ValueError("Fees have not been loaded propertly.")

        else:
            # nothing to do with stop / stop_limit / trailing_stop orders
            return

        base = symbol.split("/")[0]
        quote = symbol.split("/")[1]        

        try:
            if side == definitions.buy:
                self._virtual_portfolio[exchange][account][base][definitions.free] += amount
                self._virtual_portfolio[exchange][account][base][definitions.total] += amount
                self._virtual_portfolio[exchange][account][quote][definitions.free] -= amount*price*(1+fee)
                self._virtual_portfolio[exchange][account][quote][definitions.total] -= amount*price*(1+fee)

            elif side == definitions.sell:
                self._virtual_portfolio[exchange][account][base][definitions.free] -= amount
                self._virtual_portfolio[exchange][account][base][definitions.total] -= amount
                self._virtual_portfolio[exchange][account][quote][definitions.free] += amount*price*(1-fee)
                self._virtual_portfolio[exchange][account][quote][definitions.total] += amount*price*(1-fee)

        except:
            raise ValueError("Error in virtual portfolio trying to acces to exchange: '"+
            exchange + "', account: '"+account+"', base: '"+base+"' and quote: '"+quote+"'.")

    def update_tickers(self):

        """
        + Description: Update the dictionary with all tickers. Dummy function.
        + Input:
        -
        + Output:
        -
        """

        self.tickers = self.virtual_tickers

    def get_tickers(self):

        """
        + Description: Return a dictionary with all tickers.
        + Input:
        -
        + Output:
        - tickers: Dictionary with tickers from all exchanges connected.
        """
        
        return self.tickers


class RealWorld(World):

    """
    RealWorld: Connection with exchanges.
    Inherit from World.
    """

    def __init__(
        self,
        data_elements,
        exchanges_names,
        mode,
        api_keys_files = None,
        uid_files = None):

        """
        + Description: constructor
        + Input:
        - data_elements: Dictionary of data elements.
        - exchanges_names: List of exchange string names.
        - mode: String trading mode.
        - api_keys_files = List of api key files in case private connections are needed.
        - uid_files = List of uid files in case private connections are needed
         (requested by Bitstamp, for example).
        + Output:
        -
        """

        super().__init__(data_elements)

        self._create_clients(exchanges_names, api_keys_files, uid_files)
        self._initialize_fees()

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

    def show_time(self):

        """
        Description: Print world time.
        + Input:
        -
        + Output:
        - datetime
        """

        print("\nWORLD TIME: "+str(datetime.datetime.now()))

    def request_data(self, data_module_id, barrier):

        """
        + Description: request especific data according to data_module_id.
        + Input:
        - data_module_id: data module id integer.
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        + Output:
        - requested data.
        """

        data_module = self.data[data_module_id]
        data_type = data_module[definitions.data_type]

        if data_type == definitions.orderbook:
            return self._request_orderbook(
                barrier,
                data_module[definitions.description],
                data_module[definitions.source]
            )

        elif data_type == definitions.candles:
            return self._request_candles(
                barrier,
                data_module[definitions.description],
                data_module[definitions.source],
                data_module[definitions.timeframe],
                since=data_module[definitions.since],
                limit=data_module[definitions.limit]                
            )

        elif data_type == definitions.tickers:
            return self._request_tickers(
                barrier,
                data_module[definitions.source]
            )

        elif data_type == definitions.tweets_count:
            return self._request_tweets_count(
                barrier,
                data_module[definitions.filters]
            )

    def _request_orderbook(self, barrier, ticker, exchange):

        """
        + Description: query to request orderboooks for a given ticker.
        + Input:
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        - ticker: string
        - exchange: exchange name string        
        + Output:
        - orderbook: Array of dictionaries.
        """

        orderbook = self._exchanges[exchange].get_orderbook(ticker, barrier)
        return orderbook

    def _request_candles(self, barrier, ticker, exchange, timeframe, since=None, limit=1000):

        """
        + Description: query to request candles for a given ticker.
        + Input:
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        - ticker: string
        - exchange: exchange name string
        - timeframe: string        
        - since: seconds passed since the first required candle
        - limit: maximum amount of candles        
        + Output:
        - candles: Array of dictionaries.
        """

        candles = self._exchanges[exchange].get_candles(ticker, timeframe, since, limit, barrier)
        return candles

    def _request_tickers(self, barrier, exchange):
        
        """
        + Description: query to request tickers data.
        + Input:
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        - ticker: string
        - exchange: exchange name string        
        + Output:
        - tickers: array of dicts
        """

        tickers = self._exchanges[exchange].get_tickers(barrier)
        return tickers

    def _request_tweets_count(self, barrier, filters):

        """
        + Description: query to request actual tweets filtered count.
        + Input:
        - filters: array of keyword strings to filter twitter stream.
        - barrier: Barrier created to synchronize the threads that are working specifically now.
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
        - balance: dict with asset balances per account.
        """

        balances = {
            definitions.margin_trading: self._exchanges[exchange].get_margin_balance(),
            definitions.trading: self._exchanges[exchange].get_trading_balance()
        }

        return balances

    def update_tickers(self):

        """
        + Description: Update the dictionary with all tickers.
        + Input:
        -
        + Output:
        -
        """

        self.tickers = {}
        for client in self._exchanges.values():
            tickers = client.get_tickers_in_serial()
            if tickers is not None:
                self.tickers.update(tickers)

    def get_tickers(self):

        """
        + Description: Return a dictionary with all tickers.
        + Input:
        -
        + Output:
        - tickers: Dictionary with tickers from all exchanges connected.
        """
        
        return self.tickers

    def post_order(self, parameters):

        """
        + Description: constructor
        + Input:
        - parameters: Dictionary containing order parameters.
        + Output:
        -
        """

        symbol = parameters[definitions.symbol]
        exchange = parameters[definitions.exchange]
        account = parameters[definitions.account]
        side = parameters[definitions.side]
        amount = parameters[definitions.amount]
        order_type = parameters[definitions.order_type]
        order_pile = parameters[definitions.order_pile]
        params = parameters[definitions.params]        

        print("Executing order:", symbol, exchange, account, side, amount, order_type, params)

        if account == definitions.trading:
            order_id = self._exchanges[exchange].post_trading_order(
                symbol,
                side,
                amount,
                order_type,
                params
            )
            order = {
                definitions.exchange: exchange,
                definitions.order_id: order_id,
                definitions.amount: amount,
                definitions.symbol: symbol
            }
            order_pile.put(order)

    def check_order(self, exchange, symbol, order_id):

        """
        + Description: Check specific order status by order id for a particular exchange.
        + Input:
        - exchange: Exchange string name.
        - symbol: String symbol, only required in some particular exchanges like Yobit.
        - order_id: Order id string.
        + Output:
        - response: dictionary with order status.
        """

        print("Checking order id in: "+exchange)
        response = self._exchanges[exchange].get_order_status(symbol, order_id)

        # response = {'amount': 20.0,
        #             'average': 7.099e-05,
        #             'cost': 0.0014198,
        #             'datetime': '2018-10-18T14:30:18.743Z',
        #             'fee': {'cost': 3.54e-06, 'currency': 'BTC'},
        #             'filled': 20.0,
        #             'id': 'f36e86f0-6aed-47dc-a2e7-20f55ee3e295',
        #             'info': {'AccountId': None,
        #                     'CancelInitiated': False,
        #                     'Closed': '2018-10-18T14:30:18.79',
        #                     'CommissionPaid': 3.54e-06,
        #                     'CommissionReserveRemaining': 0.0,
        #                     'CommissionReserved': 0.0,
        #                     'Condition': 'NONE',
        #                     'ConditionTarget': None,
        #                     'Exchange': 'BTC-XRP',
        #                     'ImmediateOrCancel': False,
        #                     'IsConditional': False,
        #                     'IsOpen': False,
        #                     'Limit': 6e-05,
        #                     'Opened': '2018-10-18T14:30:18.743',
        #                     'OrderUuid': 'f36e86f0-6aed-47dc-a2e7-20f55ee3e295',
        #                     'Price': 0.0014198,
        #                     'PricePerUnit': 7.099e-05,
        #                     'Quantity': 20.0,
        #                     'QuantityRemaining': 0.0,
        #                     'ReserveRemaining': 20.0,
        #                     'Reserved': 20.0,
        #                     'Sentinel': '998ae81c-6634-425d-b559-7e995bc8b72e',
        #                     'Type': 'LIMIT_SELL'},
        #             'lastTradeTimestamp': 1539873018079,
        #             'price': 6e-05,
        #             'remaining': 0.0,
        #             'side': 'sell',
        #             'status': 'closed',
        #             'symbol': 'XRP/BTC',
        #             'timestamp': 1539873018743,
        #             'type': 'limit'}
        
        return response


class PaperWorld(RealWorld):

    """
    PaperWorld: Connection with exchanges just to request public data.
    Inherit from RealWorld.
    """

    def __init__(self, data_elements, exchanges_names, mode, virtual_portfolio):

        """
        + Description: constructor
        + Input:
        - data_elements: Dictionary of data elements.
        - exchanges_names: List of exchange string names.
        - mode: String trading mode.
        - virtual_portfolio = Dictionary containing a virtual portfolio.
        + Output:
        -
        """

        super().__init__(data_elements, exchanges_names, mode)
        self._virtual_portfolio = virtual_portfolio

    def request_balance(self, exchange):

        """
        + Description: query to request exchange balances.
        + Input:
        - exchange: Exchange string name.
        + Output:
        - balance: Dictionary with asset balances per account type.
        """

        return self._virtual_portfolio[exchange]

    def post_order(self, params):

        """
        + Description: Constructor.
        + Input:
        - params: Dictionary containing order parameters.
        + Output:
        -
        """

        symbol = params[definitions.symbol]
        exchange = params[definitions.exchange]
        account = params[definitions.account]
        side = params[definitions.side]
        amount = params[definitions.amount]
        order_type = params[definitions.order_type]
        params = params[definitions.params]

        print("Executing order in paper:", symbol, exchange, account, side, amount, order_type, params)
        order_id = 0

        self._virtual_operation(symbol, exchange, account, side, amount, order_type, params)

    def _virtual_operation(self, symbol, exchange, account, side, amount, order_type, params):

        """
        + Description: Update virtual portfolio.
        + Input:
        - symbol: Symbol string.
        - exchange: Exchange string name.
        - account: Account type string name.
        - side: "sell" or "buy" strings.
        - amount: Float amount of the operations.
        - order_type: String type of order.
        - params: Dictionary of order parameters.
        + Output:
        -
        """

        if order_type==definitions.limit:
            try:
                price = params[definitions.limit]                
            except:
                raise ValueError("Bad dictionary in params of operation.")
            try:
                fee = self.fees[exchange][definitions.trading][definitions.maker]
            except:
                raise ValueError("Fees have not been loaded propertly.")
        
        elif order_type==definitions.market:
            try:
                price = params[definitions.last]
            except:
                raise ValueError("Bad dictionary in params of operation.")
            try:
                fee = self.fees[exchange][definitions.trading][definitions.taker]
            except:
                raise ValueError("Fees have not been loaded propertly.")

        else:
            # nothing to do with stop / stop_limit / trailing_stop orders
            return

        base = symbol.split("/")[0]
        quote = symbol.split("/")[1]        

        try:
            if side == definitions.buy:
                self._virtual_portfolio[exchange][account][base][definitions.free] += amount
                self._virtual_portfolio[exchange][account][base][definitions.total] += amount
                self._virtual_portfolio[exchange][account][quote][definitions.free] -= amount*price*(1+fee)
                self._virtual_portfolio[exchange][account][quote][definitions.total] -= amount*price*(1+fee)

            elif side == definitions.sell:
                self._virtual_portfolio[exchange][account][base][definitions.free] -= amount
                self._virtual_portfolio[exchange][account][base][definitions.total] -= amount
                self._virtual_portfolio[exchange][account][quote][definitions.free] += amount*price*(1-fee)
                self._virtual_portfolio[exchange][account][quote][definitions.total] += amount*price*(1-fee)

        except:
            raise ValueError("Error in virtual portfolio trying to acces to exchange: '"+
            exchange + "', account: '"+account+"', base: '"+base+"' and quote: '"+quote+"'.")