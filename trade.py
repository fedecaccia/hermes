import definitions


class Trade(object):

    """
    Trade: Trading instance which takes care of trading orders.
    """

    def __init__(self, world, assets, portfolio, request_pile, request_flag):

        """
        + Description: Constructor.
        + Input:
        - world: World object.
        - assets: Dictionary of asset object.
        - portfolio: Portfolio objetc.
        - request_pile: A pile where request_workers look functions to evaluate.
        - request_flag: List of 1 flag ([flag]) to indicate how many workers are bussy.
        + Output:
        -
        """

        self.world = world
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
        - amount: float amount to trade.
        - params: Dictionary of parameters required to post order.
        + Output:
        -
        """
        
        symbol = self.assets[asset_id].symbol
        exchange = self.assets[asset_id].exchange
        account = self.assets[asset_id].account
        
        self.request_pile.put({
            definitions.function:self.world.post_order,
            definitions.params:{
                definitions.asset_id:asset_id,
                definitions.symbol:symbol,
                definitions.exchange:exchange,
                definitions.account:account,
                definitions.side:side,
                definitions.amount:amount,
                definitions.params:params                
                }
            })