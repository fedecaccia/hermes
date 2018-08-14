import definitions

from abc import ABC, abstractmethod


class DataModule(ABC):

    """
    DataModule: Module to store data description, content and analysis.
    """

    def __init__(self, element, world):

        """
        + Description: constructor
        + Input:
        - element: main descriptions.
        - world:
        + Output:
        -
        """

        self._check_element_consistency(element)
        self.id = element[definitions.data_id]
        self.description = element[definitions.description]
        self.source = element[definitions.source]
        self.data_type = element[definitions.data_type]
        self.world = world
    
    @abstractmethod
    def _check_element_consistency(self, element):
        pass
    
    def update(self):

        """
        Description: connection to world, to update values.
        + Input:
        -.
        + Output:
        -
        """

        data = self.world.request_data(self.id)
        print("Data module: "+str(self.id)+" updated.")


class Candles(DataModule):

    """
    Candles: Module to store candles data description, content and analysis.
    """

    def __init__(self, element, world):

        """
        + Description: constructor
        + Input:
        - element: main descriptions.
        - world: world connection.
        + Output:
        -
        """

        super().__init__(element, world)
        self.ticker = element[definitions.description]
        self.exchange = element[definitions.source]
        self.timeframe = element[definitions.timeframe]

    def _check_element_consistency(self, element):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - element: main descriptions.
        + Output:
        -
        """

        pass


class Orderbook(DataModule):

    """
    Orderbook: Module to store orderbook data description, content and analysis.
    """

    def __init__(self, element, world):

        """
        + Description: constructor
        + Input:
        - element: main descriptions.
        - world: world connection.
        + Output:
        -
        """

        super().__init__(element, world)
        self.ticker = element[definitions.description]
        self.exchange = element[definitions.source]

    def _check_element_consistency(self, element):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - element: main descriptions.
        + Output:
        -
        """

        pass


class Tickers(DataModule):

    """
    Tickers: Module to store tickers data description, content and analysis.
    """

    def __init__(self, element, world):

        """
        + Description: constructor
        + Input:
        - element: main descriptions.
        - world: world connection.
        + Output:
        -
        """

        super().__init__(element, world)
        self.ticker = element[definitions.description]
        self.exchange = element[definitions.source]
    
    def _check_element_consistency(self, element):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - element: main descriptions.
        + Output:
        -
        """

        pass


class Tweets(DataModule):

    """
    Tweets: Module to store tweets data description, content and analysis.
    """

    def __init__(self, element, world):

        """
        + Description: constructor
        + Input:
        - element: main descriptions.
        - world: world connection.
        + Output:
        -
        """

        super().__init__(element, world)
        self.description = element[definitions.description]
        self.source = element[definitions.source]

    def _check_element_consistency(self, element):
        
        """
        Description: check consistency in the element built by user.
        + Input:
        - element: main descriptions.
        + Output:
        -
        """

        pass