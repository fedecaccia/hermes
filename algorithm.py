import definitions

import copy

from abc import ABC, abstractmethod


class Algorithm(ABC):

    """
    Algorithm: a generic class to implement trading algorithm.
    Computes algorithm over a set of tickers and a set of echanges per ticker,
    with the same data_type: orderbooks, candles or tickers.
    Shoots a punctuation to Strategy.
    """

    def __init__(self, algo_id, algo_values, data_modules):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Dictionary of data module objects.
        + Output:
        -
        """
        
        self.id = algo_id
        self.data_modules = []
        self.data_modules_ids = []
        for data_module_id, data_module_values in data_modules.items():
            if data_module_id in algo_values[definitions.data_modules_array]:
                self.data_modules.append(data_module_values)
                self.data_modules_ids.append(data_module_id)
        self._check_data_modules()        
        self._define_signals(algo_values[definitions.signals])

    def _define_signals(self, signals):

        """
        + Description: define signals parameters
        + Input:
        - signals: Dictionary with long and short signal per asset id.
        + Output:
        -
        """

        # values to shoot with signals
        self._signals_values = signals
        
        # efective shoots
        self._signals = {}
        for asset, signals in signals.items():
            self._signals[asset] = {
                definitions.long_signal:0,
                definitions.short_signal:0
            }

    @abstractmethod
    def _check_data_modules(self):        
        pass

    @abstractmethod
    def _check_data_modules_amount(self):        
        pass

    @abstractmethod
    def _check_data_modules_description(self):        
        pass

    @abstractmethod
    def _check_data_modules_source(self):        
        pass

    @abstractmethod
    def _check_data_type(self):        
        pass

    @abstractmethod
    def evaluate(self):        
        pass

    def _shoot_long_signal(self, asset):

        """
        + Description: Save long signal.
        + Input:
        - asset: Asset id string name.
        + Output:
        -
        """

        self._signals[asset] = self._signals_values[asset][definitions.long_signal]

    def _shoot_short_signal(self, asset):

        """
        + Description: Save short signal.
        + Input:
        - asset: Asset id string name.
        + Output:
        -
        """

        self._signals[asset] = self._signals_values[asset][definitions.short_signal]


class CrossingMA(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules)

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

        if len(self.data_modules)!=1:
            raise ValueError("Error using: "+str(len(self.data_modules))+" data modules in algorithm with id: '"
                             +str(self.id)+"'. You can only use 1.")

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
            if module.data_type != definitions.candles:
                raise ValueError("Bad data type in data module id: "
                +str(module.id)
                +". Expected: "+definitions.candles)

    def evaluate(self):

        """
        + Description: execute algorithm
        + Input:
        -
        + Output:
        - signals: dictionary of signals returned for the algorithm
        """
        
        return self._signals


class Volume(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules):
        
        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules)
        self._check_parameters(algo_values)

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

        if len(self.data_modules)>1:
            raise ValueError("Error using: "+str(len(self.data_modules))+" data modules in algorithm with id: '"
                             +str(self.id)+"'. You can only use 1.")

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
            if module.data_type != definitions.candles:
                raise ValueError("Bad data type in data module id: "
                +str(module.id)
                +". Expected: "+definitions.candles)

    def _check_parameters(self, algo_values):

        params = algo_values[definitions.algo_params]

        try:
            self._vol_growth = params[definitions.vol_growth]
        except:
            raise ValueError("Error trying to parse vol_growth in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._vol_growth = params[definitions.ma_periods]
        except:
            raise ValueError("Error trying to parse ma_periods in algorithm: '"+self.id+"' parameters.")

    def evaluate(self):

        """
        + Description: execute algorithm
        + Input:
        -
        + Output:
        - signals: dictionary of signals returned for the algorithm
        """

        asset = list(self._signals.keys())[0]

        # print(self.data_modules[0].data)
        ma_vol = self._get_ma_volume(periods = 5)
        vol = self._get_last_volume()
        
        ma_price = self._get_ma_price(periods = 5)
        last_price = self._get_last_price()
        
        if vol>ma_vol and last_price > ma_price:
            self._shoot_long_signal(asset)
        else:
            self._shoot_short_signal(asset)

        return self._signals

    def _get_ma_volume(self, periods):

        """
        + Description: Calculate moving average volume in "periods".
        + Input:
        -
        + Output:
        - ma_volume: float
        """

        return 10

    def _get_last_volume(self):

        """
        + Description: Get last volume
        + Input:
        -
        + Output:
        - last_volume: float
        """

        return self.data_modules[0].data[-1]["volume"]

    def _get_ma_price(self, periods):

        """
        + Description: Calculate moving average price in "periods".
        + Input:
        -
        + Output:
        - ma_price: float
        """

        return 5

    def _get_last_price(self):

        """
        + Description: Get last price.
        + Input:
        -
        + Output:
        - last_price: float
        """

        return self.data_modules[0].data[-1]["close"]


class VirtualTransfer(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules)

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
                +str(self.data_modules[definitions.data_id]))

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
                +str(self.data_modules[definitions.data_id]))

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
                +str(self.data_modules[definitions.data_id])
                +". Expected: "+definitions.orderbook)

    def evaluate(self):

        """
        + Description: execute algorithm
        + Input:
        -
        + Output:
        - signals: dictionary of signals returned for the algorithm
        """
        
        # if world_time >= arr[idx] and world_time-arr[idx]<=self._max_delay_in_data:
        return self._signals


class TwitterAnalysis(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules)

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

        if len(self.data_modules)!=1:
            raise ValueError("Error using: "+str(len(self.data_modules))+" data modules in algorithm with id: '"
                             +str(self.id)+"'. You can only use 1.")

    def _check_data_modules_description(self):

        """
        + Description: check that data modules description received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.description not in definitions.counter:
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
            if module.source != definitions.twitter:
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
            if module.data_type != definitions.tweets_count:
                raise ValueError("Bad data type in data module id: "
                +str(module.id)
                +". Expected: "+definitions.tweets_count)

    def evaluate(self):

        """
        + Description: execute algorithm
        + Input:
        -
        + Output:
        - signals: dictionary of signals returned for the algorithm
        """
        
        return self._signals