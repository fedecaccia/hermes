import definitions

import ccxt
import time

import pandas as pd

from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import RequestTimeout
from urllib.request import HTTPError
from abc import ABC, abstractmethod


class Exchange(ABC):

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

        self.exchange = exchange
        self._initialize_client(exchange, keys)
        self._initialize_fees()
        self.last_request_time = 0

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

        trading_balances = None
        self._wait_rate_limit()
        try:
            res = self.client.fetch_balance()
        except DDoSProtection:
            print("WARNING: DDOS Protection. ERROR rate limit in exchange: "+self.exchange)
        except RequestTimeout:
            print("WARNING: RequestTimeout. ERROR rate limit in exchange: "+self.exchange)
        except HTTPError:
            print("WARNING: HTTPError. Bad Gateway for url in exchange: "+self.exchange)
        else:
            trading_balances = {}
            for key, values in res.items():
                if key not in ["total", "free", "used", "info"]:
                    trading_balances[key] = values
        finally:
            self.last_request_time = time.time()

        return trading_balances

    def get_margin_balance(self):

        """
        + Description: Get margin trading balances and limits. (dummy)
        + Input:
        -
        + Output:
        - margin_balance: Dictionary containing main margin balance parameters.

        """
        
        margin_balance = {
            definitions.leverage: 0,
            definitions.net_value: 0,
            definitions.required_margin: 0,
            definitions.tradable_balance: 0
        }

        return margin_balance

    def get_tickers_in_serial(self):

        """
        + Description: Get all tickers from exchange client. Not receiving barrier.
        + Input:
        -
        + Output:
        - tickers: Dictionary of all tickers.
        """
        
        tickers = None
        self._wait_rate_limit()
        try:
            tickers =  self.client.fetch_tickers()
        except DDoSProtection:
            print("WARNING: DDOS Protection. ERROR rate limit in exchange: "+self.exchange)
        except RequestTimeout:
            print("WARNING: RequestTimeout. ERROR rate limit in exchange: "+self.exchange)
        except HTTPError:
            print("WARNING: HTTPError. Bad Gateway for url in exchange: "+self.exchange)
        finally:
            self.last_request_time = time.time()

        return tickers

    def get_tickers(self, barrier):

        """
        + Description: Get all tickers from exchange client synchronized with other threads.
        + Input:
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        + Output:
        - tickers: Dictionary of all tickers.
        """
        
        tickers = None
        self.synchronize(barrier)
        try:
            tickers = self.client.fetch_tickers()
        except DDoSProtection:
            print("WARNING: DDOS Protection. ERROR rate limit in exchange: "+self.exchange)
        except RequestTimeout:
            print("WARNING: RequestTimeout. ERROR rate limit in exchange: "+self.exchange)
        except HTTPError:
            print("WARNING: HTTPError. Bad Gateway for url in exchange: "+self.exchange)
        finally:
            self.last_request_time = time.time()

        return tickers

    def get_orderbook(self, ticker, barrier):
        
        """
        + Description: query to request orderboooks for a given ticker.
        + Input:
        - ticker: string
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        + Output:
        - orderbook: Array of dictionaries.
        """

        orderbook = None
        self.synchronize(barrier)
        try:
            orderbook = self.client.fetchOrderBook(ticker)
        except DDoSProtection:
            print("WARNING: DDOS Protection. ERROR rate limit in exchange: "+self.exchange)
        except RequestTimeout:
            print("WARNING: RequestTimeout. ERROR rate limit in exchange: "+self.exchange)
        except HTTPError:
            print("WARNING: HTTPError. Bad Gateway for url in exchange: "+self.exchange)
        finally:
            self.last_request_time = time.time()

        return orderbook

    def get_candles(self, ticker, timeframe, since, limit, barrier):

        """
        + Description: query to request candles for a given ticker.
        + Input:
        - ticker: string
        - timeframe: string        
        - since: seconds passed since the first required candle
        - limit: maximum amount of candles
        - barrier: Barrier created to synchronize the threads that are working specifically now.
        + Output:
        - candles: Array of dictionaries.
        """
        
        candles = None
        self.synchronize(barrier)
        try:
            candles = self.client.fetch_ohlcv(ticker, timeframe, since, limit)
        except DDoSProtection:            
            print("WARNING: DDOS Protection. ERROR rate limit in exchange: "+self.exchange)
        except RequestTimeout:
            print("WARNING: RequestTimeout. ERROR rate limit in exchange: "+self.exchange)
        except HTTPError:
            print("WARNING: HTTPError. Bad Gateway for url in exchange: "+self.exchange)
        finally:
            self.last_request_time = time.time()
            
        return candles

    def synchronize(self, barrier):
        self._wait_rate_limit()
        barrier.wait()

    def _wait_rate_limit(self):
        while (time.time() - self.last_request_time)<self.client.rateLimit/1000:
            pass


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
        
        self._wait_rate_limit()
        try:
            res = self.client.private_post_margin_infos()[0]
        except DDoSProtection:            
            print("WARNING: DDOS Protection. ERROR rate limit in exchange: "+self.exchange)
        except RequestTimeout:
            print("WARNING: RequestTimeout. ERROR rate limit in exchange: "+self.exchange)
        except HTTPError:
            print("WARNING: HTTPError. Bad Gateway for url in exchange: "+self.exchange)
        
        finally:
            self.last_request_time = time.time()        
        
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

    def _wait_rate_limit(self):
        # candles: 30 req/min
        # orderbooks: 60 req/min
        # others: see https://docs.bitfinex.com/v1/reference
        # their actual rate limit is significantly more strict than documented!
        # 'rateLimit': 3000, # once every 3 seconds, 20 times per minute – will work
        rateLimit = 3000
        while (time.time() - self.last_request_time)<rateLimit/1000:
            pass

class Bitstamp(Exchange):

    """
    Bitstamp: client interface to connect with Bittrex.
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


class Cex(Exchange):

    """
    Cex: client interface to connect with Cex.
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


class Coinex(Exchange):

    """
    Coinex: client interface to connect with Coinex.
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


class Exmo(Exchange):

    """
    Exmo: client interface to connect with Exmo.
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


class Gatecoin(Exchange):

    """
    Gatecoin: client interface to connect with Gatecoin.
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


class Gateio(Exchange):

    """
    Gateio: client interface to connect with Gateio.
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


class Gdax(Exchange):

    """
    Gdax: client interface to connect with Gdax.
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


class Gemini(Exchange):

    """
    Gemini: client interface to connect with Gemini.
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


class Hitbtc(Exchange):

    """
    Hitbtc: client interface to connect with Hitbtc.
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


class Huobipro(Exchange):

    """
    Huobipro: client interface to connect with Huobipro.
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


class Kraken(Exchange):

    """
    Kraken: client interface to connect with Kraken.
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


class Kucoin(Exchange):

    """
    Kucoin: client interface to connect with Kucoin.
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


class Okex(Exchange):

    """
    Okex: client interface to connect with Okex.
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


class Poloniex(Exchange):

    """
    Poloniex: client interface to connect with Poloniex.
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


class Yobit(Exchange):

    """
    Yobit: client interface to connect with Yobit.
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