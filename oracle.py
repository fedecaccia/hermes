import definitions

import datetime


class Oracle(object):

    """
    Oracle: Fast information from databases or real world.
    """

    def __init__(self, world):

        """
        + Description: Constructor.
        + Input:
        - current world
        + Output:
        -
        """

        super().__init__()
        self.world = world
        self.fees = self.world.fees
        self._last_update = pd.datetime(1970,1,1)
        self._delta_update = datetime.timedelta(minutes=10)
        self.update()

    def update(self):

        """
        + Description: Update values if it's necessary.
        + Input:
        -
        + Output:
        -
        """

        if self.world.get_time() - self._last_update > self._delta_update:            
            self.world.update_tickers()
            self.tickers = self.world.get_tickers()
            self._last_update = self.world.get_time()

    def get_amount_in_base(self, base, quote, quote_amount):

        """
        + Description: Returns the equivalent value of base amount to quote_amount.
        + Input:
        - base: Asset currency string name.
        - quote: Quote currency string name.
        - quote_amount: Float amount of quote currency.
        + Output:
        -
        """

        symbol = base.upper()+"/"+quote.upper()

        try:
            amount = self.tickers[symbol][definitions.last]
        except:
            raise ValueError("Error in oracle trying to retrieve last for symbol: '"+symbol+"'.")
        
        return amount