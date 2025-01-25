import threading
'''
Note  : The GIL is a mechanism used by CPython to ensure that 
only one thread executes Python bytecode at a time, even on multi-core systems.
'''
class Count:
    def __init__(self):
        self.value = 0
        self.mutex = threading.Lock()
    
    def add(self, amount):
        with self.mutex:
            self.value += amount
    
    def subtract(self, amount):
        with self.mutex:
            self.value -= amount
    
    def getValue(self):
        return self.value