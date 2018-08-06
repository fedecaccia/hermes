import config

from world import World
from portfolio import Portfolio
from trade import Trade
from strategy import Strategy


class Hermes(object):

    """
    Hermes: the brain of he whole system. It could be replaced by an interface in future.
    """

    def __init__(self):

        """
        + Description: constructor
        + Input:
        -
        + Output:
        -
        """

        self._load_config()
        self._build_system()
        self._connect_to_world()
        self._create_portfolio()
        self._create_trading_platform()
        self._build_strategies()

    def _load_config(self):

        """
        + Description: load configuration from user's input
        + Input:
        -
        + Output:
        -
        """

        pass

    def _build_system(self):

        """
        + Description: build userful variables from configuration
        + Input:
        -
        + Output:
        -
        """

        pass

    def _connect_to_world(self):

        """
        + Description: initialize connections
        + Input:
        -
        + Output:
        -
        """

        pass

    def _create_portfolio(self):

        """
        + Description: create portfolio based on individual wallets
        + Input:
        -
        + Output:
        -
        """

        pass

    def _create_trading_platform(self):

        """
        + Description: create trading platform
        + Input:
        -
        + Output:
        -
        """

        pass

    def _build_strategies(self):

        """
        + Description: create strategy objects based on user configuration
        + Input:
        -
        + Output:
        -
        """

        pass

    def run(self):

        """
        + Description: execute loop on strategies
        + Input:
        -
        + Output:
        -
        """

        pass