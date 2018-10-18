import definitions

import time
import datetime


class Trade(object):

    """
    Trade: Trading instance which takes care of trading orders.
    """

    def __init__(
        self,
        world,
        oracle,
        assets,
        portfolio,
        request_pile,
        request_flag,
        mutex,
        order_pile):

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
        - order_pile: A pile where request_workers have put order ids (real world) or None (other).
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
        self.order_pile = order_pile
        # self._transactions_file = "transactions.dat"
        self._transactions_file = "trades/ini"+str(datetime.datetime.now())+".dat"
        self._real_transactions_file = "trades/tx_ini"+str(datetime.datetime.now())+".dat"
        self._warnings_file = "trades/warnings_ini"+str(datetime.datetime.now())+".dat"

    def check_funds(self, side, amount, exchange, account, base, quote, params):

        """
        + Description: Evaluate if funds are available to trade.
        + Input:
        - side: "buy" or "sell" string sides.
        - amount: float amount to trade or "full" string.
        In "full" case, the function computes the maximum amount able to trade.
        - exchange: Exchange string name.
        - account: Account in exchange string name.
        - base: Base currency string name.
        - quote: Quote currency string name.
        - params: Parameters of asset, like limit and last values.
        + Output:
        - funds_are_available: Bool indicating whether funds are available to trade or not.
        """

        if side == definitions.sell:

            base_in_portfolio = self.portfolio.get_amount_of_asset(exchange, account, base)

            if amount == definitions.full:                
                amount_to_sell = base_in_portfolio
            else:
                amount_to_sell = amount
            
            funds_are_available = amount_to_sell <= base_in_portfolio
            amount_to_trade = amount_to_sell

        elif side == definitions.buy:

            quote_in_portfolio = self.portfolio.get_amount_of_asset(exchange, account, quote)
            base_price = params[definitions.last]
            max_base_to_buy = quote_in_portfolio / base_price

            if amount == definitions.full:                
                # in this case we are trying to buy as much as we can
                # to secure this, we try to buy the 97% of the aproximated value the oracle tell us
                amount_to_buy = max_base_to_buy*0.97
            else:
                amount_to_buy = amount
            
            funds_are_available = max_base_to_buy >= amount_to_buy
            amount_to_trade = amount_to_buy

        return funds_are_available

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
        funds_are_available = False

        funds_are_available, amount_to_trade = self._evaluate_funds(side, amount, exchange, account, base, quote, params)

        if funds_are_available:

            self._call_threads_to_trade(asset_id, symbol, exchange, account, side, amount_to_trade, order_type, params)
        
            with open(self._transactions_file, "a") as out:
                out.write("\n"+str(self.world.get_time()))
                out.write("\n"+"Initiating transaction")
                out.write("\n"+asset_id + " " + side + " " + str(params))
                out.write("\n")

        else:
            raise ("ERROR: Funds are not enough checking inside trade.")
    
    def _evaluate_funds(self, side, amount, exchange, account, base, quote, params):

        """
        + Description: Evaluate if funds are available to trade.
        + Input:
        - side: "buy" or "sell" string sides.
        - amount: float amount to trade or "full" string.
        In "full" case, the function computes the maximum amount able to trade.
        - exchange: Exchange string name.
        - account: Account in exchange string name.
        - base: Base currency string name.
        - quote: Quote currency string name.
        - params: Parameters of asset, like limit and last values.
        + Output:
        - funds_are_available: Bool indicating whether funds are available to trade or not.
        - amount_to_trade: Float amount to buy or to sell.
        """

        if side == definitions.sell:

            base_in_portfolio = self.portfolio.get_amount_of_asset(exchange, account, base)

            if amount == definitions.full:                
                amount_to_sell = base_in_portfolio
            else:
                amount_to_sell = amount
            
            funds_are_available = amount_to_sell <= base_in_portfolio
            amount_to_trade = amount_to_sell

        elif side == definitions.buy:

            quote_in_portfolio = self.portfolio.get_amount_of_asset(exchange, account, quote)
            base_price = params[definitions.last]
            max_base_to_buy = quote_in_portfolio / base_price

            if amount == definitions.full:                
                # in this case we are trying to buy as much as we can
                # to secure this, we try to buy the 97% of the aproximated value the oracle tell us
                amount_to_buy = max_base_to_buy*0.97
            else:
                amount_to_buy = amount
            
            funds_are_available = max_base_to_buy >= amount_to_buy
            amount_to_trade = amount_to_buy

        return funds_are_available, amount_to_trade

    def _call_threads_to_trade(self, asset_id, symbol, exchange, account, side, amount_to_trade, order_type, params):

        """
        + Description: Put trade order in a pile where workers collect works.
        + Input:
        - asset_id: Asset id string name.
        - symbol: Symbol string name.
        - exchange: Exchange string name.
        - account: Account in exchange string name.
        - side: "buy" or "sell" string sides.
        - amount_to_trade: Float amount to buy or to sell.
        - order_type: Type of order string name.
        - params: Dictionary of parameters required to post order.
        + Output:
        -
        """

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
                definitions.amount:amount_to_trade,
                definitions.order_type:order_type,
                definitions.params:params                
                }
            })

        while self.request_flag[0]>0:
            pass

    def check_orders(self):

        """
        + Description: Check order status, looking for order ids in order_pile.
        + Input:
        -        
        + Output:
        -
        """

        # Workers have finished function evaluation
        # They were waited in while loop in _call_threads_to_trade()

        if self.order_pile:
            time.sleep(0.5) # wait to complete order
            print("Checking order status...")
            for _ in range(self.order_pile.qsize()):
                order = self.order_pile.get()
                exchange = order[definitions.exchange]
                order_id = order[definitions.order_id]
                amount = order[definitions.amount]
                response = self.world.check_order(exchange, order_id, amount)
                
                filled = float(response[definitions.filled])
                symbol = float(response[definitions.symbol])
                side = float(response[definitions.side])
                status = float(response[definitions.status])
                price = float(response[definitions.average])
                fee = float(response[definitions.fee])
                if filled != amount or status != definitions.closed:                    
                    print("WARNING! Order incomplete")
                    with open(self._warnings_file, "a") as out:
                        out.write("\n"+str(self.world.get_time()))
                        out.write("\n"+exchange + " - symbol: " + symbol +\
                        " - filled: " + filled + " of amount: " + amount +
                        " - side: " + side + " - order id:" + order_id + ":" + status)
                        out.write("\n")

                        if status == definitions.canceled:
                            # algo.update_status()
                            pass
                        elif status == definitions.opened:                            
                            self.order_pile.put(order) # put it again to check it later
                else:
                    with open(self._real_transactions_file, "a") as out:
                        out.write("\n"+str(self.world.get_time()))
                        out.write("\n"+"Transaction complete")
                        out.write("\n exchange: "+exchange)
                        out.write("\n symbol: "+symbol)
                        out.write("\n amount: "+amount)
                        out.write("\n side: "+side)
                        out.write("\n price: "+price)
                        out.write("\n fee: "+fee)
                        out.write("\n")

            print("Order checking finished")