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
        self._world = world
        self.data = None
        self._initialize_data()
    
    @abstractmethod
    def _check_element_consistency(self, element):
        pass
    
    @abstractmethod
    def _initialize_data(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def _data_is_new(self, income_data):
        pass
    
    def _data_is_not_none(self, incoming_data):

        """
        Description: evaluate wether incoming data is None.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """

        if incoming_data is None:
            return False
        return True


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


    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        self.data = []
    
    def update(self):

        """
        Description: connection to world, to update values.
        + Input:
        -.
        + Output:
        -
        """

        incoming_data = self._world.request_data(self.id)

        if self._data_is_new(incoming_data) and self._data_is_not_none(incoming_data):
            self.data.append(incoming_data)
            print("Data module: "+str(self.id)+" updated.")

        else:
            print("Data module is old or None")

    def _data_is_new(self, incoming_data):
        
        """
        Description: evaluate wether incoming data is new or repeated.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """
        
        return True


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

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        pass

    def update(self):

        """
        Description: connection to world, to update values.
        + Input:
        -.
        + Output:
        -
        """

        data = self._world.request_data(self.id)
        print(data)
        print("Data module: "+str(self.id)+" updated.")

    def _data_is_new(self, incoming_data):
        
        """
        Description: evaluate wether incoming data is new or repeated.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """
        
        return True


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

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        pass

    def update(self):

        """
        Description: connection to world, to update values.
        + Input:
        -.
        + Output:
        -
        """

        data = self._world.request_data(self.id)
        print(data)
        print("Data module: "+str(self.id)+" updated.")

    def _data_is_new(self, incoming_data):
        
        """
        Description: evaluate wether incoming data is new or repeated.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """
        
        return True


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

    def _initialize_data(self):

        """
        Description: initialize an empty data object.
        + Input:
        -
        + Output:
        -
        """

        pass

    def update(self):

        """
        Description: connection to world, to update values.
        + Input:
        -.
        + Output:
        -
        """

        data = self._world.request_data(self.id)
        print(data)
        print("Data module: "+str(self.id)+" updated.")

    def _data_is_new(self, incoming_data):
        
        """
        Description: evaluate wether incoming data is new or repeated.
        + Input:
        - incoming_data: dict containing incoming data.
        + Output:
        - Bool.
        """
        
        return True