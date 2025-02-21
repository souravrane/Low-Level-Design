from abc import ABC, abstractmethod

class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass