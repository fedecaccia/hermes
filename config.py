from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_ethbtc_bittrex":{
		description: ethbtc,
		source: bittrex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "sample/orderbookbinanceETHBTC.csv",
	},
	"orderbook_ethbtc_binance":{
		description: ethbtc,
		source: binance,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "sample/orderbookbittrexETHBTC.csv",
	},
}

#######################################################
#                  ASSETS SECTION
#######################################################

assets_elements = {
	"ethbtc_bittrex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: bittrex,
		account: trading,
	},
	"ethbtc_binance":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: binance,
		account: trading,
	},
}

#######################################################
#                  ALGORITHMS SECTION
#######################################################

algorithms_elements = {
	"arbitrage_0":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_binance"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			max_delay_in_data:2,
			limit_sell_pct:100,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
			period:30,
		},
	},
}

#######################################################
#                  STRATEGIES SECTION
#######################################################

strategies_elements = {
	"strategy_0":{
		algorithms_array:["arbitrage_0"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
}

#######################################################
#                  GENERAL SETTINGS
#######################################################

trading_mode = backtest
n_request_threads = 2

#######################################################
#                  BACKTEST SECTION
#######################################################

time_step = one_min
virtual_portfolio = {
	bittrex:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		trading:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		funding:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
	},
	binance:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		trading:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		funding:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
	},
}
virtual_tickers = {
	btcusd:{
		last:6300
	},
	ethbtc:{
		last:0.031
	},
	ethusd:{
		last:200
	},
}


#######################################################
#                  PAPER TRADING SECTION
#######################################################



#######################################################
#                  REAL TRADING SECTION
#######################################################

api_keys_files = {
	bittrex: "keys/bittrex.key",
	bitfinex: "keys/bitfinex.key",
	binance: "keys/binance.key",
}


