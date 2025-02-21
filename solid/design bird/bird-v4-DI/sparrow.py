from flyable import Flyable
from bird import Bird
from color import Color
from birdType import BirdType
from size import Size
from beak import Beak

class Sparrow(Bird, Flyable):
    def __init__(self, name: str, weight: int, color: Color, size: Size, beak: Beak) -> None:
        super().__init__(name, weight, color, size, BirdType.SPARROW.value, beak)
    
    def fly(self) -> None:
        print(f"Sparrow {self._Bird__name} is flying")