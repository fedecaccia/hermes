import definitions

from wallet import Wallet

import datetime

import pandas as pd


class Portfolio(object):

    """
    Portfolio: Global balance build with individual exchange wallets.
    """

    def __init__(self, world, exchanges_names):

        """
        + Description: constructor.
        + Input:
        - world: world object connection.
        - exchanges names: list of string exchange names.
        + Output:
        -
        """

        self.world = world
        self.exchanges_names = exchanges_names
        # self.balance = {
        #     exchange_name: Wallet(world, exchange_name) for exchange_name in exchanges_names
        # }
        self.balance = {exchange_name: None for exchange_name in exchanges_names}
        self._last_update = pd.datetime(1970,1,1)
        self._delta_update = datetime.timedelta(minutes=30)
        
        self.update()


    def get_total_balance(self, coin):

        """
        + Description: returns total balance of portfolio valuated in coin.
        + Input:
        - coin: String of the reference coin.
        + Output:
        - value: Float portfolio value in coin.
        """    

        pass

    def get_balance_in_exchange(self, coin, exchange):

        """
        + Description: returns balance of funds in a particular exchange valuated in coin.
        + Input:
        - coin: String of the reference coin.
        - exchange: Exchange string name.
        + Output:
        - value: Float portfolio value in coin.
        """    

        pass

    def get_amount_of_asset(self, exchange, account, asset):

        """
        + Description: returns amount of asset in a particular account of a given exchange.
        If the account refers to margin trading, it returns the maximum amount available to trade
        (using leverage).
        + Input:
        - exchange: Exchange string name.
        - account: Account string name.
        - asset: Asset string name.
        + Output:
        - value: Float amount of asset.
        """

        if account != definitions.margin_trading:
            try:
                return self.balance[exchange][account][asset][definitions.free]
            except:
                print("WARNING: without funds: "+asset+" in account: "+account+" in: "+exchange)
                return 0
        else:
            try:
                return self.balance[exchange][definitions.margin_trading][definitions.tradable_balance][asset]
            except:
                print("WARNING: without tradable balance for: "+asset+" in margin trading account in: "+exchange)
                return 0

    def update(self):

        """
        + Description: Update each wallet.
        + Input:
        -
        + Output:
        -
        """

        for exchange in self.exchanges_names:
            self.balance[exchange] = self.world.request_balance(exchange)

    def check_update(self):

        """
        + Description: Check if update is needed.
        + Input:
        -
        + Output:
        -
        """

        if self.world.get_time() - self._last_update > self._delta_update:

            for exchange in self.exchanges_names:
                self.balance[exchange] = self.world.request_balance(exchange)
                
            self._last_update = self.world.get_time()

    def show(self):

        """
        + Description: Print wallets contents.
        + Input:
        -
        + Output:
        -
        """

        self.world.show_time()

        print("\nPortfolio:")
        for exchange in self.exchanges_names:
            self.balance[exchange].show()