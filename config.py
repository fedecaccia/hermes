from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_btcusd_bitstamp":{
		description: btcusd,
		source: bitstamp,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBitstampBTCUSD.csv",
	},
	"orderbook_ethusd_bittrex":{
		description: ethusd,
		source: bittrex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBittrexpBTCUSD.csv",
	},
	"orderbook_btcusd_cex":{
		description: btcusd,
		source: cex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookCexBTCUSD.csv",
	},
	"orderbook_ethusd_exmo":{
		description: ethusd,
		source: exmo,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookExmoBTCUSD.csv",
	},
}

#######################################################
#                  ASSETS SECTION
#######################################################

assets_elements = {
	"btcusd_bitstamp":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: bitstamp,
		account: trading,
	},
	"ethusd_bittrex":{
		symbol: ethusd,
		base: eth,
		quote: usd,
		exchange: bittrex,
		account: trading,
	},
	"btcusd_cex":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: cex,
		account: trading,
	},
	"ethusd_exmo":{
		symbol: ethusd,
		base: eth,
		quote: usd,
		exchange: exmo,
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
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_cex"
		],
		signals: {
			"btcusd_bitstamp":{
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
	"arbitrage_1":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethusd_bittrex",
			"orderbook_ethusd_exmo"
		],
		signals: {
			"ethusd_bittrex":{
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
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_1":{
		algorithms_array:["arbitrage_1"],
		thresholds:{
			"ethusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethusd_exmo":{
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

trading_mode = backtestn_request_threads = 2

#######################################################
#                  BACKTEST SECTION
#######################################################

time_step = one_min
virtual_portfolio = {
	bitstamp:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			usd:{
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
			usd:{
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
			usd:{
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
	bittrex:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			usd:{
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
			usd:{
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
			usd:{
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
	exmo:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			usd:{
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
			usd:{
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
			usd:{
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
	cex:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			usd:{
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
			usd:{
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
			usd:{
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
	ethusd:{
		last:200
	},
	btcusd:{
		last:6300
	},
	ethbtc:{
		last:0.031
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


