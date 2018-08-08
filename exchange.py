class Exchange(object):

    """
    Exchange: client interface to connect with a particular exchange.
    """

    def __init__(self):

        """
        + Description: constructor
        + Input:
        -
        + Output:
        -
        """

        pass


class Binance(Exchange):

    """
    Binance: client interface to connect with Binance.
    """

    def __init__(self, keys = None):

        """
        Description: Constructor.
        + Input:
        - keys: dict with 'apiKey' and 'secret'.
        + Output:
        -
        """

        super().__init__()


class Bitfinex(Exchange):

    """
    Bitfinex: client interface to connect with Bitfinex.
    """

    def __init__(self, keys = None):

        """
        Description: Constructor.
        + Input:
        - keys: dict with 'apiKey' and 'secret'.
        + Output:
        -
        """

        super().__init__()


class Bittrex(Exchange):

    """
    Bittrex: client interface to connect with Bittrex.
    """

    def __init__(self ,keys = None):

        """
        Description: Constructor.
        + Input:
        - keys: dict with 'apiKey' and 'secret'.
        + Output:
        -
        """

        super().__init__()