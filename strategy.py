from abc import ABC, abstractmethod


class Strategy(ABC):

    """
    Strategy: a generic class to implement data reception and algorithm evaluation.
    Based on a sum over individual algorithm punctuation values, takes a trading decision.
    """

    def __init__(self, world, portfolio, trading):

        """
        + Description: constructor
        + Input:
        - world
        - portfolio
        - strategy
        + Output:
        -
        """

        self.world = world
        self.portfolio = portfolio
        self.trading = trading