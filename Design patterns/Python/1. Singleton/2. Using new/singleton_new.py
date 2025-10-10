import threading

class SingletonNew():
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

class Logger(SingletonNew):
    def __init__(self):
        if not hasattr(self, '_initialized') or not self._initialized:
            print("Logger class initialized")
            self._initialized = True

class Database(SingletonNew):
    def __init__(self, url):
        if not hasattr(self, '_initialized') or not self._initialized:
            self.url = url
            print("Database connected")
            self._initialized = True