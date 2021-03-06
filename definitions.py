# Trading mode

backtest = "backtest"
paper = "paper"
real = "real"

# Exchanges definition

binance = "binance"
bitfinex = "bitfinex"
bitstamp = "bitstamp"
bittrex = "bittrex"
cex = "cex"
coinex = "coinex"
exmo = "exmo"
gatecoin = "gatecoin"
gateio = "gateio"
gdax = "gdax"
gemini = "gemini"
hitbtc = "hitbtc"
huobipro = "huobipro"
kraken = "kraken"
kucoin = "kucoin"
okex = "okex"
poloniex = "poloniex"
yobit = "yobit"

exchange = "exchange"
all_exchanges = [
    binance,
    bitfinex,    
    bitstamp,
    bittrex,
    cex,
    coinex,
    exmo,
    gatecoin,
    gateio,
    gdax,
    gemini,
    hitbtc,
    huobipro,
    kraken,
    kucoin,
    okex,
    poloniex,
    yobit
]

# Other sources definition

twitter = "twitter"

# Tickers definition

btcusd = "BTC/USD"
ethusd = "ETH/USD"
ethusdt = "ETH/USDT"
ethbtc = "ETH/BTC"
batbtc = "BAT/BTC"
neobtc = "NEO/BTC"
adabtc = "ADA/BTC"
sntbtc = "SNT/BTC"
trxbtc = "TRX/BTC"
xtzbtc = "XTZ/BTC"
xrpusd = "XRP/USD"
zecbtc = "ZEC/BTC"
all_tickers = [
    btcusd,
    ethusd,
    ethusdt,
    ethbtc,
    batbtc,
    neobtc,
    adabtc,
    sntbtc,
    trxbtc,
    xtzbtc,
    xrpusd,
    zecbtc
]

# Coins definition

usd = "USD"
usdt = "USDT"
eur = "EUR"
btc = "BTC"
eth = "ETH"
bat = "BAT"
neo = "NEO"
ada = "ADA"
snt = "SNT"
trx = "TRX"
xtz = "XTZ"
xrp = "XRP"
zec = "ZEC"
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

crossing_sma = "crossing_sma"
crossing_ema = "crossing_ema"
volume = "volume"
virtual_transfer = "virtual_transfer"
statarb = "statarb"
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
min_usd_profit = "min_usd_profit"

# Account types

account = "account"
trading = "trading"
funding = "funding"
margin_trading = "margin"

# Algorithm valuations definition

thresholds = "thresholds"
long_threshold = "long_threshold"
short_threshold = "short_threshold"
signal = "signal"
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
full = "full"
last = "last"

# Fees

fee = "fee"
fees = "fees"
taker = "taker"
maker = "maker"

# Balances

free = "free"
used = "used"
total = "total"
leverage = "leverage"
net_value = "net_value"
required_margin = "required_margin"
margin_limits = "margin_limits"
on_pair = "on_pair"
tradable_balance = "tradable_balance"

# Candles

open_ = "open"
high = "high"
low = "low"
close = "close"
volume = "volume"

# Orders 

order_id = "id"
info = "info"
filled = "filled"
status = "status"
opened = "open"
closed = "closed"
canceled = "canceled"
closed = "closed"
average = "average"
price = "price"
rate = "rate"

# Bitfinex margin trading definitions

bitfinex_leverage = "leverage"
bitfinex_net_value = "net_value"
bitfinex_required_margin = "required_margin"
bitfinex_margin_limits = "margin_limits"
bitfinex_on_pair = "on_pair"
bitfinex_tradable_balance = "tradable_balance"

# Algorithms

max_delay_in_data = "max_delay_in_data"
period = "period"

# Positions

short_position = "short_position"
long_position = "long_position"

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
barrier = "barrier"
uid = "uid"
order_pile = "order_pile"
order_type = "type"

# trade signals to strategy
strategy_abort = "abort"
strategy_success = "success"
strategy_wait = "wait"