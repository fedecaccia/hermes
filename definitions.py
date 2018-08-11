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
tweets_growth = "tweets_growth"
min_profit = "min_profit"
trade_amount_coin = "trade_amount_coin"
trade_amount_value = "trade_amount_value"

# Account types

trading = "trading"
funding = "funding"
margin_trading = "margin_trading"

# Margin trading specifics

margin = "margin"

# Algorithm valuations definition

threshold = "threshold"
valuation = "valuation"
passed = "passed"
reprobed = "reprobed"

# Useful definitions

data_id = "data_id"
description = "description"
source = "source"
algorithm = "algorithm"
algorithms_array = "algorithms_array"
parameters = "parameters"
data_modules_array = "data_modules_array"
strategy_id = "strategy_id"
values = "values"
filters = "filters"