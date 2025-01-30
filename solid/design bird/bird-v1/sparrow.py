from bird import Bird
from birdType import BirdType
from color import Color
from size import Size

class Sparrow(Bird):
    def __init__(self, name: str, weight: int, color: Color, size: Size) -> None:
        super().__init__(name, weight, color, size, BirdType.SPARROW)
    
    def fly(self) -> None:
        print(f"Sparrow {self._Bird__name} is flying")