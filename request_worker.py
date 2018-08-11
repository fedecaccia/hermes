from threading import Thread


class RequestWorker(Thread):

    """
    RequestWorker: particular thread that make requests.
    """

    def __init__(self, thread_id, request_queue, request_flag, mutex):

        """
        + Description: constructor
        + Input:
        - thread_id: integer thread id.
        - request_queue: pile where requests are stacked.
        - request_flag: list of 1 flag ([flag]) to indicate how many workers are bussy.
        - mutext: thread locker
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

        while function is not None:
            
            self._evaluate_function(function)            
            function = self.request_queue.get()

    def _evaluate_function(self, function):

        """
        + Description: input function evaluation
        + Input:
        - function
        + Output:
        -
        """

        function()
        self.mutex.acquire()
        self.request_flag[0] -= 1
        self.mutex.release()
