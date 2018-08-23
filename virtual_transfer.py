import definitions

from algorithm import Algorithm


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
            if module.data_type != definitions.orderbook:
                raise ValueError("Bad data type in data module id: "
               +str(module.id)
                +". Expected: "+definitions.orderbook)

    def _check_parameters(self, algo_values):

        """
        + Description: Check parameters received in algo_values dictionary.
        + Input:
        - algo values: Dictionary containing algorithmic parameters defined in config.py.
        + Output:
        -
        """

        algo_params = algo_values[definitions.algo_params]
        
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
        + Description: Execute algorithm evaluating virtual transfers based on arbitrage.
        + Input:
        -
        + Output:
        - signals: Dictionary of signals returned for the algorithm.
        - params: Dictionary of order parameters.
        """

        # reinitialize signals
        self._reinitialize_signals()

        # reinitialize parameters
        params = {asset:{
            definitions.limit:0,
            definitions.amount:0
        } for asset in list(self._signals.keys())}

        # asset key should be the same as defined in # Assets in config.py
        asset = list(self._signals.keys())[0]
        
        # quick access to exchange name
        exchange = self.data_modules[0].source

        # quick access to fees
        maker_fee = self._fees[exchange][definitions.trading][definitions.maker]
        taker_fee = self._fees[exchange][definitions.trading][definitions.taker]
        
        # if world_time >= arr[idx] and world_time-arr[idx]<=self._max_delay_in_data:
        

        return self._signals, params