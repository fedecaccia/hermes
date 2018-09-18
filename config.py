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
	"orderbook_btcusd_bittrex":{
		description: btcusd,
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
	"orderbook_btcusd_exmo":{
		description: btcusd,
		source: exmo,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookExmoBTCUSD.csv",
	},
	"orderbook_btcusd_gatecoin":{
		description: btcusd,
		source: gatecoin,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGatecoinBTCUSD.csv",
	},
	"orderbook_btcusd_gdax":{
		description: btcusd,
		source: gdax,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGdaxBTCUSD.csv",
	},
	"orderbook_btcusd_gemini":{
		description: btcusd,
		source: gemini,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGeminiBTCUSD.csv",
	},
	"orderbook_btcusd_kraken":{
		description: btcusd,
		source: kraken,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookKrakenBTCUSD.csv",
	},
	"orderbook_btcusd_okex":{
		description: btcusd,
		source: okex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookOkexBTCUSD.csv",
	},
	"orderbook_btcusd_yobit":{
		description: btcusd,
		source: yobit,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookYobitBTCUSD.csv",
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
	"btcusd_bittrex":{
		symbol: btcusd,
		base: btc,
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
	"btcusd_exmo":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: exmo,
		account: trading,
	},
	"btcusd_gatecoin":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: gatecoin,
		account: trading,
	},
	"btcusd_gdax":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: gdax,
		account: trading,
	},
	"btcusd_gemini":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: gemini,
		account: trading,
	},
	"btcusd_kraken":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: kraken,
		account: trading,
	},
	"btcusd_okex":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: okex,
		account: trading,
	},
	"btcusd_yobit":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: yobit,
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
			"orderbook_btcusd_bittrex"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_1":{
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
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_2":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_exmo"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_3":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_gatecoin"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_4":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_gdax"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_5":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_gemini"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_6":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_7":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_8":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bitstamp",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_9":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_cex"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_10":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_exmo"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_11":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_gatecoin"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_12":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_gdax"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_13":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_gemini"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_14":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_15":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_16":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_bittrex",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_17":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_exmo"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_18":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_gatecoin"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_19":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_gdax"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_20":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_gemini"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_21":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_22":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_23":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_cex",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_24":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_exmo",
			"orderbook_btcusd_gatecoin"
		],
		signals: {
			"btcusd_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_25":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_exmo",
			"orderbook_btcusd_gdax"
		],
		signals: {
			"btcusd_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_26":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_exmo",
			"orderbook_btcusd_gemini"
		],
		signals: {
			"btcusd_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_27":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_exmo",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_28":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_exmo",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_29":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_exmo",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_30":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gatecoin",
			"orderbook_btcusd_gdax"
		],
		signals: {
			"btcusd_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_31":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gatecoin",
			"orderbook_btcusd_gemini"
		],
		signals: {
			"btcusd_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_32":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gatecoin",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_33":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gatecoin",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_34":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gatecoin",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_35":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gdax",
			"orderbook_btcusd_gemini"
		],
		signals: {
			"btcusd_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_36":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gdax",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_37":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gdax",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_38":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gdax",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_39":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gemini",
			"orderbook_btcusd_kraken"
		],
		signals: {
			"btcusd_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_40":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gemini",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_41":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_gemini",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_42":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_kraken",
			"orderbook_btcusd_okex"
		],
		signals: {
			"btcusd_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_43":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_kraken",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
		},
	},
	"arbitrage_44":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_btcusd_okex",
			"orderbook_btcusd_yobit"
		],
		signals: {
			"btcusd_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			period:30,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			limit_buy_pct:100,
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
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_1":{
		algorithms_array:["arbitrage_1"],
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
	"strategy_2":{
		algorithms_array:["arbitrage_2"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_3":{
		algorithms_array:["arbitrage_3"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_4":{
		algorithms_array:["arbitrage_4"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_5":{
		algorithms_array:["arbitrage_5"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_6":{
		algorithms_array:["arbitrage_6"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_7":{
		algorithms_array:["arbitrage_7"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_8":{
		algorithms_array:["arbitrage_8"],
		thresholds:{
			"btcusd_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_9":{
		algorithms_array:["arbitrage_9"],
		thresholds:{
			"btcusd_bittrex":{
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
	"strategy_10":{
		algorithms_array:["arbitrage_10"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_11":{
		algorithms_array:["arbitrage_11"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_12":{
		algorithms_array:["arbitrage_12"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_13":{
		algorithms_array:["arbitrage_13"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_14":{
		algorithms_array:["arbitrage_14"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_15":{
		algorithms_array:["arbitrage_15"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_16":{
		algorithms_array:["arbitrage_16"],
		thresholds:{
			"btcusd_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_17":{
		algorithms_array:["arbitrage_17"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_18":{
		algorithms_array:["arbitrage_18"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_19":{
		algorithms_array:["arbitrage_19"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_20":{
		algorithms_array:["arbitrage_20"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_21":{
		algorithms_array:["arbitrage_21"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_22":{
		algorithms_array:["arbitrage_22"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_23":{
		algorithms_array:["arbitrage_23"],
		thresholds:{
			"btcusd_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_24":{
		algorithms_array:["arbitrage_24"],
		thresholds:{
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_25":{
		algorithms_array:["arbitrage_25"],
		thresholds:{
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_26":{
		algorithms_array:["arbitrage_26"],
		thresholds:{
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_27":{
		algorithms_array:["arbitrage_27"],
		thresholds:{
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_28":{
		algorithms_array:["arbitrage_28"],
		thresholds:{
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_29":{
		algorithms_array:["arbitrage_29"],
		thresholds:{
			"btcusd_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_30":{
		algorithms_array:["arbitrage_30"],
		thresholds:{
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_31":{
		algorithms_array:["arbitrage_31"],
		thresholds:{
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_32":{
		algorithms_array:["arbitrage_32"],
		thresholds:{
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_33":{
		algorithms_array:["arbitrage_33"],
		thresholds:{
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_34":{
		algorithms_array:["arbitrage_34"],
		thresholds:{
			"btcusd_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_35":{
		algorithms_array:["arbitrage_35"],
		thresholds:{
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_36":{
		algorithms_array:["arbitrage_36"],
		thresholds:{
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_37":{
		algorithms_array:["arbitrage_37"],
		thresholds:{
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_38":{
		algorithms_array:["arbitrage_38"],
		thresholds:{
			"btcusd_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_39":{
		algorithms_array:["arbitrage_39"],
		thresholds:{
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_40":{
		algorithms_array:["arbitrage_40"],
		thresholds:{
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_41":{
		algorithms_array:["arbitrage_41"],
		thresholds:{
			"btcusd_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_42":{
		algorithms_array:["arbitrage_42"],
		thresholds:{
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_43":{
		algorithms_array:["arbitrage_43"],
		thresholds:{
			"btcusd_kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_44":{
		algorithms_array:["arbitrage_44"],
		thresholds:{
			"btcusd_okex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_yobit":{
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
	kraken:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	cex:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	gemini:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	bittrex:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	bitstamp:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	yobit:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	gdax:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	gatecoin:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	okex:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
	exmo:{
		margin:{
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
		},
		trading:{
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
		},
		funding:{
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
		},
	},
}
virtual_tickers = {
	btcusd:{
		last:6300
	},
	ethusd:{
		last:200
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
	bitfinex: "keys/bitfinex.key",
	bittrex: "keys/bittrex.key",
	binance: "keys/binance.key",
}


