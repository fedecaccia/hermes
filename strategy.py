from abc import ABC, abstractmethod


class Strategy(ABC):

    """
    Strategy: a generic class to implement data reception and algorithm evaluation.
    Based on a sum over individual algorithm punctuation values, takes a trading decision.
    """

    def __init__(self, algorithms, portfolio, trading):

        """
        + Description: constructor
        + Input:
        - algorithms: Array of algorithm objects.
        - portfolio: portfolio object.
        - trading: trading platform object.
        + Output:
        -
        """

        self.algorithms = algorithms
        self.portfolio = portfolio
        self.trading = trading