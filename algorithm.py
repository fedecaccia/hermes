import definitions

from abc import ABC, abstractmethod


class Algorithm(ABC):

    """
    Algorithm: a generic class to implement trading algorithm.
    Computes algorithm over a set of tickers and a set of echanges per ticker,
    with the same data_type: orderbooks, candles or tickers.
    Shoots a punctuation to Strategy.
    """

    def __init__(self, algo_id, valuation, data_modules):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - valuation: Dictionary with passed and reprobed values.
        - data_modules: array of data module objects.
        + Output:
        -
        """
        
        self._id = algo_id
        self.data_modules = data_modules
        self._check_data_modules()
        self._define_valuation(valuation[definitions.passed],
                               valuation[definitions.reprobed])

    def _define_valuation(self, passed_value, reprobed_value):

        """
        + Description: define valuation parameters
        + Input:
        - passed_value: punctutation in case algorithm pass test
        - reprobed_value: punctutation in case algorithm reprobe test
        + Output:
        -
        """
        
        self._passed_value = passed_value
        self._reprobed_value = reprobed_value

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


class CrossingMA(Algorithm):

    def __init__(self, algo_id, valuation, data_modules, parameters):

        """
        + Description: Trading strategy based on moving average crossings.
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - valuation: Dictionary with passed and reprobed values.
        - data_modules: Array of data module objects.
        - parameters: Dictionary of specific algorithm parameters.
        + Output:
        -
        """
        
        super().__init__(algo_id, valuation, data_modules)

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
                             +str(self._id)+"'. You can only use 1.")

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
        
        if 0>1:
            valuation = self._reprobed_value
        else:
            valuation = self._passed_value

        return valuation


class Volume(Algorithm):

    def __init__(self, algo_id, valuation, data_modules, parameters):

        """
        + Description: Trading strategy based on volume analysis.
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - valuation: Dictionary with passed and reprobed values.
        - data_modules: Array of data module objects.
        - parameters: Dictionary of specific algorithm parameters.
        + Output:
        -
        """
        
        super().__init__(algo_id, valuation, data_modules)

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
                             +str(self._id)+"'. You can only use 1.")

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
        
        if 0>1:
            valuation = self._reprobed_value
        else:
            valuation = self._passed_value

        return valuation


class VirtualTransfer(Algorithm):

    def __init__(self, algo_id, valuation, data_modules, parameters):

        """
        + Description: Trading strategy based on statistical arbitrage.
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - valuation: Dictionary with passed and reprobed values.
        - data_modules: Array of data module objects.
        - parameters: Dictionary of specific algorithm parameters.
        + Output:
        -
        """
        
        super().__init__(algo_id, valuation, data_modules)

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
                             +str(self._id)+"'. You can only use 2.")

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
        
        if 0>1:
            valuation = self._reprobed_value
        else:
            valuation = self._passed_value

        return valuation


class TwitterAnalysis(Algorithm):

    def __init__(self, algo_id, valuation, data_modules, parameters):

        """
        + Description: Trading strategy based on twitter analysis.
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - valuation: Dictionary with passed and reprobed values.
        - data_modules: Array of data module objects.
        - parameters: Dictionary of specific algorithm parameters.
        + Output:
        -
        """
        
        super().__init__(algo_id, valuation, data_modules)

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
                             +str(self._id)+"'. You can only use 1.")

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
        - valuation: integer algorithm valuation
        """
        
        if 0>1:
            valuation = self._reprobed_value
        else:
            valuation = self._passed_value

        return valuation

        
