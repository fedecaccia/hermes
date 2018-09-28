from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_ethbtc_binance":{
		description: ethbtc,
		source: binance,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBinanceETHBTC.csv",
	},
	"orderbook_ethbtc_bitfinex":{
		description: ethbtc,
		source: bitfinex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBitfinexETHBTC.csv",
	},
}

#######################################################
#                  ASSETS SECTION
#######################################################

assets_elements = {
	"ethbtc_binance":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: binance,
		account: trading,
	},
	"ethbtc_bitfinex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: bitfinex,
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
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_bitfinex"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			period:30,
			max_delay_in_data:2,
			limit_buy_pct:100,
			limit_sell_pct:100,
			usd_amount_to_trade:50,
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
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_bitfinex":{
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

time_step = one_sec
virtual_portfolio = {
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
	bitfinex:{
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
	binance: "keys/binance.key",
	bittrex: "keys/bittrex.key",
	bitfinex: "keys/bitfinex.key",
}


