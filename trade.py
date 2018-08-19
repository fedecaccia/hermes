import definitions


class Trade(object):

    """
    Trade: Trading instance which takes care of trading orders.
    """

    def __init__(self, world, oracle, assets, portfolio, request_pile, request_flag):

        """
        + Description: Constructor.
        + Input:
        - world: World object.
        - world: Oracle object.
        - assets: Dictionary of asset object.
        - portfolio: Portfolio objetc.
        - request_pile: A pile where request_workers look functions to evaluate.
        - request_flag: List of 1 flag ([flag]) to indicate how many workers are bussy.
        + Output:
        -
        """

        self.world = world
        self.oracle = oracle
        self.assets = assets
        self.portfolio = portfolio
        self.request_pile = request_pile
        self.request_flag = request_flag

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
        
        symbol = self.assets[asset_id].symbol
        exchange = self.assets[asset_id].exchange
        account = self.assets[asset_id].account        

        if amount==definitions.full and side==definitions.sell:
            coin = symbol.split("/")[0]
            amount = self.portfolio.get_balance_in_exchange(coin, exchange)
        
        elif amount==definitions.full and side==definitions.buy:
            coin = symbol.split("/")[0]
            quote = symbol.split("/")[1]
            quote_amount = self.portfolio.get_balance_in_exchange(quote, exchange)
            # in this case we are trying to buy as much as we can
            # to secure this, we try to buy the 97% if the aproximated value the oracle tell us
            amount = self.oracle.get_amount_in_base(coin, quote, quote_amount)*0.97

        else:
            # amount is rightly calculated
            pass
        
        self.request_flag[0] += 1
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