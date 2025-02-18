from bird import Bird
from abc import ABC, abstractmethod
from color import Color
from size import Size
from birdType import BirdType

class FlyableBird(Bird, ABC):
    def __init__(self, name: str, weight: int, color: Color, size: Size, birdType: BirdType):
        super().__init__(name, weight, color, size, birdType)

    @abstractmethod
    def fly(self) -> None: pass