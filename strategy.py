from abc import ABC, abstractmethod


class Strategy(ABC):

    """
    Strategy: a generic class to implement data reception and algorithm evaluation.
    Based on a sum over individual algorithm punctuation values, takes a trading decision.
    """

    def __init__(self, id, threshold, requests_pile, algorithms, data_modules, portfolio, trading):

        """
        + Description: constructor
        + Input:
        - id: Strategy id.
        - threshold: min integer valuation value to shoot trading order.        
        - algorithms: Dictionary of algorithm objects.
        - data_modules: Array of all data_modules objects used in startegy.
        - portfolio: portfolio object.
        - trading: trading platform object.
        + Output:
        -
        """

        self.id = id
        self._threshold = threshold
        self.data_modules = data_modules
        self.requests_pile = requests_pile
        self.algorithms = algorithms
        self.portfolio = portfolio
        self.trading = trading
        self._valuation = 0

    def execute(self):

        """
        + Description: Strategy executor.
        + Input:
        - 
        + Output:
        -
        """

        print("\nExecuting strategy id: "+str(self.id))  
        self._restart_valuation()      
        self._update_data_modules()
        self._evaluate_algorithms()
        self._analyze_valuation()

    def _update_data_modules(self):

        """
        + Description: Function to update all data modules in strategy.
        + Input:
        - 
        + Output:
        -
        """

        print("Updating data modules")
        for module in self.data_modules:
            self.requests_pile.put(module.update())

    def _restart_valuation(self):

        """
        + Description: Function to reinitialize valuation.
        + Input:
        - 
        + Output:
        -
        """

        self._valuation = 0

    def _evaluate_algorithms(self):

        """
        + Description: Run algorithms.
        + Input:
        - 
        + Output:
        -
        """

        for algorithm in self.algorithms:
            self._valuation += algorithm.evaluate()

    def _analyze_valuation(self):

        """
        + Description: Shoots trade order in case that valuation is greater than threshold.
        + Input:
        - 
        + Output:
        -
        """

        if self._valuation >= self._threshold:
            print("Shooting trading order")
        