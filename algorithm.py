from abc import ABC, abstractmethod


class Algorithm(ABC):

    """
    Algorithm: a generic class to implement trading algorithm.
    Computes algorithm over a set of tickers and a set of echanges per ticker,
    with the same data_type: orderbooks, candles or tickers.
    Shoots a punctuation to Strategy.
    """

    def __init__(self, data_type, tickers, exchanges):

        """
        + Description: constructor
        + Input:
        - data_type: data type id
        - tickers: list of tickers
        - exchanges: dict with tickers (keys) and list of eschanges (value per key)
        + Output:
        -
        """
        
        self.data_type = data_type
        self.tickers = tickers
        self.exchanges = exchanges

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
    def run(self, tables):

        """
        + Description: execute algorithm
        + Input:
        - tables: data structure.
        + Output:
        -
        """
        
        pass


class TestingAlgorithm(Algorithm):

    def __init__(self, data_type, tickers, exchanges):

        """
        + Description: constructor
        + Input:
        - data_type: data type id
        - tickers: list of tickers
        - exchanges: dict with tickers (keys) and list of eschanges (value per key)
        + Output:
        -
        """
        
        super().__init__(data_type, tickers, exchanges)
        self._define_valuation(pass_value = 2, reprobe_value = -1)
        
    def run(self, tables):

        """
        + Description: execute algorithm
        + Input:
        - tables: data structure.
        + Output:
        -
        """
        
        pass

        
