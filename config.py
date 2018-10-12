from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_xtzbtc_gateio":{
		description: xtzbtc,
		source: gateio,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGateioXTZBTC.csv",
	},
	"orderbook_xtzbtc_hitbtc":{
		description: xtzbtc,
		source: hitbtc,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookHitbtcXTZBTC.csv",
	},
}

#######################################################
#                  ASSETS SECTION
#######################################################

assets_elements = {
	"xtzbtc_gateio":{
		symbol: xtzbtc,
		base: xtz,
		quote: btc,
		exchange: gateio,
		account: trading,
	},
	"xtzbtc_hitbtc":{
		symbol: xtzbtc,
		base: xtz,
		quote: btc,
		exchange: hitbtc,
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
			"orderbook_xtzbtc_gateio",
			"orderbook_xtzbtc_hitbtc"
		],
		signals: {
			"xtzbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"xtzbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			min_usd_profit:0.1,
			period:30,
			usd_amount_to_trade:100,
			limit_buy_pct:100,
			limit_sell_pct:100,
			max_delay_in_data:5,
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
			"xtzbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"xtzbtc_hitbtc":{
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

trading_mode = paper
n_request_threads = 2

#######################################################
#                  BACKTEST SECTION
#######################################################

time_step = one_sec
virtual_portfolio = {
	hitbtc:{
		margin:{
			xtz:{
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
			xtz:{
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
			xtz:{
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
	gateio:{
		margin:{
			xtz:{
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
			xtz:{
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
			xtz:{
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
	bitfinex: "keys/bitfinex.key",
	bittrex: "keys/bittrex.key",
	binance: "keys/binance.key",
}


