from swimmable import Swimmable
from bird import Bird
from color import Color
from birdType import BirdType
from size import Size

class Penguine(Bird, Swimmable):
    def __init__(self, name: str, weight: int, color: Color, size: Size) -> None:
        super().__init__(name, weight, color, size, BirdType.PENGUIN.value)
    
    def swim(self) -> None:
        print(f"Penguine {self._Bird__name} is swimming")
