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

    def __init__(self):

        """
        + Description: constructor
        + Input:
        -
        + Output:
        -
        """

        super().__init__()


class Oracle(World):

    """
    Oracle: Fast information from databases or real world.
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