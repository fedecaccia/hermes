from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_ethbtc_yobit":{
		description: ethbtc,
		source: yobit,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "xxx",
	},
	"orderbook_ethbtc_huobipro":{
		description: ethbtc,
		source: huobipro,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "xxx",
	},
	"orderbook_zecbtc_yobit":{
		description: zecbtc,
		source: yobit,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "xxx",
	},
	"orderbook_zecbtc_bitfinex":{
		description: zecbtc,
		source: bitfinex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "xxx",
	},
	"orderbook_xrpusd_kraken":{
		description: xrpusd,
		source: kraken,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "xxx",
	},
	"orderbook_xrpusd_bittrex":{
		description: xrpusd,
		source: bittrex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "xxx",
	},
}

#######################################################
#                  ASSETS SECTION
#######################################################

assets_elements = {
	"ethbtc_yobit":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: yobit,
		account: trading,
	},
	"ethbtc_huobipro":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: huobipro,
		account: trading,
	},
	"zecbtc_yobit":{
		symbol: zecbtc,
		base: zec,
		quote: btc,
		exchange: yobit,
		account: trading,
	},
	"zecbtc_bitfinex":{
		symbol: zecbtc,
		base: zec,
		quote: btc,
		exchange: bitfinex,
		account: trading,
	},
	"xrpusd_kraken":{
		symbol: xrpusd,
		base: xrp,
		quote: usd,
		exchange: kraken,
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
			"orderbook_ethbtc_yobit",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			min_usd_profit:0.1,
			usd_amount_to_trade:50,
			max_delay_in_data:5,
			period:1,
			limit_sell_pct:100,
		},
	},
	"arbitrage_1":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_zecbtc_yobit",
			"orderbook_zecbtc_bitfinex"
		],
		signals: {
			"zecbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
			"zecbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			min_usd_profit:0.1,
			usd_amount_to_trade:50,
			max_delay_in_data:5,
			period:1,
			limit_sell_pct:100,
		},
	},
	"arbitrage_2":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_xrpusd_kraken",
			"orderbook_xrpusd_bittrex"
		],
		signals: {
			"xrpusd_kraken":{
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
			min_usd_profit:0.1,
			usd_amount_to_trade:50,
			max_delay_in_data:5,
			period:1,
			limit_sell_pct:100,
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
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:market
	},
	"strategy_1":{
		algorithms_array:["arbitrage_1"],
		thresholds:{
			"zecbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			},
			"zecbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:market
	},
	"strategy_2":{
		algorithms_array:["arbitrage_2"],
		thresholds:{
			"xrpusd_kraken":{
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
	huobipro:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
	bittrex:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
	yobit:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
	bitfinex:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
	kraken:{
		margin:{
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
			eth:{
				free:9999999,
				used:0,
				total:9999999
			},
			zec:{
				free:9999999,
				used:0,
				total:9999999
			},
			btc:{
				free:9999999,
				used:0,
				total:9999999
			},
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
	huobipro: "keys/huobi.key",
	bittrex: "keys/bittrex.key",
	yobit: "keys/yobit.key",
	bitstamp: "keys/bitstamp.key",
	bitfinex: "keys/bitfinex.key",
	kraken: "keys/kraken.key",
}
uid_files = {
	bitstamp: "uid/bitstamp.uid",
}


