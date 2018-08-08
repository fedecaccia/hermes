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
            definitions.trading: None,
            definitions.funding: None,
            definitions.margin_trading: None
        }
        self.update()

    def update(self):

        """
        + Description: balance update function.
        + Input:
        -
        + Output:
        -
        """
        accounts = self.world.request_balance(self.exchange)
        self.accounts = {
            definitions.trading: accounts[definitions.trading],
            definitions.funding: accounts[definitions.funding],
            definitions.margin_trading: accounts[definitions.margin_trading]
        }