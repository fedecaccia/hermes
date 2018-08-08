import definitions


class Wallet(object):

    """
    Wallet: Balance of funds in different account types for a given exchange.
    """

    def __init__(self, world, exchange_name):

        """
        + Description: constructor.
        + Input:
        - world: world object connection.
        - exchange_name: sstring exchange name.
        + Output:
        -
        """

        self.world = world
        self.exchange = exchange_name
        self.accounts = {
            definitions.trading: Account(),
            definitions.funding: Account(),
            definitions.margin_trading: Account()
        }


class Account(object):

    """
    Account: Balance of assets in a particular account for a given exchange.
    """

    def __init__(self):

        """
        Description: constructor.
        + Input:
        -
        + Output:
        -
        """

        self.assets = {}