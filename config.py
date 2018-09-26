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
	"orderbook_ethbtc_bitstamp":{
		description: ethbtc,
		source: bitstamp,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBitstampETHBTC.csv",
	},
	"orderbook_ethbtc_bittrex":{
		description: ethbtc,
		source: bittrex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBittrexETHBTC.csv",
	},
	"orderbook_ethbtc_cex":{
		description: ethbtc,
		source: cex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookCexETHBTC.csv",
	},
	"orderbook_ethbtc_coinex":{
		description: ethbtc,
		source: coinex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookCoinexETHBTC.csv",
	},
	"orderbook_ethbtc_exmo":{
		description: ethbtc,
		source: exmo,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookExmoETHBTC.csv",
	},
	"orderbook_ethbtc_gatecoin":{
		description: ethbtc,
		source: gatecoin,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGatecoinETHBTC.csv",
	},
	"orderbook_ethbtc_gateio":{
		description: ethbtc,
		source: gateio,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGateioETHBTC.csv",
	},
	"orderbook_ethbtc_gdax":{
		description: ethbtc,
		source: gdax,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGdaxETHBTC.csv",
	},
	"orderbook_ethbtc_gemini":{
		description: ethbtc,
		source: gemini,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGeminiETHBTC.csv",
	},
	"orderbook_ethbtc_hitbtc":{
		description: ethbtc,
		source: hitbtc,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookHitbtcETHBTC.csv",
	},
	"orderbook_ethbtc_huobipro":{
		description: ethbtc,
		source: huobipro,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookHuobiproETHBTC.csv",
	},
	"orderbook_ethbtc_kraken":{
		description: ethbtc,
		source: kraken,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookKrakenETHBTC.csv",
	},
	"orderbook_ethbtc_kucoin":{
		description: ethbtc,
		source: kucoin,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookKucoinETHBTC.csv",
	},
	"orderbook_ethbtc_okex":{
		description: ethbtc,
		source: okex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookOkexETHBTC.csv",
	},
	"orderbook_ethbtc_poloniex":{
		description: ethbtc,
		source: poloniex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookPoloniexETHBTC.csv",
	},
	"orderbook_ethbtc_yobit":{
		description: ethbtc,
		source: yobit,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookYobitETHBTC.csv",
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
	"ethbtc_bitstamp":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: bitstamp,
		account: trading,
	},
	"ethbtc_bittrex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: bittrex,
		account: trading,
	},
	"ethbtc_cex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: cex,
		account: trading,
	},
	"ethbtc_coinex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: coinex,
		account: trading,
	},
	"ethbtc_exmo":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: exmo,
		account: trading,
	},
	"ethbtc_gatecoin":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: gatecoin,
		account: trading,
	},
	"ethbtc_gateio":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: gateio,
		account: trading,
	},
	"ethbtc_gdax":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: gdax,
		account: trading,
	},
	"ethbtc_gemini":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: gemini,
		account: trading,
	},
	"ethbtc_hitbtc":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: hitbtc,
		account: trading,
	},
	"ethbtc_huobipro":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: huobipro,
		account: trading,
	},
	"ethbtc_kraken":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: kraken,
		account: trading,
	},
	"ethbtc_kucoin":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: kucoin,
		account: trading,
	},
	"ethbtc_okex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: okex,
		account: trading,
	},
	"ethbtc_poloniex":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
		exchange: poloniex,
		account: trading,
	},
	"ethbtc_yobit":{
		symbol: ethbtc,
		base: eth,
		quote: btc,
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
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_1":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_bitstamp"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_2":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_bittrex"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_3":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_cex"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_4":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_coinex"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_5":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_exmo"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_6":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_7":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_8":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_9":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_10":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_11":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_12":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_13":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_14":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_15":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_16":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_binance",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_binance":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_17":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_bitstamp"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_18":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_bittrex"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_19":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_cex"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_20":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_coinex"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_21":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_exmo"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_22":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_23":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_24":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_25":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_26":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_27":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_28":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_29":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_30":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_31":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_32":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitfinex",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_bitfinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_33":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_bittrex"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_34":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_cex"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_35":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_coinex"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_36":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_exmo"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_37":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_38":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_39":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_40":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_41":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_42":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_43":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_44":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_45":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_46":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_47":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bitstamp",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_bitstamp":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_48":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_cex"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_49":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_coinex"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_50":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_exmo"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_51":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_52":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_53":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_54":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_55":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_56":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_57":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_58":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_59":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_60":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_61":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_bittrex",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_bittrex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_62":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_coinex"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_63":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_exmo"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_64":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_65":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_66":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_67":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_68":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_69":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_70":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_71":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_72":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_73":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_74":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_cex",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_cex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_75":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_exmo"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_76":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_77":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_78":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_79":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_80":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_81":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_82":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_83":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_84":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_85":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_86":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_coinex",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_coinex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_87":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_gatecoin"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_88":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_89":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_90":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_91":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_92":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_93":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_94":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_95":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_96":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_97":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_exmo",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_exmo":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_98":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_gateio"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_99":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_100":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_101":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_102":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_103":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_104":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_105":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_106":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_107":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gatecoin",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_gatecoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_108":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_gdax"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_109":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_110":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_111":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_112":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_113":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_114":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_115":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_116":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gateio",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_gateio":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_117":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_gemini"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_118":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_119":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_120":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_121":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_122":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_123":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_124":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gdax",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_gdax":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_125":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_hitbtc"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_126":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_127":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_128":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_129":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_130":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_131":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_gemini",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_gemini":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_132":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_hitbtc",
			"orderbook_ethbtc_huobipro"
		],
		signals: {
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_133":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_hitbtc",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_134":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_hitbtc",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_135":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_hitbtc",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_136":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_hitbtc",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_137":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_hitbtc",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_hitbtc":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_138":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_huobipro",
			"orderbook_ethbtc_kraken"
		],
		signals: {
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_139":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_huobipro",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_140":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_huobipro",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_141":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_huobipro",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_142":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_huobipro",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_huobipro":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_143":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kraken",
			"orderbook_ethbtc_kucoin"
		],
		signals: {
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_144":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kraken",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_145":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kraken",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_146":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kraken",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_kraken":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_147":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kucoin",
			"orderbook_ethbtc_okex"
		],
		signals: {
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_148":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kucoin",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_149":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_kucoin",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_kucoin":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_150":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_okex",
			"orderbook_ethbtc_poloniex"
		],
		signals: {
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_151":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_okex",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_okex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
			period:30,
		},
	},
	"arbitrage_152":{
		algorithm: statarb,
		data_modules_array: [
			"orderbook_ethbtc_poloniex",
			"orderbook_ethbtc_yobit"
		],
		signals: {
			"ethbtc_poloniex":{
				long_signal:1,
				short_signal:-1,
			},
			"ethbtc_yobit":{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_sell_pct:100,
			limit_buy_pct:100,
			max_delay_in_data:2,
			usd_amount_to_trade:50,
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
	"strategy_1":{
		algorithms_array:["arbitrage_1"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_2":{
		algorithms_array:["arbitrage_2"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_3":{
		algorithms_array:["arbitrage_3"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_4":{
		algorithms_array:["arbitrage_4"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_5":{
		algorithms_array:["arbitrage_5"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_6":{
		algorithms_array:["arbitrage_6"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_7":{
		algorithms_array:["arbitrage_7"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_8":{
		algorithms_array:["arbitrage_8"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_9":{
		algorithms_array:["arbitrage_9"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_10":{
		algorithms_array:["arbitrage_10"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_11":{
		algorithms_array:["arbitrage_11"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_12":{
		algorithms_array:["arbitrage_12"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_13":{
		algorithms_array:["arbitrage_13"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_14":{
		algorithms_array:["arbitrage_14"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_15":{
		algorithms_array:["arbitrage_15"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_16":{
		algorithms_array:["arbitrage_16"],
		thresholds:{
			"ethbtc_binance":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_17":{
		algorithms_array:["arbitrage_17"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_18":{
		algorithms_array:["arbitrage_18"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_19":{
		algorithms_array:["arbitrage_19"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_20":{
		algorithms_array:["arbitrage_20"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_21":{
		algorithms_array:["arbitrage_21"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_22":{
		algorithms_array:["arbitrage_22"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_23":{
		algorithms_array:["arbitrage_23"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_24":{
		algorithms_array:["arbitrage_24"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_25":{
		algorithms_array:["arbitrage_25"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_26":{
		algorithms_array:["arbitrage_26"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_27":{
		algorithms_array:["arbitrage_27"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_28":{
		algorithms_array:["arbitrage_28"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_29":{
		algorithms_array:["arbitrage_29"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_30":{
		algorithms_array:["arbitrage_30"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_31":{
		algorithms_array:["arbitrage_31"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_32":{
		algorithms_array:["arbitrage_32"],
		thresholds:{
			"ethbtc_bitfinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_33":{
		algorithms_array:["arbitrage_33"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_34":{
		algorithms_array:["arbitrage_34"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_35":{
		algorithms_array:["arbitrage_35"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_36":{
		algorithms_array:["arbitrage_36"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_37":{
		algorithms_array:["arbitrage_37"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_38":{
		algorithms_array:["arbitrage_38"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_39":{
		algorithms_array:["arbitrage_39"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_40":{
		algorithms_array:["arbitrage_40"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_41":{
		algorithms_array:["arbitrage_41"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_42":{
		algorithms_array:["arbitrage_42"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_43":{
		algorithms_array:["arbitrage_43"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_44":{
		algorithms_array:["arbitrage_44"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_45":{
		algorithms_array:["arbitrage_45"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_46":{
		algorithms_array:["arbitrage_46"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_47":{
		algorithms_array:["arbitrage_47"],
		thresholds:{
			"ethbtc_bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_48":{
		algorithms_array:["arbitrage_48"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_49":{
		algorithms_array:["arbitrage_49"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_50":{
		algorithms_array:["arbitrage_50"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_51":{
		algorithms_array:["arbitrage_51"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_52":{
		algorithms_array:["arbitrage_52"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_53":{
		algorithms_array:["arbitrage_53"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_54":{
		algorithms_array:["arbitrage_54"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_55":{
		algorithms_array:["arbitrage_55"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_56":{
		algorithms_array:["arbitrage_56"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_57":{
		algorithms_array:["arbitrage_57"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_58":{
		algorithms_array:["arbitrage_58"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_59":{
		algorithms_array:["arbitrage_59"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_60":{
		algorithms_array:["arbitrage_60"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_61":{
		algorithms_array:["arbitrage_61"],
		thresholds:{
			"ethbtc_bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_62":{
		algorithms_array:["arbitrage_62"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_63":{
		algorithms_array:["arbitrage_63"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_64":{
		algorithms_array:["arbitrage_64"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_65":{
		algorithms_array:["arbitrage_65"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_66":{
		algorithms_array:["arbitrage_66"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_67":{
		algorithms_array:["arbitrage_67"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_68":{
		algorithms_array:["arbitrage_68"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_69":{
		algorithms_array:["arbitrage_69"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_70":{
		algorithms_array:["arbitrage_70"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_71":{
		algorithms_array:["arbitrage_71"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_72":{
		algorithms_array:["arbitrage_72"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_73":{
		algorithms_array:["arbitrage_73"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_74":{
		algorithms_array:["arbitrage_74"],
		thresholds:{
			"ethbtc_cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_75":{
		algorithms_array:["arbitrage_75"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_76":{
		algorithms_array:["arbitrage_76"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_77":{
		algorithms_array:["arbitrage_77"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_78":{
		algorithms_array:["arbitrage_78"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_79":{
		algorithms_array:["arbitrage_79"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_80":{
		algorithms_array:["arbitrage_80"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_81":{
		algorithms_array:["arbitrage_81"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_82":{
		algorithms_array:["arbitrage_82"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_83":{
		algorithms_array:["arbitrage_83"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_84":{
		algorithms_array:["arbitrage_84"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_85":{
		algorithms_array:["arbitrage_85"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_86":{
		algorithms_array:["arbitrage_86"],
		thresholds:{
			"ethbtc_coinex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_87":{
		algorithms_array:["arbitrage_87"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_88":{
		algorithms_array:["arbitrage_88"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_89":{
		algorithms_array:["arbitrage_89"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_90":{
		algorithms_array:["arbitrage_90"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_91":{
		algorithms_array:["arbitrage_91"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_92":{
		algorithms_array:["arbitrage_92"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_93":{
		algorithms_array:["arbitrage_93"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_94":{
		algorithms_array:["arbitrage_94"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_95":{
		algorithms_array:["arbitrage_95"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_96":{
		algorithms_array:["arbitrage_96"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_97":{
		algorithms_array:["arbitrage_97"],
		thresholds:{
			"ethbtc_exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_98":{
		algorithms_array:["arbitrage_98"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_99":{
		algorithms_array:["arbitrage_99"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_100":{
		algorithms_array:["arbitrage_100"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_101":{
		algorithms_array:["arbitrage_101"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_102":{
		algorithms_array:["arbitrage_102"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_103":{
		algorithms_array:["arbitrage_103"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_104":{
		algorithms_array:["arbitrage_104"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_105":{
		algorithms_array:["arbitrage_105"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_106":{
		algorithms_array:["arbitrage_106"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_107":{
		algorithms_array:["arbitrage_107"],
		thresholds:{
			"ethbtc_gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_108":{
		algorithms_array:["arbitrage_108"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_109":{
		algorithms_array:["arbitrage_109"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_110":{
		algorithms_array:["arbitrage_110"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_111":{
		algorithms_array:["arbitrage_111"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_112":{
		algorithms_array:["arbitrage_112"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_113":{
		algorithms_array:["arbitrage_113"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_114":{
		algorithms_array:["arbitrage_114"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_115":{
		algorithms_array:["arbitrage_115"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_116":{
		algorithms_array:["arbitrage_116"],
		thresholds:{
			"ethbtc_gateio":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_117":{
		algorithms_array:["arbitrage_117"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_118":{
		algorithms_array:["arbitrage_118"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_119":{
		algorithms_array:["arbitrage_119"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_120":{
		algorithms_array:["arbitrage_120"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_121":{
		algorithms_array:["arbitrage_121"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_122":{
		algorithms_array:["arbitrage_122"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_123":{
		algorithms_array:["arbitrage_123"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_124":{
		algorithms_array:["arbitrage_124"],
		thresholds:{
			"ethbtc_gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_125":{
		algorithms_array:["arbitrage_125"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_126":{
		algorithms_array:["arbitrage_126"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_127":{
		algorithms_array:["arbitrage_127"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_128":{
		algorithms_array:["arbitrage_128"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_129":{
		algorithms_array:["arbitrage_129"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_130":{
		algorithms_array:["arbitrage_130"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_131":{
		algorithms_array:["arbitrage_131"],
		thresholds:{
			"ethbtc_gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_132":{
		algorithms_array:["arbitrage_132"],
		thresholds:{
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_133":{
		algorithms_array:["arbitrage_133"],
		thresholds:{
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_134":{
		algorithms_array:["arbitrage_134"],
		thresholds:{
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_135":{
		algorithms_array:["arbitrage_135"],
		thresholds:{
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_136":{
		algorithms_array:["arbitrage_136"],
		thresholds:{
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_137":{
		algorithms_array:["arbitrage_137"],
		thresholds:{
			"ethbtc_hitbtc":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_138":{
		algorithms_array:["arbitrage_138"],
		thresholds:{
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_139":{
		algorithms_array:["arbitrage_139"],
		thresholds:{
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_140":{
		algorithms_array:["arbitrage_140"],
		thresholds:{
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_141":{
		algorithms_array:["arbitrage_141"],
		thresholds:{
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_142":{
		algorithms_array:["arbitrage_142"],
		thresholds:{
			"ethbtc_huobipro":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_143":{
		algorithms_array:["arbitrage_143"],
		thresholds:{
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_144":{
		algorithms_array:["arbitrage_144"],
		thresholds:{
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_145":{
		algorithms_array:["arbitrage_145"],
		thresholds:{
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_146":{
		algorithms_array:["arbitrage_146"],
		thresholds:{
			"ethbtc_kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_147":{
		algorithms_array:["arbitrage_147"],
		thresholds:{
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_148":{
		algorithms_array:["arbitrage_148"],
		thresholds:{
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_149":{
		algorithms_array:["arbitrage_149"],
		thresholds:{
			"ethbtc_kucoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_150":{
		algorithms_array:["arbitrage_150"],
		thresholds:{
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_151":{
		algorithms_array:["arbitrage_151"],
		thresholds:{
			"ethbtc_okex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_152":{
		algorithms_array:["arbitrage_152"],
		thresholds:{
			"ethbtc_poloniex":{
				long_threshold:1,
				short_threshold:-1
			},
			"ethbtc_yobit":{
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
	poloniex:{
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
	kucoin:{
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
	gateio:{
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
	coinex:{
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
	cex:{
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
	exmo:{
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
	kraken:{
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
	hitbtc:{
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
	okex:{
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
	huobipro:{
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
	bitstamp:{
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
	gdax:{
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
	gemini:{
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
	yobit:{
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
	gatecoin:{
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
	ethbtc:{
		last:0.031
	},
	btcusd:{
		last:6300
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
	bitfinex: "keys/bitfinex.key",
	bittrex: "keys/bittrex.key",
}


