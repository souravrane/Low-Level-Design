from bird import Bird
from birdType import BirdType
from color import Color
from size import Size

class Eagle(Bird):
    def __init__(self, name: str, weight: int, color: Color, size: Size) -> None:
        super().__init__(name, weight, color, size, BirdType.EAGLE)
    
    def fly(self) -> None:
        print(f"Eagle {self._Bird__name} is flying")