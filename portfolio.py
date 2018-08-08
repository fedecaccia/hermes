from wallet import Wallet


class Portfolio(object):

    """
    Portfolio: Global balance build with individual exchange wallets.
    """

    def __init__(self, world):

        """
        + Description: constructor
        + Input:
        - world
        + Output:
        -
        """

        self.world = world