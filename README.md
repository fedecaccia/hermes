# Hermes <img align="right" width="45" height="45" src="img/hermes.png">
Hermes is a crypto platform to test and run trading algorithms.

## Main features
Under development.

## Installation
Hermes uses [ta-Lib](https://github.com/mrjbq7/ta-lib) library to compute technical analysis calculations, which is a python wrapper for [TA-Lib](http://ta-lib.org/). To use [ta-Lib](https://github.com/mrjbq7/ta-lib) for python, you need to have [TA-Lib](http://ta-lib.org/) already installed. You should probably follow their installation directions for your platform, but some suggestions are included below for reference.

**Linux**

Download [ta-lib-0.4.0-src.tar.gz](http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz) and:

```bash
untar and cd
./configure --prefix=/usr
make
sudo make install
```
Then you can install requirements typing in your terminal:
```bash
sudo pip3 install -r requirements.txt
```
which installs:
- [numpy](http://www.numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [ta-lib](https://github.com/mrjbq7/ta-lib) (python wrapper)

## Quickstart
Under development.

## Documentation
Under development.

## TODO

- [X] ~~Exchanges: Implement counter to avoid request rate limit. Implement barriers.~~
- [x] ~~EmulatedWorld: emulate fees by exhchanges (price increment or amount decrement according to exchange).~~
- [x] ~~Algorithms: load fees per exchanges.~~
- [x] ~~Oracle: implement pricing.~~
- [x] ~~Trading: check available funds in portfolio to execute algorithms in trading accounts.~~
- [x] ~~Portfolio: margin structure.~~
- [x] ~~Strategy: check available margin in portfolio to execute algorithms in margin accounts. (check asssets by thrs keys)~~
- [x] ~~Strategy: manage oracle updates.~~
- [X] ~~Strategy: manage portfolio updates.~~
- [ ] Strategy: check margin limits to show warnings.
- [ ] Strategy: check order status (and wait for that).
- [ ] World: save order ids.
- [x] ~~DataModule: create pandas dataframe requesting candles.~~
- [x] ~~DataModule: create pandas dataframe requesting orderbooks.~~
- [ ] EmulatedWorld: load data from sql.
- [ ] EmulatedWorld: load data from mongo.
- [x] ~~DataModule: implement ta-lib.~~
- [x] ~~Algorithms: implement simple pumping and dumping follower.~~
- [ ] Algorithms: implement crossing moving average algorithm.
- [ ] Algorithms: implement crossing moving average with volume algorithm.
- [ ] Algorithms: implement pair trading.
- [ ] Trade: Store transactions.
- [ ] Portolio: Compute P&L per asset.
- [ ] Portolio: Compute P&L in usd.
- [ ] Portolio: Compute P&L in other coins.
- [ ] Hermes: Save status (...).
- [ ] Hermes: Load status (...).
- [x] ~~RealWorld: online public orderbook requests.~~
- [x] ~~RealWorld: online public candles requests.~~
- [x] ~~RealWorld: online public balances requests.~~
- [ ] RealWorld: online private post order requests.
- [ ] **TESTS**.
- [ ] Implement function to save data in data_module. Similar to crypto_monitor.
- [ ] Implement mode *saving_data* which only saves data.
- [ ] Implement multiIP.

## Notes

### Fees
Different exchanges charge fees in different ways.
Most exchanges charge fees on the currency you are using to pay when you buy (or  on the currency you are receiving when you sell), like USD in BTC/USD.
If you are using Bitfinex for example, to be consistent you should adjust fees in Account/Fees and select: *Fees will be taken in the default currency set above* (BTC or USD).
This way, you will always receive the amount submited in the order.

## Contact
Developed by [CoinFabrik](https://www.coinfabrik.com/). 
Interested in crypto? You can read our articles [here](https://blog.coinfabrik.com/).
Any questions or suggestions feel free to contact me at federico.caccia@coinfabrik.com.

## Licensing
Copyright (C) 2018 Federico A. Caccia @ CoinFabrik

Hermes is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

Hermes is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Hermes.  If not, see <http://www.gnu.org/licenses/>.

### Icon licensing
<div>Icon made by <a href="http://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>
