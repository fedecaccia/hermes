import definitions

from abc import ABC, abstractmethod

class Algorithm(ABC):

    """
    Algorithm: a generic class to implement trading algorithm.
    Computes algorithm over a set of tickers and a set of echanges per ticker,
    with the same data_type: orderbooks, candles or tickers.
    Shoots a punctuation to Strategy.
    """

    def __init__(self, algo_id, algo_values, data_modules, assets, oracle):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. It only saves what here cares.
        - assets: Array of all assets objetcs. It only saves what here cares.
        - oracle: Oracle object.
        + Output:
        -
        """
        
        self.id = algo_id
        self.data_modules_ids = [k for k in data_modules.keys() if k in algo_values[definitions.data_modules_array]]
        self.data_modules = [data_modules[k] for k in self.data_modules_ids]
        self._check_data_modules()

        self.assets = {}
        for asset_key, asset_values in assets.items():
            if asset_key in algo_values[definitions.signals].keys():
                self.assets[asset_key] = asset_values
                    
        self._check_parameters(algo_values)
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
    def _check_parameters(self, algo_values):        
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

    def get_usd_base_value(self, base, quote, base_price_in_quote):

        """
        + Description: Return USD price of base coin.
        + Input:
        - base: base pair string name.
        - quote: quote pair string name.
        - base_price_in_quote: price of base coin in quote coin.
        + Output:
        - usd_price: price of base coin in usd coin.
        """

        if quote==definitions.usd or quote==definitions.usdt:
            
            return base_price_in_quote # approximated price

        elif quote==definitions.btc:

            btc_usd = self._oracle.get_price(
                definitions.btc,
                definitions.usd
            )                   
            
            return base_price_in_quote*btc_usd # approximated price

        elif quote==definitions.eth:

            eth_usd = self._oracle.get_price(
                definitions.eth,
                definitions.usd
            )                   
            
            return base_price_in_quote*eth_usd # approximated price
        
        else:
            raise ValueError("Error trying to get USD value in pair: "+base+"/"+quote)
