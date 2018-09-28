import time

import definitions

from threading import Thread


class RequestWorker(Thread):

    """
    RequestWorker: particular thread that make requests.
    """

    def __init__(self, thread_id, request_queue, request_flag, mutex):

        """
        + Description: constructor
        + Input:
        - thread_id: Integer thread id.
        - request_queue: Pile where requests are stacked.
        None element act as a signal to finish.
        - request_flag: List of 1 flag ([flag]) to indicate how many workers are bussy.
        - mutext: Thread locker.
        + Output:
        -
        """

        Thread.__init__(self)
        self.id = thread_id
        self.request_queue = request_queue        
        self.request_flag = request_flag
        self.mutex = mutex

    def run(self):

        """
        + Description: thread execution
        + Input:
        -
        + Output:
        -
        """

        print("Request worker: "+str(self.id)+" started.")
        
        function = self.request_queue.get()

        # None element act as a signal to finish
        while function is not None:
            
            self._evaluate_function(
                function[definitions.function], 
                function[definitions.params]
            )            
            function = self.request_queue.get()

        print("Request worker "+str(self.id)+" found None signal.")

    def _evaluate_function(self, function, params):

        """
        + Description: Input function evaluation.
        + Input:
        - function: Function to evaluate.
        - params: Dictionary containing parameters definitions needed by function.
        + Output:
        -
        """

        function(params)
        
        self.mutex.acquire()
        self.request_flag[0] -= 1
        self.mutex.release()