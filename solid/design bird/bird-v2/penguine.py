from nonflyableBird import NonflyableBird
from birdType import BirdType
from color import Color
from size import Size

class Penguine(NonflyableBird):
    def __init__(self, name: str, weight: int, color: Color, size: Size) -> None:
        super().__init__(name, weight, color, size, BirdType.PENGUIN)