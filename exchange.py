import definitions

import ccxt


class Exchange(object):

    """
    Exchange: client interface to connect with a particular exchange.
    """

    def __init__(self, exchange, keys):

        """
        + Description: Constructor.
        + Input:
        - exchange: Exchange string name.
        - keys: Dictionary of 'apiKey' and 'secret' or None object.
        + Output:
        -
        """

        self._initialize_client(exchange, keys)
        self._initialize_fees()

    def _initialize_client(self, exchange, keys):

        """
        + Description: Instantiate client to connect with exchange.
        + Input:
        - exchange: Exchange string name.
        - keys: Dictionary of 'apiKey' and 'secret' or None object.
        + Output:
        -
        """

        if keys is not None:
            self.client = getattr(ccxt, exchange)(keys)
        else:
            self.client = getattr(ccxt, exchange)()

    def _initialize_fees(self):

        """
        + Description: Load exchange fees.
        + Input:
        -
        + Output:
        -
        """

        self.fees = {}
        fees = self.client.describe()[definitions.fees]
        taker = fees[definitions.trading][definitions.taker]
        maker = fees[definitions.trading][definitions.maker]
        self.fees = {
            definitions.trading:{
                definitions.taker: taker,
                definitions.maker: maker
            }
        }


class Binance(Exchange):

    """
    Binance: client interface to connect with Binance.
    """

    def __init__(self, exchange, keys = None):

        """
        Description: Constructor.
        + Input:
        - exchange: Exchange string name.
        - keys: Dictionary of 'apiKey' and 'secret' or None object.
        + Output:
        -
        """

        super().__init__(exchange, keys)


class Bitfinex(Exchange):

    """
    Bitfinex: client interface to connect with Bitfinex.
    """

    def __init__(self, exchange, keys = None):

        """
        Description: Constructor.
        + Input:
        - exchange: Exchange string name.
        - keys: Dictionary of 'apiKey' and 'secret' or None object.
        + Output:
        -
        """

        super().__init__(exchange, keys)


class Bittrex(Exchange):

    """
    Bittrex: client interface to connect with Bittrex.
    """

    def __init__(self, exchange, keys = None):

        """
        Description: Constructor.
        + Input:
        - exchange: Exchange string name.
        - keys: Dictionary of 'apiKey' and 'secret' or None object.
        + Output:
        -
        """

        super().__init__(exchange, keys)