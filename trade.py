class Trade(object):

    """
    Trade: Trading instance which takes care of trading orders.
    """

    def __init__(self, world, portfolio):

        """
        + Description: constructor.
        + Input:
        - world
        - portfolio
        + Output:
        -
        """
        self.world = world
        self.portfolio = portfolio