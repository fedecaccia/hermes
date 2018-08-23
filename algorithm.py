import definitions

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