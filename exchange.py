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

    def get_trading_balance(self):

        """
        + Description: Get balance in trading (exchange) account.
        + Input:
        -
        + Output:
        - trading_balance: Dictionary containing balances.
        """

        trading_balances = {}
        res = self.client.fetch_balances()

        for key, values in res.items():
            if key not in ["total", "free", "used", "info"]:
                trading_balances[key] = values

        return trading_balances

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

    def get_margin_balance(self):

        """
        + Description: Get margin trading balances and limits.
        + Input:
        -
        + Output:
        - margin_balance: Dictionary containing main margin balance parameters.

        Message returned in private_post_margin_infos from Bitfinex:
        'message': 'Margin requirement, leverage and tradable balance are now per '
        'pair. Values displayed in the root of the JSON message are '
        'incorrect (deprecated). You will find the correct ones under '
        'margin_limits, for each pair. Please update your code as soon as '
        'possible.'
        """    
        res = self.client.private_post_margin_infos()[0]
        
        leverage = res[definitions.bitfinex_leverage]
        # Your net value (the USD value of your trading wallet, including your margin balance, your unrealized P/L and margin funding)
        net_value = float(res[definitions.bitfinex_net_value]) # USD actual value after discounts
        # The minimum net value to maintain in your trading wallet, under which all of your positions are fully liquidated
        required_margin = float(res[definitions.bitfinex_required_margin])
        # Your tradable balance in USD (the maximum size you can open on leverage for each pair)
        tradable_balance = {}
        for margin_limits in res[definitions.bitfinex_margin_limits]:
            symbol = margin_limits[definitions.bitfinex_on_pair]
            tradable_balance[symbol] = float(margin_limits[definitions.bitfinex_tradable_balance])

        margin_balance = {
            definitions.leverage: leverage,
            definitions.net_value: net_value,
            definitions.required_margin: required_margin,
            definitions.tradable_balance: tradable_balance
        }

        return margin_balance

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