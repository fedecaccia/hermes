import definitions

from abc import ABC, abstractmethod


class World(ABC):

    """
    World: Connection with external services which provides exchange information and also receive trading orders.
    """

    def __init__(self):

        """
        + Description: constructor
        + Input:
        -
        + Output:
        -
        """

        pass


class EmulatedWorld(World):

    """
    BacktestWorld: Connection with databases and ficticious accounts.
    Inherit from World.
    """

    def __init__(self):

        """
        + Description: constructor
        + Input:
        -
        + Output:
        -
        """

        super().__init__()


class RealWorld(World):

    """
    RealWorld: Connection with exchanges.
    Inherit from World.
    """

    def __init__(self, mode):

        """
        + Description: constructor
        + Input:
        -
        + Output:
        -
        """

        super().__init__()
        self.mode = mode
        if self.mode == self.definitions.real:
            self._create_clients_with_private_connections()

    def _create_clients_with_private_connections(self):
        pass


class Oracle(World):

    """
    Oracle: Fast information from databases or real world.
    Inherit from World.
    """

    def __init__(self, world):

        """
        + Description: constructor
        + Input:
        - current world
        + Output:
        -
        """

        super().__init__()