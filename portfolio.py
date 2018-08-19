from wallet import Wallet


class Portfolio(object):

    """
    Portfolio: Global balance build with individual exchange wallets.
    """

    def __init__(self, world, exchanges_names):

        """
        + Description: constructor.
        + Input:
        - world: world object connection.
        - exchanges names: list of string exchange names.
        + Output:
        -
        """

        self.world = world
        self.exchanges_names = exchanges_names
        self.balance = {
            exchange_name: Wallet(world, exchange_name) for exchange_name in exchanges_names
        }
        self.update()


    def get_total_balance(self, coin):

        """
        + Description: returns total balance of portfolio valuated in coin.
        + Input:
        - coin: string of the reference coin.
        + Output:
        - value: float portfolio value in coin.
        """    

        pass

    def get_balance_in_exchange(self, coin, exchange):

        """
        + Description: returns balance of funds in a particular exchange valuated in coin.
        + Input:
        - coin: string of the reference coin.
        - exchange: string of the exchange.
        + Output:
        - value: float portfolio value in coin.
        """    

        pass

    def update(self):

        """
        + Description: Update each wallet.
        + Input:
        -
        + Output:
        -
        """

        for exchange in self.exchanges_names:
            self.balance[exchange].update(self.world.request_balance(exchange))

    def show(self):

        """
        + Description: Print wallets contents.
        + Input:
        -
        + Output:
        -
        """

        print(self.world.get_time())
        print("\nPortfolio:")
        for exchange in self.exchanges_names:
            self.balance[exchange].show()