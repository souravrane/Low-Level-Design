from abc import ABC, abstractmethod

class Beak(ABC):
    def __init__(self, strength, material):
        self.strength = strength
        self.material = material