from threading import Thread


class RequestWorker(Thread):

    """
    RequestWorker: particular thread that make requests.
    """

    def __init__(self, thread_id, request_queue, request_flags, mutex):

        """
        + Description: constructor
        + Input:
        - thread_id: integer thread id.
        - request_queue: pile where requests are stacked.
        - request_flags: list of flags to indicate wheter a given thread is working.
        0 means waiting, and 1 means working.
        - mutext: thread locker
        + Output:
        -
        """

        Thread.__init__(self)
        self.id = thread_id
        self.request_queue = request_queue        
        self.request_flags = request_flags
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
        function()
        self.mutex.acquire()
        self.request_flags[self.id] = 0
        self.mutex.release()

        while function != None:
            function = self.request_queue.get()
            function()
            self.mutex.acquire()
            self.request_flags[self.id] = 0
            self.mutex.release()

        # esto esta mal cuando no todos los threads tienen que estar ocupados
