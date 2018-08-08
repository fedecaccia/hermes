from definitions import *


#######################################################
#                  ALGORITHM SECTION
#######################################################

# Data modules

data_modules = [
  {
    data_id: 0,
    description: btcusd,
    source: bittrex,
    datatype: candles
  },
  {
    data_id: 1,
    description: ethbtc,
    source: bittrex,
    datatype: orderbook
  },
  {
    data_id: 2,
    description: ethbtc,
    source: binance,
    datatype: orderbook
  }
]

# Algorithms

algorithms = [
  {
    algorithm: crossing_ema,
    parameters: {
      ema_low: 10,
      ema_fast: 20,
      trade_amount_coin: usd,
      trade_amount_value: 100
    },
    data_modules_array: [0]
  },
  {
    algorithm: volume,
    parameters: {
      vol_growth:0.5,
      trade_amount_coin: usd,
      trade_amount_value: 200
    },
    data_modules_array: [0]
  },
  {
    algorithm: virtual_transfer,
    parameters: {
      min_profit:0.1,
      trade_amount_coin: usd,
      trade_amount_value: 100
    },
    data_modules_array: [1,2]
  }
]

# Strategies definition

strategies = [
  {
    strategy_id: 0,
    algorithms_array: [crossing_ema, volume]
  },
  {
    strategy_id: 1,
    algorithms_array: [virtual_transfer]
  }
]

# Trading mode

trading_mode = backtest


#######################################################
#                  BACKTEST SECTION
#######################################################

# Backtest data format

backtest_datatype = csv

# Backtest data path

csv_dir = "./data/"
sql_dir = ""
mongo_port = ""

# Backtest data file names format

table_name_format = cdm

# Backtest data format

db_format = cdm

# Accounts


#######################################################
#                 PAPER TRADING SECTION
#######################################################




#######################################################
#                 REAL TRADING SECTION
#######################################################

