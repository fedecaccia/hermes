from definitions import *


#######################################################
#                      DATA SECTION
#######################################################

# PAIR TRADING

# Data modules

data_elements = {
  "orderbook_batbtc_binance":{
    description: batbtc,
    source: binance,
    data_type: orderbook,
    timeframe: one_sec,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/orderbookbittrexETHBTC.csv"
    # db_file = "sqlite:///data/data.db"
    # mongo_port = ""
  },
  "orderbook_batbtc_bitfinex":{
    description: batbtc,
    source: bitfinex,
    data_type: orderbook,
    timeframe: one_sec,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/orderbookbinanceETHBTC.csv"
    # db_file = "sqlite:///data/data.db"
    # mongo_port = ""
  },
  "orderbook_neobtc_binance":{
    description: neobtc,
    source: binance,
    data_type: orderbook,
    timeframe: one_sec,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/orderbookbittrexETHBTC.csv"
    # db_file = "sqlite:///data/data.db"
    # mongo_port = ""
  },
  "orderbook_neobtc_bittrex":{
    description: neobtc,
    source: bittrex,
    data_type: orderbook,
    timeframe: one_sec,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/orderbookbinanceETHBTC.csv"
    # db_file = "sqlite:///data/data.db"
    # mongo_port = ""
  },
  "orderbook_adabtc_binance":{
    description: adabtc,
    source: binance,
    data_type: orderbook,
    timeframe: one_sec,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/orderbookbittrexETHBTC.csv"
    # db_file = "sqlite:///data/data.db"
    # mongo_port = ""
  },
  "orderbook_adabtc_bittrex":{
    description: adabtc,
    source: bittrex,
    data_type: orderbook,
    timeframe: one_sec,
    data_format: csv,
    header_format: cdm,
    file_name: "./sample/orderbookbinanceETHBTC.csv"
    # db_file = "sqlite:///data/data.db"
    # mongo_port = ""
  }
}

#######################################################
#                      ASSETS SECTION
#######################################################

assets_elements = {
  "batbtc_bitfinex":{
    symbol:batbtc,
    base:bat,
    quote:btc,
    exchange:bitfinex,
    account:trading
  },
  "batbtc_binance":{
    symbol:batbtc,
    base:bat,
    quote:btc,
    exchange:binance,
    account:trading
  },
  "neobtc_bittrex":{
    symbol:neobtc,
    base:neo,
    quote:btc,
    exchange:bittrex,
    account:trading
  },
  "neobtc_binance":{
    symbol:neobtc,
    base:neo,
    quote:btc,
    exchange:binance,
    account:trading
  },
  "adabtc_bittrex":{
    symbol:adabtc,
    base:ada,
    quote:btc,
    exchange:bittrex,
    account:trading
  },
  "adabtc_binance":{
    symbol:adabtc,
    base:ada,
    quote:btc,
    exchange:binance,
    account:trading
  }
}

#######################################################
#                  ALGORITHM SECTION
#######################################################

algorithms_elements = {
  "arbitrage_batbtc":{
    algorithm:statarb,
    data_modules_array:[
      "orderbook_batbtc_bitfinex",
      "orderbook_batbtc_binance"
      ],
    signals:{
      "batbtc_bitfinex":{
        long_signal:+1,
        short_signal:-1
      },
      "batbtc_binance":{
        long_signal:+1,
        short_signal:-1
      }
    },
    algo_params:{
      limit_buy_pct:100,
      limit_sell_pct:100,
      max_delay_in_data:2, # seconds
      usd_amount_to_trade:50, # 10, 15, full
      period:30, # amount of data points to compute mean
    }
  },
  "arbitrage_neobtc":{
    algorithm:statarb,
    data_modules_array:[
      "orderbook_neobtc_bittrex",
      "orderbook_neobtc_binance"
      ],
    signals:{
      "neobtc_bittrex":{
        long_signal:+1,
        short_signal:-1
      },
      "neobtc_binance":{
        long_signal:+1,
        short_signal:-1
      }
    },
    algo_params:{
      limit_buy_pct:100,
      limit_sell_pct:100,
      max_delay_in_data:2, # seconds
      usd_amount_to_trade:50, # 10, 15, full
      period:30, # amount of data points to compute mean
    }
  },
  "arbitrage_adabtc":{
    algorithm:statarb,
    data_modules_array:[
      "orderbook_adabtc_bittrex",
      "orderbook_adabtc_binance"
      ],
    signals:{
      "adabtc_bittrex":{
        long_signal:+1,
        short_signal:-1
      },
      "adabtc_binance":{
        long_signal:+1,
        short_signal:-1
      }
    },
    algo_params:{
      limit_buy_pct:100,
      limit_sell_pct:100,
      max_delay_in_data:2, # seconds
      usd_amount_to_trade:50, # 10, 15, full
      period:30, # amount of data points to compute mean
    }
  }
}

# Strategies

strategies_elements = {
  "arbitrage1":{
    algorithms_array:["arbitrage_batbtc"],
    thresholds:{
      "batbtc_bitfinex":{
        long_threshold:1,
        short_threshold:-1
      },
      "batbtc_binance":{
        long_threshold:1,
        short_threshold:-1
      }
    },
    order_type:limit
  },
  "arbitrage2":{
    algorithms_array:["arbitrage_neobtc"],
    thresholds:{
      "neobtc_bittrex":{
        long_threshold:1,
        short_threshold:-1
      },
      "neobtc_binance":{
        long_threshold:1,
        short_threshold:-1
      }
    },
    order_type:limit
  },
  "arbitrage3":{
    algorithms_array:["arbitrage_adabtc"],
    thresholds:{
      "adabtc_bittrex":{
        long_threshold:1,
        short_threshold:-1
      },
      "adabtc_binance":{
        long_threshold:1,
        short_threshold:-1
      }
    },
    order_type:limit
  }
}

# VIRTUAL ARBITRAGE BATBTC

# # Data modules

# data_elements = {
#   "orderbook_batbtc_binance":{
#     description: batbtc,
#     source: binance,
#     data_type: orderbook,
#     timeframe: one_sec,
#     data_format: csv,
#     header_format: cdm,
#     file_name: "./sample/orderbookbittrexETHBTC.csv"
#     # db_file = "sqlite:///data/data.db"
#     # mongo_port = ""
#   },
#   "orderbook_batbtc_bitfinex":{
#     description: batbtc,
#     source: bitfinex,
#     data_type: orderbook,
#     timeframe: one_sec,
#     data_format: csv,
#     header_format: cdm,
#     file_name: "./sample/orderbookbinanceETHBTC.csv"
#     # db_file = "sqlite:///data/data.db"
#     # mongo_port = ""
#   },
# }

# # Assets

# assets_elements = {
#   "batbtc_bitfinex":{
#     symbol:batbtc,
#     base:bat,
#     quote:btc,
#     exchange:bitfinex,
#     account:trading
#   },
#   "batbtc_binance":{
#     symbol:batbtc,
#     base:bat,
#     quote:btc,
#     exchange:binance,
#     account:trading
#   }
# }

# # Algorithms

# algorithms_elements = {
#   "virtual_arbitrage":{
#     algorithm:virtual_transfer,
#     data_modules_array:[
#       "orderbook_batbtc_bitfinex",
#       "orderbook_batbtc_binance"
#       ],
#     signals:{
#       "batbtc_bitfinex":{
#         long_signal:+1,
#         short_signal:-1
#       },
#       "batbtc_binance":{
#         long_signal:+1,
#         short_signal:-1
#       }
#     },
#     algo_params:{
#       limit_buy_pct:100,
#       limit_sell_pct:100,
#       max_delay_in_data:2, # seconds
#       usd_amount_to_trade:50 # 10, 15, full
#     }
#   }
# }

# # Strategies

# strategies_elements = {
#   "arbitrage":{
#     algorithms_array:["virtual_arbitrage"],
#     thresholds:{
#       "batbtc_bitfinex":{
#         long_threshold:1,
#         short_threshold:-1
#       },
#       "batbtc_binance":{
#         long_threshold:1,
#         short_threshold:-1
#       }
#     },
#     order_type:limit   
#   }
# }

# VIRTUAL ARBITRAGE ETHBTC

# # Data modules

# data_elements = {
#   "orderbook_ethbtc_bittrex":{
#     description: ethbtc,
#     source: bittrex,
#     data_type: orderbook,
#     timeframe: one_sec,
#     data_format: csv,
#     header_format: cdm,
#     file_name: "./sample/orderbookbittrexETHBTC.csv"
#     # db_file = "sqlite:///data/data.db"
#     # mongo_port = ""
#   },
#   "orderbook_ethbtc_binance":{
#     description: ethbtc,
#     source: binance,
#     data_type: orderbook,
#     timeframe: one_sec,
#     data_format: csv,
#     header_format: cdm,
#     file_name: "./sample/orderbookbinanceETHBTC.csv"
#     # db_file = "sqlite:///data/data.db"
#     # mongo_port = ""
#   },
# }

# # Assets

# assets_elements = {
#   "ethbtc_bittrex":{
#     symbol:ethbtc,
#     base:eth,
#     quote:btc,
#     exchange:bittrex,
#     account:trading
#   },
#   "ethbtc_binance":{
#     symbol:ethbtc,
#     base:eth,
#     quote:btc,
#     exchange:binance,
#     account:trading
#   }
# }

# # Algorithms

# algorithms_elements = {
#   "virtual_arbitrage":{
#     algorithm:virtual_transfer,
#     data_modules_array:[
#       "orderbook_ethbtc_bittrex",
#       "orderbook_ethbtc_binance"
#       ],
#     signals:{
#       "ethbtc_bittrex":{
#         long_signal:+1,
#         short_signal:-1
#       },
#       "ethbtc_binance":{
#         long_signal:+1,
#         short_signal:-1
#       }
#     },
#     algo_params:{
#       limit_buy_pct:100,
#       limit_sell_pct:100,
#       max_delay_in_data:2, # seconds
#       usd_amount_to_trade:50 # 10, 15, full
#     }
#   }
# }

# # Strategies

# strategies_elements = {
#   "arbitrage":{
#     algorithms_array:["virtual_arbitrage"],
#     thresholds:{
#       "ethbtc_bittrex":{
#         long_threshold:1,
#         short_threshold:-1
#       },
#       "ethbtc_binance":{
#         long_threshold:1,
#         short_threshold:-1
#       }
#     },
#     order_type:limit   
#   }
# }

# VOLUME

# # Data modules

# data_elements = {
#   "candles_ethbtc_bittrex":{
#     description: ethbtc,
#     source: bittrex,
#     data_type: candles,
#     timeframe: one_min,
#     since: None,
#     limit: 3,
#     data_format: csv,
#     header_format: cdm,
#     file_name: "./sample/candlesbittrexETHBTC.csv"
#     # db_file = "sqlite:///data/data.db"
#     # mongo_port = ""
#   }
# }

# # Assets

# assets_elements = {
#   "ethbtc_bittrex":{
#     symbol:ethbtc,
#     base:eth,
#     quote:btc,
#     exchange:bittrex,
#     account:trading
#   }
# }

# # Algorithms

# algorithms_elements = {
#   "vol":{
#     algorithm:volume,
#     data_modules_array:["candles_ethbtc_bittrex"],
#     signals:{
#       "ethbtc_bittrex":{
#         long_signal:+1,
#         short_signal:-1
#       }
#     },
#     algo_params:{
#       vol_growth:0.5,
#       ma_periods:5,
#       limit_buy_pct: 101,
#       limit_sell_pct:99,
#       usd_amount_to_trade:50 # 10, 15, full
#     }
#   }
# }

# # Strategies

# strategies_elements = {
#   "test":{
#     algorithms_array:["vol"],
#     thresholds:{
#       "ethbtc_bittrex":{
#         long_threshold:1,
#         short_threshold:-1
#       }
#     },
#     order_type:limit    
#   }
# }

# Trading mode

trading_mode = paper # paper # backtest
n_request_threads = 2


#######################################################
#                  BACKTEST SECTION
#######################################################

time_step = one_min

virtual_portfolio = {
  bittrex:{
    trading:{
      eth:{
        free:100,
        used:0,
        total:100
      },
      btc:{
        free:10,
        used:0,
        total:10
      },
      neo:{
        free:1000,
        used:0,
        total:1000
      },
      ada:{
        free:1000,
        used:0,
        total:1000
      }
    }
  },
  binance:{
    trading:{
      eth:{
        free:100,
        used:0,
        total:100
      },
      btc:{
        free:10,
        used:0,
        total:10
      },
      bat:{
        free:1000,
        used:0,
        total:1000
      },
      neo:{
        free:1000,
        used:0,
        total:1000
      },
      ada:{
        free:1000,
        used:0,
        total:1000
      }
    }
  },
  bitfinex:{
    trading:{
      eth:{
        free:100,
        used:0,
        total:100
      },
      btc:{
        free:10,
        used:0,
        total:10
      },
      bat:{
        free:1000,
        used:0,
        total:1000,
      },
      neo:{
        free:1000,
        used:0,
        total:1000
      },
      ada:{
        free:1000,
        used:0,
        total:1000
      }
    }
  }
}

virtual_tickers = {
  btcusd:{
    last:6500
  },
  ethusd:{
    last:300
  },
  ethbtc:{
    last:300./6500
  }
}


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

# data
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

  # algorithms_elements = [
#   # {
#   #   algorithm_id: 0,
#   #   algorithm: crossing_sma,
#   #   parameters: {
#   #     ema_low: 10,
#   #     ema_fast: 20,
#   #     trade_amount_coin: usd,
#   #     trade_amount_value: 100
#   #   },
#   #   data_modules_array: [0],
#   #   signals:{
#   #     ethbtc:{      
#   #       bittrex:{
#           # trading:{
#           #   long_signal:+1,
#           #   short_signal:-1
#           # }
#   #       }
#   #     }
#   #   }
#   # },
#   {
#     algorithm_id: 1,
#     algorithm: volume,
#     parameters: {
#       vol_growth:0.5,
#       ma_periods:5,
#       trade_amount_coin: usd,
#       trade_amount_value: 200
#     },
#     data_modules_array: [0],
#     signals:{
#       ethbtc:{
#         bittrex:{
#           trading:{
#             long_signal:+1,
#             short_signal:-1
#           }
#         }
#       }
#     }
#   }#,
#   # {
#   #   algorithm_id: 2,
#   #   algorithm: twitter_analysis,
#   #   parameters: {
#   #     tweets_growth:0.3,
#   #     trade_amount_coin: usd,
#   #     trade_amount_value: 200
#   #   },
#   #   data_modules_array: [3],
#   #   signals:{
#   #     ethbtc:{      
#   #       bittrex:{
#           # trading:{
#           #   long_signal:+1,
#           #   short_signal:-1
#           # }
#   #       }
#   #     }
#   #   }
#   # },
#   # {
#   #   algorithm_id: 3,
#   #   algorithm: virtual_transfer,
#   #   parameters: {
#   #     min_profit:0.1,
#   #     trade_amount_coin: usd,
#   #     trade_amount_value: 100
#   #   },
#   #   data_modules_array: [1,2],
#   #   signals:{
#   #     ethbtc:{      
#   #       bittrex:{
#           # trading:{
#           #   long_signal:+1,
#           #   short_signal:-1
#           # }
#   #       }
#   #     },
#   #     ethbtc:{      
#   #       binance:{
#           # trading:{
#           #   long_signal:+1,
#           #   short_signal:-1
#           # }
#   #       }
#   #     }
#   #   }
#   # }
# ]

# # Strategies definition

# # strategies_elements = [
# #   {
# #     strategy_id: 0,
# #     algorithms_array: [0, 1, 3],
# #     threshold: 3
# #   },
# #   {
# #     strategy_id: 1,
# #     algorithms_array: [2],
# #     thresholds:{
# #       bittrex:{      
# #         ethbtc:{
# #           long_threshold:+1,
# #           short_threshold:-1
# #         }
# #       },
# #       binance:{      
# #         ethbtc:{
# #           long_threshold:+1,
# #           short_threshold:-1
# #         }
# #       }
# #     }
# #   }
# # ]
# strategies_elements = [
#   {
#     strategy_id: 0,
#     algorithms_array: [1],
#     thresholds:{
#       ethbtc:{   
#         bittrex:{
#           long_threshold:+1,
#           short_threshold:-1
#         }
#       }
#     },
#     assets:{
#       ethbtc:{
#         base:eth,
#         quote:btc,
#         usd_trade_amount:100,
#         order_type:market
#       }
#     }
#   }
# ]
