import definitions


class Asset(object):

    """
    Asset: Class to instance assets.
    """

    def __init__(self, asset_id, asset_element):

        """
        + Description: constructor
        + Input:
        - asset_id: String asset name
        - asset_element: Dictionary of variables and values.
        + Output:
        -
        """

        self.id = asset_id
        self.symbol = asset_element[definitions.symbol]
        self.base = asset_element[definitions.base]
        self.quote = asset_element[definitions.quote]
        self.exchange = asset_element[definitions.exchange]
        self.account = asset_element[definitions.account]

