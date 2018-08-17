class Trade(object):

    """
    Trade: Trading instance which takes care of trading orders.
    """

    def __init__(self, world, portfolio):

        """
        + Description: Constructor.
        + Input:
        - world
        - portfolio
        + Output:
        -
        """
        self.world = world
        self.portfolio = portfolio

    def execute_order(self, asset_id, order_type, side, params, amount):
        
        """
        + Description: call trading order in client.
        + Input:
        - asset_id: Asset id string name.        
        - order_type: Type of order string name.
        - side: "buy" or "sell" string sides.        
        - params: Dictionary of special parameters according to the type of order.
        - amount: Float amount to trade.
        + Output:
        -
        """

        print("Executing order:", asset_id, order_type, side, amount)