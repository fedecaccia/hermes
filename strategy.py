import numpy as np

from abc import ABC, abstractmethod


class Strategy(ABC):

    """
    Strategy: a generic class to implement data reception and algorithm evaluation.
    Based on a sum over individual algorithm punctuation values, takes a trading decision.
    """

    def __init__(self,
                 id,
                 threshold,
                 request_pile,
                 request_flags,
                 algorithms,
                 data_modules,
                 portfolio,trading):

        """
        + Description: constructor
        + Input:
        - id: Strategy id.
        - threshold: Min integer valuation value to shoot trading order.        
        - request_pile: a pile to where request_workers look functions to evaluate.
        - request_flags: an array of flags indicanting that a given worker is waiting (0) or working (1).
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
        self.request_pile = request_pile
        self.request_flags = request_flags
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
        for i in range(len(self.request_flags)):
            self.request_flags[i] = 1 # all workers are flagged as working
        
        for module in self.data_modules:
            self.request_pile.put(module.update)

        while np.any(self.request_flags): # some worker is still working
            pass
        print("All modules have been updated")

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
        print("valuation", self._valuation)
        if self._valuation >= self._threshold:
            print("Shooting trading order")
        