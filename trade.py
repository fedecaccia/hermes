import definitions


class Trade(object):

    """
    Trade: Trading instance which takes care of trading orders.
    """

    def __init__(self, world, oracle, assets, portfolio, request_pile, request_flag, mutex):

        """
        + Description: Constructor.
        + Input:
        - world: World object.
        - world: Oracle object.
        - assets: Dictionary of asset object.
        - portfolio: Portfolio objetc.
        - request_pile: A pile where request_workers look functions to evaluate.
        - request_flag: List of 1 flag ([flag]) to indicate how many workers are bussy.
        - mutext: Thread locker.
        + Output:
        -
        """

        self.world = world
        self.oracle = oracle
        self.assets = assets
        self.portfolio = portfolio
        self.request_pile = request_pile
        self.request_flag = request_flag
        self.mutex = mutex

    def execute_order(self, asset_id, order_type, side, amount, params):
        
        """
        + Description: call trading order in client.
        + Input:
        - asset_id: Asset id string name.        
        - order_type: Type of order string name.
        - side: "buy" or "sell" string sides.
        - amount: float amount to trade or "full" string.
        In "full" case, the function computes the maximum amount able to trade.
        - params: Dictionary of parameters required to post order.
        + Output:
        -
        """
        
        exchange = self.assets[asset_id].exchange
        account = self.assets[asset_id].account
        symbol = self.assets[asset_id].symbol
        base, quote = symbol.split("/")[:2]
        trade_available = False

        if side == definitions.sell:

            if amount == definitions.full:
                
                amount = self.portfolio.get_amount_of_asset(exchange, account, base)
            
            trade_available = self._funds_are_available(exchange, account, base, amount)

        elif side == definitions.buy:

            if amount == definitions.full:

                quote_available = self.portfolio.get_amount_of_asset(exchange, account, quote)           
                # in this case we are trying to buy as much as we can
                # to secure this, we try to buy the 97% if the aproximated value the oracle tell us
                amount = self.oracle.get_amount_in_base(base, quote, quote_available)*0.97             
            
            trade_available = self._funds_are_available(exchange, account, quote, amount)

        if trade_available:
        
            self.mutex.acquire()
            self.request_flag[0] += 1
            self.mutex.release()

            self.request_pile.put({
                definitions.function:self.world.post_order,
                definitions.params:{
                    definitions.asset_id:asset_id,
                    definitions.symbol:symbol,
                    definitions.exchange:exchange,
                    definitions.account:account,
                    definitions.side:side,
                    definitions.amount:amount,
                    definitions.order_type:order_type,
                    definitions.params:params                
                    }
                })

            while self.request_flag[0]>0:
                pass

            with open("transactions.dat", "a") as out:
                out.write("\n"+str(self.world.get_time()))
                out.write("\n"+asset_id)
                out.write("\n"+order_type)
                out.write("\n"+side)
                out.write("\n"+str(amount))
                out.write("\n"+str(params))
                out.write("\n")

        else:
            print("WARNING: Funds are not enough")

    def _funds_are_available(self, exchange, account, currency, amount):

        """
        + Description: Check if funds are available to trade.
        + Input:
        - 
        + Output:
        -
        """
        return self.portfolio.get_amount_of_asset(exchange, account, currency) >= amount
