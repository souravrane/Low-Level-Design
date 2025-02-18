from abc import ABC, abstractmethod
from birdType import BirdType
from color import Color
from size import Size

class Bird:
    def __init__(self, name: str, weight: int, color: Color, size: Size, birdType: BirdType) -> None:
        self.__name = name
        self.__birdType = birdType
        self.__color = color
        self.__size = size

    def eat(self):
        print(f"{self.__name} the {self.__birdType} is eating.")