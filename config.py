from definitions import *


#######################################################
#                  DATA SECTION
#######################################################

data_elements = {
	"orderbook_btcusd_Bitstamp":{
		description: btcusd,
		source: Bitstamp,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBitstampBTCUSD.csv",
	},
	"orderbook_btcusd_Bittrex":{
		description: btcusd,
		source: Bittrex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookBittrexpBTCUSD.csv",
	},
	"orderbook_btcusd_Cex":{
		description: btcusd,
		source: Cex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookCexBTCUSD.csv",
	},
	"orderbook_btcusd_Exmo":{
		description: btcusd,
		source: Exmo,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookExmoBTCUSD.csv",
	},
	"orderbook_btcusd_Gatecoin":{
		description: btcusd,
		source: Gatecoin,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGatecoinBTCUSD.csv",
	},
	"orderbook_btcusd_Gdax":{
		description: btcusd,
		source: Gdax,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGdaxBTCUSD.csv",
	},
	"orderbook_btcusd_Gemini":{
		description: btcusd,
		source: Gemini,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookGeminiBTCUSD.csv",
	},
	"orderbook_btcusd_Kraken":{
		description: btcusd,
		source: Kraken,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookKrakenBTCUSD.csv",
	},
	"orderbook_btcusd_Okex":{
		description: btcusd,
		source: Okex,
		data_type: orderbook,
		timeframe: one_sec,
		data_format: csv,
		header_format: cdm,
		file_name: "data/orderbookOkexBTCUSD.csv",
	},
	"orderbook_btcusd_Yobit":{
		description: btcusd,
		source: Yobit,
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
	"btcusd_Bitstamp":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Bitstamp,
		account: trading,
	},
	"btcusd_Bittrex":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Bittrex,
		account: trading,
	},
	"btcusd_Cex":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Cex,
		account: trading,
	},
	"btcusd_Exmo":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Exmo,
		account: trading,
	},
	"btcusd_Gatecoin":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Gatecoin,
		account: trading,
	},
	"btcusd_Gdax":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Gdax,
		account: trading,
	},
	"btcusd_Gemini":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Gemini,
		account: trading,
	},
	"btcusd_Kraken":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Kraken,
		account: trading,
	},
	"btcusd_Okex":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Okex,
		account: trading,
	},
	"btcusd_Yobit":{
		symbol: btcusd,
		base: btc,
		quote: usd,
		exchange: Yobit,
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
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Bittrex
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_1":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Cex
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_2":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Exmo
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_3":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Gatecoin
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_4":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Gdax
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_5":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Gemini
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_6":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_7":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_8":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bitstamp,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Bitstamp:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_9":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Cex
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_10":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Exmo
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_11":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Gatecoin
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_12":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Gdax
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_13":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Gemini
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_14":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_15":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_16":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Bittrex,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Bittrex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_17":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Exmo
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_18":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Gatecoin
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_19":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Gdax
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_20":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Gemini
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_21":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_22":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_23":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Cex,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Cex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_24":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Exmo,
			orderbook_btcusd_Gatecoin
		],
		signals: {
			btcusd_Exmo:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_25":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Exmo,
			orderbook_btcusd_Gdax
		],
		signals: {
			btcusd_Exmo:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_26":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Exmo,
			orderbook_btcusd_Gemini
		],
		signals: {
			btcusd_Exmo:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_27":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Exmo,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Exmo:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_28":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Exmo,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Exmo:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_29":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Exmo,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Exmo:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_30":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gatecoin,
			orderbook_btcusd_Gdax
		],
		signals: {
			btcusd_Gatecoin:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_31":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gatecoin,
			orderbook_btcusd_Gemini
		],
		signals: {
			btcusd_Gatecoin:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_32":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gatecoin,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Gatecoin:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_33":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gatecoin,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Gatecoin:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_34":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gatecoin,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Gatecoin:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_35":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gdax,
			orderbook_btcusd_Gemini
		],
		signals: {
			btcusd_Gdax:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_36":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gdax,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Gdax:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_37":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gdax,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Gdax:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_38":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gdax,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Gdax:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_39":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gemini,
			orderbook_btcusd_Kraken
		],
		signals: {
			btcusd_Gemini:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_40":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gemini,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Gemini:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_41":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Gemini,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Gemini:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_42":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Kraken,
			orderbook_btcusd_Okex
		],
		signals: {
			btcusd_Kraken:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_43":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Kraken,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Kraken:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
			period:30,
		},
	},
	"arbitrage_44":{
		algorithm: statarb,
		data_modules_array: [
			orderbook_btcusd_Okex,
			orderbook_btcusd_Yobit
		],
		signals: {
			btcusd_Okex:{
				long_signal:1,
				short_signal:-1,
			},
		},
		algo_params: {
			limit_buy_pct:100,
			usd_amount_to_trade:50,
			max_delay_in_data:2,
			limit_sell_pct:100,
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
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_1":{
		algorithms_array:["arbitrage_1"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_2":{
		algorithms_array:["arbitrage_2"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_3":{
		algorithms_array:["arbitrage_3"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_4":{
		algorithms_array:["arbitrage_4"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_5":{
		algorithms_array:["arbitrage_5"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_6":{
		algorithms_array:["arbitrage_6"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_7":{
		algorithms_array:["arbitrage_7"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_8":{
		algorithms_array:["arbitrage_8"],
		thresholds:{
			"btcusd_Bitstamp":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_9":{
		algorithms_array:["arbitrage_9"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_10":{
		algorithms_array:["arbitrage_10"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_11":{
		algorithms_array:["arbitrage_11"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_12":{
		algorithms_array:["arbitrage_12"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_13":{
		algorithms_array:["arbitrage_13"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_14":{
		algorithms_array:["arbitrage_14"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_15":{
		algorithms_array:["arbitrage_15"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_16":{
		algorithms_array:["arbitrage_16"],
		thresholds:{
			"btcusd_Bittrex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_17":{
		algorithms_array:["arbitrage_17"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_18":{
		algorithms_array:["arbitrage_18"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_19":{
		algorithms_array:["arbitrage_19"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_20":{
		algorithms_array:["arbitrage_20"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_21":{
		algorithms_array:["arbitrage_21"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_22":{
		algorithms_array:["arbitrage_22"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_23":{
		algorithms_array:["arbitrage_23"],
		thresholds:{
			"btcusd_Cex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_24":{
		algorithms_array:["arbitrage_24"],
		thresholds:{
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_25":{
		algorithms_array:["arbitrage_25"],
		thresholds:{
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_26":{
		algorithms_array:["arbitrage_26"],
		thresholds:{
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_27":{
		algorithms_array:["arbitrage_27"],
		thresholds:{
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_28":{
		algorithms_array:["arbitrage_28"],
		thresholds:{
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_29":{
		algorithms_array:["arbitrage_29"],
		thresholds:{
			"btcusd_Exmo":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_30":{
		algorithms_array:["arbitrage_30"],
		thresholds:{
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_31":{
		algorithms_array:["arbitrage_31"],
		thresholds:{
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_32":{
		algorithms_array:["arbitrage_32"],
		thresholds:{
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_33":{
		algorithms_array:["arbitrage_33"],
		thresholds:{
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_34":{
		algorithms_array:["arbitrage_34"],
		thresholds:{
			"btcusd_Gatecoin":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_35":{
		algorithms_array:["arbitrage_35"],
		thresholds:{
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_36":{
		algorithms_array:["arbitrage_36"],
		thresholds:{
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_37":{
		algorithms_array:["arbitrage_37"],
		thresholds:{
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_38":{
		algorithms_array:["arbitrage_38"],
		thresholds:{
			"btcusd_Gdax":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_39":{
		algorithms_array:["arbitrage_39"],
		thresholds:{
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_40":{
		algorithms_array:["arbitrage_40"],
		thresholds:{
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_41":{
		algorithms_array:["arbitrage_41"],
		thresholds:{
			"btcusd_Gemini":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_42":{
		algorithms_array:["arbitrage_42"],
		thresholds:{
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_43":{
		algorithms_array:["arbitrage_43"],
		thresholds:{
			"btcusd_Kraken":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
				long_threshold:1,
				short_threshold:-1
			}
		},
		order_type:limit
	},
	"strategy_44":{
		algorithms_array:["arbitrage_44"],
		thresholds:{
			"btcusd_Okex":{
				long_threshold:1,
				short_threshold:-1
			},
			"btcusd_Yobit":{
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
	Yobit:{
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
	Bitstamp:{
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
	Kraken:{
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
	Okex:{
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
	Cex:{
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
	Gatecoin:{
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
	Gdax:{
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
	Bittrex:{
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
	Gemini:{
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
	Exmo:{
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


