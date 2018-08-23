import definitions

from algorithm import Algorithm


class TwitterAnalysis(Algorithm):

    def __init__(self, algo_id, algo_values, data_modules, assets, oracle):

        """
        + Description: constructor
        + Input:
        - algo_id: Algorithm id (with particular combination of name, parameters and data modules).
        - algo_values: Dictionary with algorithm parameters values.
        - data_modules: Array of all data modules objects. Super only saves what here cares.
        - assets: Dictionary of all assets objetcs. Super only saves what here cares.
        - oracle: Oracle object.
        + Output:
        -
        """
        
        super().__init__(algo_id, algo_values, data_modules, assets, oracle)

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

    def _check_parameters(self, algo_values):

        """
        + Description: Check parameters received in algo_values dictionary.
        + Input:
        - algo values: Dictionary containing algorithmic parameters defined in config.py.
        + Output:
        -
        """

        pass

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

        params = {asset:{
            definitions.limit:0,
            definitions.amount:0
        } for asset in list(self._signals.keys())}
        
        return self._signals, params