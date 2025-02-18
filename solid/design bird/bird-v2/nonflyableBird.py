from abc import ABC
from bird import Bird

class NonflyableBird(ABC, Bird):
    def __init__(self, name, weight, color, size, birdType):
        super().__init__(name, weight, color, size, birdType)