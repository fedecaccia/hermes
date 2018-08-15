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
    timeframe: one_min,
    since: None,
    limit: 10,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/candlesbittrexETHBTC.csv"
  }#,
  # {
  #   data_id: 1,
  #   description: ethbtc,
  #   source: bittrex,
  #   data_type: orderbook,
  #   data_format: csv,
  #   header_format: cdm,
  #   file_name: "./sample/orderbookbittrexETHBTC.csv"
  # },
  # {
  #   data_id: 2,
  #   description: ethbtc,
  #   source: binance,
  #   data_type: orderbook,
  #   data_format: csv,
  #   header_format: cdm,
  #   file_name: "./sample/orderbookbinanceETHBTC.csv"
  # },
  # {
  #   data_id: 3,
  #   description: counter,
  #   filters: [bitcoin, ethereum, blockchain],
  #   source: twitter,
  #   data_type: tweets_count,
  #   data_format: csv,
  #   header_format: tdm,
  #   file_name: "./sample/tweetsBTC.csv"
  # }
]

# Algorithms

algorithms_elements = [
  # {
  #   algorithm_id: 0,
  #   algorithm: crossing_ma,
  #   parameters: {
  #     ema_low: 10,
  #     ema_fast: 20,
  #     trade_amount_coin: usd,
  #     trade_amount_value: 100
  #   },
  #   data_modules_array: [0],
  #   signals:{
  #     ethbtc:{      
  #       bittrex:{
  #         long_signal:+1,
  #         short_signal:-1
  #       }
  #     }
  #   }
  # },
  {
    algorithm_id: 1,
    algorithm: volume,
    parameters: {
      vol_growth:0.5,
      ma_periods:5,
      trade_amount_coin: usd,
      trade_amount_value: 200
    },
    data_modules_array: [0],
    signals:{
      ethbtc:{
        bittrex:{
          long_signal:+1,
          short_signal:-1
        }
      }
    }
  }#,
  # {
  #   algorithm_id: 2,
  #   algorithm: twitter_analysis,
  #   parameters: {
  #     tweets_growth:0.3,
  #     trade_amount_coin: usd,
  #     trade_amount_value: 200
  #   },
  #   data_modules_array: [3],
  #   signals:{
  #     ethbtc:{      
  #       bittrex:{
  #         long_signal:+1,
  #         short_signal:-1
  #       }
  #     }
  #   }
  # },
  # {
  #   algorithm_id: 3,
  #   algorithm: virtual_transfer,
  #   parameters: {
  #     min_profit:0.1,
  #     trade_amount_coin: usd,
  #     trade_amount_value: 100
  #   },
  #   data_modules_array: [1,2],
  #   signals:{
  #     ethbtc:{      
  #       bittrex:{
  #         long_signal:+1,
  #         short_signal:-1
  #       }
  #     },
  #     ethbtc:{      
  #       binance:{
  #         long_signal:+1,
  #         short_signal:-1
  #       }
  #     }
  #   }
  # }
]

# Strategies definition

# strategies_elements = [
#   {
#     strategy_id: 0,
#     algorithms_array: [0, 1, 3],
#     threshold: 3
#   },
#   {
#     strategy_id: 1,
#     algorithms_array: [2],
#     thresholds:{
#       bittrex:{      
#         ethbtc:{
#           long_threshold:+1,
#           short_threshold:-1
#         }
#       },
#       binance:{      
#         ethbtc:{
#           long_threshold:+1,
#           short_threshold:-1
#         }
#       }
#     }
#   }
# ]
strategies_elements = [
  {
    strategy_id: 0,
    algorithms_array: [1],
    thresholds:{
      ethbtc:{   
        bittrex:{
          long_threshold:+1,
          short_threshold:-1
        }
      }
    }
  }
]

# Trading mode

trading_mode = backtest
n_request_threads = 2
max_delay_in_data = 0.5 # seconds


#######################################################
#                  BACKTEST SECTION
#######################################################

time_step = one_min


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