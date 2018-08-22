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

    def __init__(self, algo_id, algo_values, data_modules, oracle):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - oracle: Oracle object.
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
        self._oracle = oracle
        self._fees = self._oracle.fees

    def _define_signals(self, signals):

        """
        + Description: Define signals parameters.
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

    def _reinitialize_signals(self):

        """
        + Description: Reinitialize signal values.
        + Input:
        -
        + Output:
        -
        """

        for asset in self._signals.keys():
            self._signals[asset]=0

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

    def __init__(self, algo_id, algo_values, data_modules, oracle):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - oracle: Oracle object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, oracle)

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
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """

        params = {asset:{
            definitions.limit:0,
            definitions.last:0
        } for asset in list(self._signals.keys())} 
        
        return self._signals, params


class Volume(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules, oracle):
        
        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - oracle: Oracle object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, oracle)
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

        algo_params = algo_values[definitions.algo_params]

        try:
            self._vol_growth = algo_params[definitions.vol_growth]
        except:
            raise ValueError("Error trying to parse vol_growth in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._vol_growth = algo_params[definitions.ma_periods]
        except:
            raise ValueError("Error trying to parse ma_periods in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._limit_buy_pct = algo_params[definitions.limit_buy_pct]
        except:
            raise ValueError("Error trying to parse limit_buy_pct in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._limit_sell_pct = algo_params[definitions.limit_sell_pct]
        except:
            raise ValueError("Error trying to parse limit_sell_pct in algorithm: '"+self.id+"' parameters.")
        
        try:
            self._usd_amount_to_trade = algo_params[definitions.usd_amount_to_trade]
        except:
            raise ValueError("Error trying to parse usd_amount_to_trade in algorithm: '"+self.id+"' parameters.")

    def evaluate(self):

        """
        + Description: execute algorithm
        + Input:
        -
        + Output:
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """

        # reinitialize signals
        self._reinitialize_signals()

        # asset key should be the same as defined in # Assets in config.py
        asset = list(self._signals.keys())[0]
        
        # quick access to exchange name
        exchange = self.data_modules[0].source

        # quick access to fees
        maker_fee = self._fees[exchange][definitions.trading][definitions.maker]
        taker_fee = self._fees[exchange][definitions.trading][definitions.taker]
        
        params = {asset:{
            definitions.limit:0,
            definitions.amount:0
        } for asset in list(self._signals.keys())} 

        # print(self.data_modules[0].data)
        ma_vol = self._get_last_sma_volume(periods = 5)
        vol = self._get_last_volume()
        
        ma_price = self._get_last_sma_price(periods = 5)
        prev_price = self._get_prev_price()
        last_price = self._get_last_price()

        # We don't resolve any signal when we don't have enough data
        if ma_vol is None or vol is None or ma_price is None or prev_price is None or last_price is None:
            return self._signals, params
        
        btc_usd = self._oracle.get_amount_in_base(
            definitions.btc,
            definitions.usd,
            self._usd_amount_to_trade
        )
        
        eth_usd = last_price*btc_usd

        if self._usd_amount_to_trade == definitions.full:
            amount = definitions.full
        else:
            amount = self._usd_amount_to_trade / eth_usd

        # high volume & prices over SMA & prices pumping
        if vol>ma_vol and last_price > ma_price and last_price > prev_price:
            self._shoot_long_signal(asset)
            params[asset] = {
                definitions.amount:amount,
                definitions.limit:last_price*self._limit_buy_pct/100.                
            }

        # high volume & prices below SMA & prices dumping
        elif vol>ma_vol and last_price < ma_price  and last_price < prev_price:
            self._shoot_short_signal(asset)
            params[asset] = {
                definitions.amount:amount,
                definitions.limit:last_price*self._limit_sell_pct/100.
            }
        else:

            # do nothing
            pass

        return self._signals, params

    def _get_last_sma_volume(self, periods):

        """
        + Description: Get last volume average volume using "periods".
        + Input:
        - periods: Integer number of periods to use in calculation.
        + Output:
        - sma_volume: Float last simple moving volume.
        """

        column = "vol_sma_"+str(periods)
        self.data_modules[0].compute_vol_sma(periods, column)

        if len(self.data_modules[0].data) > 1:
            return self.data_modules[0].data.iloc[-1][column]
        else:
            return None

    def _get_last_volume(self):

        """
        + Description: Get last volume
        + Input:
        -
        + Output:
        - last_volume: Float last volume.
        """
        
        if len(self.data_modules[0].data) > 1:
            return self.data_modules[0].data.iloc[-1][definitions.volume]
        else:
            return None

    def _get_last_sma_price(self, periods):

        """
        + Description: Calculate moving average price in "periods".
        + Input:
        - periods: Integer number of periods to use in calculation.
        + Output:
        - sma_price: Float last simple moving average price.
        """

        column = "sma_"+str(periods)
        self.data_modules[0].compute_sma(periods, column)
        if len(self.data_modules[0].data) > 1:
            return self.data_modules[0].data.iloc[-1][column]
        else:
            return None

    def _get_last_price(self):

        """
        + Description: Get last price.
        + Input:
        -
        + Output:
        - last_price: Float last price (close).
        """

        if len(self.data_modules[0].data) > 1:
            return self.data_modules[0].data.iloc[-1][definitions.close]
        else:
            return None

    def _get_prev_price(self):

        """
        + Description: Get previous price.
        + Input:
        -
        + Output:
        - prev_price: Float previous price (close).
        """

        if len(self.data_modules[0].data) > 2:
            return self.data_modules[0].data.iloc[-2][definitions.close]
        else:
            return None


class VirtualTransfer(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules, oracle):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - oracle: Oracle object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, oracle)

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
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """
        
        # if world_time >= arr[idx] and world_time-arr[idx]<=self._max_delay_in_data:
        params = {asset:{
            definitions.limit:0,
            definitions.last:0
        } for asset in list(self._signals.keys())} 
        
        return self._signals, params



class TwitterAnalysis(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules, oracle):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - oracle: Oracle object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, oracle)

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
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """

        params = {asset:{
            definitions.limit:0,
            definitions.last:0
        } for asset in list(self._signals.keys())} 
        
        return self._signals, params