import definitions

import datetime

import numpy as np

from abc import ABC, abstractmethod


class DataModule(ABC):

    """
    DataModule: Module to store data description, content and analysis.
    """

    def __init__(self, data_id, data_values, world):

        """
        + Description: constructor
        + Input:
        - data_id: Data id string.
        - data_values: Dictionary with main parameter values.
        - world:
        + Output:
        -
        """

        self._check_element_consistency(data_values)
        self.id = data_id
        self.description = data_values[definitions.description]
        self.source = data_values[definitions.source]
        self.data_type = data_values[definitions.data_type]
        self._world = world
        self.data = None
        self.last_data_datetime = 0
        self._initialize_data()
    
    @abstractmethod
    def _check_element_consistency(self, element):
        pass
    
    @abstractmethod
    def _initialize_data(self):
        pass

    def update(self, params):

        """
        Description: connection to world, to update values.
        + Input:
        - params: Dictionary with parameters passed to the request workers.
        + Output:
        -
        """

        try:
            barrier = params[definitions.barrier]
        except:
            raise ValueError("Barrier has not been received to update data module.")

        incoming_data = self._world.request_data(self.id, barrier)

        if self._data_is_new(incoming_data) and self._data_is_not_none(incoming_data):
            self._particular_update(incoming_data)
            print("Data module: "+str(self.id)+" updated.")

        else:
            print("Data module is old or None")

    def _data_is_new(self, incoming_data):
        
        """
        Description: evaluate wether incoming data is new or repeated.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """
        
        return True

    @abstractmethod
    def _particular_update(self, incoming_data):
        pass
    
    def _data_is_not_none(self, incoming_data):

        """
        Description: evaluate wether incoming data is None.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """

        if incoming_data is None:
            return False
        return True


class Candles(DataModule):

    """
    Candles: Module to store candles data description, content and analysis.
    """

    def __init__(self, data_id, data_values, world):

        """
        + Description: constructor
        + Input:
        - data_id: Data id string.
        - data_values: Dictionary with main parameter values.
        - world:
        + Output:
        -
        """

        super().__init__(data_id, data_values, world)
        self.ticker = data_values[definitions.description]
        self.exchange = data_values[definitions.source]
        self.timeframe = data_values[definitions.timeframe]

    def _check_element_consistency(self, data_values):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - data_values: Dictionary with main parameter values.
        + Output:
        -
        """

        pass

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        self.data = []

    def _particular_update(self, incoming_data):

        """
        Description: Update data.
        + Input:
        - incoming data: data received from client.
        + Output:
        -
        """
        
        candles = np.array(incoming_data)
    
        # discard last candle: yet incomplete
        candles = np.delete(candles, -1, 0)

        # remove old values
        for time in candles.transpose()[0]:
            if time <= self.last_data_datetime:
                candles = np.delete(candles, 0, 0)

        # if new values
        if len(candles)>0:

            # update last datetime
            self.last_data_datetime = candles[-1][0]
            
            for candle in candles:
                candle = {"datetime": candle[0],
                        # "symbol": symbol,
                        # "exchange": self.exchange,
                        "open":candle[1],
                        "high":candle[2],
                        "low":candle[3],
                        "close":candle[4],
                        "volume":candle[5]}

                self.data.append(candle)


class Orderbook(DataModule):

    """
    Orderbook: Module to store orderbook data description, content and analysis.
    """

    def __init__(self, data_id, data_values, world):

        """
        + Description: constructor
        + Input:
        - data_id: Data id string.
        - data_values: Dictionary with main parameter values.
        - world:
        + Output:
        -
        """

        super().__init__(data_id, data_values, world)
        self.ticker = data_values[definitions.description]
        self.exchange = data_values[definitions.source]

    def _check_element_consistency(self, data_values):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - data_values: Dictionary with main parameter values.
        + Output:
        -
        """

        pass

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        pass

    def _particular_update(self, incoming_data):
        
        """
        Description: Update data.
        + Input:
        - incoming data: data received from client.
        + Output:
        -
        """

        book = incoming_data
        if self.book_is_valid(book):
            bid_weight_val_1, bid_weight_count_1 = self.weighted_orders(book['bids'], limit=5)
            bid_weight_val_2, bid_weight_count_2 = self.weighted_orders(book['bids'], limit=10)
            ask_weight_val_1, ask_weight_count_1 = self.weighted_orders(book['asks'], limit=5)
            ask_weight_val_2, ask_weight_count_2 = self.weighted_orders(book['asks'], limit=10)
            data = {"datetime": datetime.now(),                    
                    "bid_weight_val_1":bid_weight_val_1,
                    "bid_weight_count_1":bid_weight_count_1,
                    "bid_weight_val_2":bid_weight_val_2,
                    "bid_weight_count_2":bid_weight_count_2,
                    "bid_val_2":book['bids'][2][0],
                    "bid_count_2":book['bids'][2][1],                    
                    "bid_val_1":book['bids'][1][0],
                    "bid_count_1":book['bids'][1][1],
                    "bid_val_0":book['bids'][0][0],
                    "bid_count_0":book['bids'][0][1],
                    "ask_val_0":book['asks'][0][0],
                    "ask_count_0":book['asks'][0][1],
                    "ask_val_1":book['asks'][1][0],
                    "ask_count_1":book['asks'][1][1],
                    "ask_val_2":book['asks'][2][0],
                    "ask_count_2":book['asks'][2][1], 
                    "ask_weight_val_1":ask_weight_val_1, 
                    "ask_weight_count_1":ask_weight_count_1, 
                    "ask_weight_val_2":ask_weight_val_2, 
                    "ask_weight_count_2":ask_weight_count_2}
        
            self.data.append(data)

    def book_is_valid(self, book):
        if book == None:
            return False
        if book == []:
            return False
        if len(book['bids'])<3:
            return False
        if len(book['asks'])<3:
            return False
        return True

    def weighted_orders(self, book, limit):
        
        weighted_value = 0
        count = 0

        for i_order, order in enumerate(book, 0):
            if i_order<limit:              
                weighted_value += order[0]*order[1]
                count += order[1]
            else:
                break

        try:
            weighted_value /= count
        except:
            print(self.exchange, book)

        return weighted_value, count


class Tickers(DataModule):

    """
    Tickers: Module to store tickers data description, content and analysis.
    """

    def __init__(self, data_id, data_values, world):

        """
        + Description: constructor
        + Input:
        - data_id: Data id string.
        - data_values: Dictionary with main parameter values.
        - world:
        + Output:
        -
        """

        super().__init__(data_id, data_values, world)
        self.ticker = data_values[definitions.description]
        self.exchange = data_values[definitions.source]
    
    def _check_element_consistency(self, data_values):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - data_values: Dictionary with main parameter values.
        + Output:
        -
        """

        pass

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        pass

    def _particular_update(self, incoming_data):
        
        """
        Description: Update data.
        + Input:
        - incoming data: data received from client.
        + Output:
        -
        """

        self.data.append(incoming_data)


class Tweets(DataModule):

    """
    Tweets: Module to store tweets data description, content and analysis.
    """

    def __init__(self, data_id, data_values, world):

        """
        + Description: constructor
        + Input:
        - data_id: Data id string.
        - data_values: Dictionary with main parameter values.
        - world:
        + Output:
        -
        """

        super().__init__(data_id, data_values, world)
        self.description = data_values[definitions.description]
        self.source = data_values[definitions.source]

    def _check_element_consistency(self, data_values):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - data_values: Dictionary with main parameter values.
        + Output:
        -
        """

        pass

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        pass

    def _particular_update(self, incoming_data):
        
        """
        Description: Update data.
        + Input:
        - incoming data: data received from client.
        + Output:
        -
        """

        self.data.append(incoming_data)