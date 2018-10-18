from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_xrpusd_bitstamp":{
		description: xrpusd,
		source: bitstamp,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "orderbookBitstampXRPUSD.csv",
	},
	"orderbook_xrpusd_bittrex":{
		description: xrpusd,
		source: bittrex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "orderbookBittrexXRPUSD.csv",
	},
}

#######################################################
#                  ASSETS SECTION
#######################################################

assets_elements = {
	"xrpusd_bitstamp":{
		symbol: xrpusd,
		base: xrp,
		quote: usd,
		exchange: bitstamp,
		account: trading,
	},
	"xrpusd_bittrex":{
		symbol: xrpusd,
		base: xrp,
		quote: usd,
		exchange: bittrex,
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
			"orderbook_xrpusd_bitstamp",
			"orderbook_xrpusd_bittrex"
		],
		signals: {
			"xrpusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"xrpusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			limit_sell_pct:100,
			max_delay_in_data:5,
			usd_amount_to_trade:1000,
			min_usd_profit:0.1,
			period:1,
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
			"xrpusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"xrpusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:market
	},
}

#######################################################
#                  GENERAL SETTINGS
#######################################################

trading_mode = real
n_request_threads = 2

#######################################################
#                  BACKTEST SECTION
#######################################################

time_step = one_sec
virtual_portfolio = {
	bittrex:{
		margin:{
			usd:{
				free:9999999,
				used:0,
				total:9999999
			},
			xrp:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		trading:{
			usd:{
				free:9999999,
				used:0,
				total:9999999
			},
			xrp:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		funding:{
			usd:{
				free:9999999,
				used:0,
				total:9999999
			},
			xrp:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
	},
	bitstamp:{
		margin:{
			usd:{
				free:9999999,
				used:0,
				total:9999999
			},
			xrp:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		trading:{
			usd:{
				free:9999999,
				used:0,
				total:9999999
			},
			xrp:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
		funding:{
			usd:{
				free:9999999,
				used:0,
				total:9999999
			},
			xrp:{
				free:9999999,
				used:0,
				total:9999999
			},
		},
	},
}
virtual_tickers = {
	btcusd:{
		last:6500
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
	bitstamp: "keys/bitstamp.key",
}
uid_files = {
	bitstamp: "uid/bitstamp.uid",
}


