import threading


class Doer:

    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()

        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, action):
        self.lock1.acquire()
        action()
        self.lock2.release()

    def second(self, action):
        self.lock2.acquire()
        action()
        self.lock3.release()

    def third(self, action):
        self.lock3.acquire()
        action()
        self.lock1.release()
