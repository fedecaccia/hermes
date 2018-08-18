# Trading mode

backtest = "backtest"
paper = "paper"
real = "real"

# Exchanges definition

bittrex = "bittrex"
bitfinex = "bitfinex"
binance = "binance"
kucoin = "kucoin"
okex = "okex"
poloniex = "poloniex"
exchange = "exchange"
all_exchanges = [bittrex, bitfinex, binance, kucoin, okex, poloniex]

# Other sources definition

twitter = "twitter"

# Tickers definition

btcusd = "BTC/USD"
ethusd = "ETH/USD"
ethbtc = "ETH/BTC"
all_tickers = [btcusd, ethusd, ethbtc]

# Coins definition

usd = "USD"
eur = "EUR"
btc = "BTC"
eth = "ETH"
asset_id = "asset_id"

# Other description definitions

counter = "counter"

# Twitter filters

bitcoin = "bitcoin"
ethereum = "ethereum"
blockchain = "blockchain"

# Data types definition

data_type = "datatype"
orderbook = "orderbook"
candles = "candles"
ticker = "ticker"
tickers = "tickers"
tweets_count = "tweets_count"

# Timeframes definition

one_sec = "1s"
one_min = "1m"
five_min = "5m"
thirty_min = "30m"
one_hour = "1h"
four_hour = "4h"
six_hour = "6h"
one_day = "1d"
timeframe = "timeframe"
since = "since"
limit = "limit"

# Backtest data format definition

data_format = "data_format"
csv = "csv"
sql = "sql"
nosql = "nosql"

# Algorithms definition

crossing_ma = "crossing_ma"
crossing_ema = "crossing_ema"
volume = "volume"
virtual_transfer = "virtual_transfer"
twitter_analysis = "twitter_analysis"

# Backtest data format

header_format = "header_format"
cdm = "crypto data monitor"
tdm = "twitter data monitor"

# Backtest file name

file_name = "file_name"
db_path = "db_path"
table_name = "table_name"
mongo_port = "mongo_port"

# Specific algorithm definitions

ema_low = "ema_low"
ema_fast = "ema_fast"
vol_growth = "vol_growth"
ma_periods = "ma_periods"
tweets_growth = "tweets_growth"
min_profit = "min_profit"
trade_amount_coin = "trade_amount_coin"
trade_amount_value = "trade_amount_value"

# Account types

account = "account"
trading = "trading"
funding = "funding"
margin_trading = "margin_trading"

# Algorithm valuations definition

thresholds = "thresholds"
long_threshold = "long_threshold"
short_threshold = "short_threshold"
signals = "signals"
long_signal = "long_signal"
short_signal = "short_signal"

# Orders

buy = "buy"
sell = "sell"
order_type = "order_type"
margin = "margin"
trading = "trading"
limit = "limit"
market = "market"
stop = "stop"
stop_limit = "stop_limit"
usd_amount_to_trade = "usd_amount_to_trade"
limit_buy_pct = "limit_buy_pct"
limit_sell_pct = "limit_sell_pct"
side = "side"
params = "params"

# Useful definitions

data_id = "data_id"
description = "description"
source = "source"
algorithm = "algorithm"
algorithms_array = "algorithms_array"
data_modules_array = "data_modules_array"
algorithm_id = "algorithm_id"
strategy_id = "strategy_id"
values = "values"
filters = "filters"
assets = "assets"
base = "base"
quote = "quote"
symbol = "symbol"
algo_params = "algo_params"
order_params = "order_params"
amount = "amount"
function = "funtcion"