import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Logger(metaclass = SingletonMeta):
    def __init__(self):
        print("Logger class initialized")


class Database(metaclass = SingletonMeta):
    def __init__(self, url):
        self.url = url
        print("Database connected")