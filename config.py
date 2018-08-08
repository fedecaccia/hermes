from definitions import *


#######################################################
#                  ALGORITHM SECTION
#######################################################

# Data modules

data_elements = [
  {
    data_id: 0,
    description: ethbtc,
    source: bittrex,
    data_type: candles,
    data_format: csv,
    header_format: cdm,
    file_name: "./data/candlesbittrexETHBTC.csv"
  },
  {
    data_id: 1,
    description: ethbtc,
    source: bittrex,
    data_type: orderbook,
    data_format: csv,
    header_format: cdm,
    file_name: "./data/orderbookbittrexETHBTC.csv"
  },
  {
    data_id: 2,
    description: ethbtc,
    source: binance,
    data_type: orderbook,
    data_format: csv,
    header_format: cdm,
    file_name: "./data/orderbookbinanceETHBTC.csv"
  },
  {
    data_id: 3,
    description: tweets_count,
    source: twitter,
    data_type: tweets_histogram,
    data_format: csv,
    header_format: tdm,
    file_name: "./data/tweetsBTC.csv"
  }
]

# Algorithms

algorithms_elements = [
  {
    algorithm: crossing_ma,
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
    algorithm: twitter_analysis,
    parameters: {
      tweets_growth:0.3,
      trade_amount_coin: usd,
      trade_amount_value: 200
    },
    data_modules_array: [3]
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

strategies_elements = [
  {
    strategy_id: 0,
    algorithms_array: [crossing_ma, volume, twitter_analysis]
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




#######################################################
#                 PAPER TRADING SECTION
#######################################################




#######################################################
#                 REAL TRADING SECTION
#######################################################

api_keys_files = {
    binance: "./keys/binance.key",
    bitfinex: "./keys/bitfinex.key",
    bittrex: "./keys/bittrex.key"
}