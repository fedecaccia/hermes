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
            definitions.trading: {},
            definitions.funding: {},
            definitions.margin_trading: {}
        }

    def update(self, balances):

        """
        + Description: Balance update function.
        + Input:
        - balances: Dictionary with asset balances per account type.
        + Output:
        -
        """

        for account, assets in balances.items():
            for asset, amount in assets.items():
                self.accounts[account][asset] = amount

    def show(self):

        """
        + Description: Print balances.
        + Input:
        -
        + Output:
        -
        """

        print("  "+self.exchange.capitalize()+" wallet:")
        for account, assets in self.accounts.items():
            print("    "+account.capitalize()+ " account:")
            for asset, amount in assets.items():
                print("      "+asset+": "+str(amount))
