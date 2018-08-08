import definitions

from abc import ABC, abstractmethod


class Algorithm(ABC):

    """
    Algorithm: a generic class to implement trading algorithm.
    Computes algorithm over a set of tickers and a set of echanges per ticker,
    with the same data_type: orderbooks, candles or tickers.
    Shoots a punctuation to Strategy.
    """

    def __init__(self, data_modules):

        """
        + Description: constructor
        + Input:
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        self.data_modules = data_modules
        self._check_data_modules()

    def _define_valuation(self, pass_value, reprobe_value):

        """
        + Description: define valuation parameters
        + Input:
        - pass_value: punctutation in case algorithm pass test
        - reprobe_value: punctutation in case algorithm reprobe test
        + Output:
        -
        """
        
        self.pass_value = pass_value
        self.reprobe_value = reprobe_value

    @abstractmethod
    def _check_data_modules(self):        
        
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


class CrossingMA(Algorithm):

    def __init__(self, data_modules):

        """
        + Description: Trading strategy based on moving average crossings.
        + Input:
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(data_modules)
        self._define_valuation(pass_value = 2, reprobe_value = -1)

    def _check_data_modules(self):

        """
        + Description: check that data module received is right.
        + Input:
        -
        + Output:
        -
        """
        
        self._check_data_modules_description()
        self._check_data_modules_source()
        self._check_data_type()

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
        - valuation: integer algorithm valuation
        """
        
        if 1>0:
            valuation = self.reprobe_value
        else:
            valuation = self.pass_value

        return valuation


class Volume(Algorithm):

    def __init__(self, data_modules):

        """
        + Description: Trading strategy based on volume analysis.
        + Input:
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(data_modules)
        self._define_valuation(pass_value = 1, reprobe_value = -1)

    def _check_data_modules(self):

        """
        + Description: check that data module received is right.
        + Input:
        -
        + Output:
        -
        """
        
        self._check_data_modules_description()
        self._check_data_modules_source()
        self._check_data_type()

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
        - valuation: integer algorithm valuation
        """
        
        if 1>0:
            valuation = self.reprobe_value
        else:
            valuation = self.pass_value

        return valuation


class VirtualTransfer(Algorithm):

    def __init__(self, data_modules):

        """
        + Description: Trading strategy based on statistical arbitrage.
        + Input:
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(data_modules)
        self._define_valuation(pass_value = 1, reprobe_value = 0)

    def _check_data_modules(self):

        """
        + Description: check that data module received is right.
        + Input:
        -
        + Output:
        -
        """
        
        self._check_data_modules_description()
        self._check_data_modules_source()
        self._check_data_type()

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
        - valuation: integer algorithm valuation
        """
        
        if 1>0:
            valuation = self.reprobe_value
        else:
            valuation = self.pass_value

        return valuation


class TwitterAnalysis(Algorithm):

    def __init__(self, data_modules):

        """
        + Description: Trading strategy based on twitter analysis.
        + Input:
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        super().__init__(data_modules)
        self._define_valuation(pass_value = 1, reprobe_value = 0)

    def _check_data_modules(self):

        """
        + Description: check that data module received is right.
        + Input:
        -
        + Output:
        -
        """
        
        self._check_data_modules_description()
        self._check_data_modules_source()
        self._check_data_type()

    def _check_data_modules_description(self):

        """
        + Description: check that data modules description received is right.
        + Input:
        -
        + Output:
        -
        """

        for module in self.data_modules:
            if module.description != definitions.tweets_count:
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
            if module.data_type != definitions.tweets_histogram:
                raise ValueError("Bad data type in data module id: "
                +str(module.id)
                +". Expected: "+definitions.tweets_histogram)

    def evaluate(self):

        """
        + Description: execute algorithm
        + Input:
        -
        + Output:
        - valuation: integer algorithm valuation
        """
        
        if 1>0:
            valuation = self.reprobe_value
        else:
            valuation = self.pass_value

        return valuation

        
