from abc import ABC, abstractmethod
from birdType import BirdType
from color import Color
from size import Size
from beak import Beak

class Bird:
    def __init__(self, name: str, weight: int, color: Color, size: Size, birdType: BirdType, beak: Beak) -> None:
        self.__name = name
        self.__birdType = birdType
        self.__color = color
        self.__size = size
        self.__beak = beak

    def eat(self):
        print(f"{self.__name} the {self.__birdType} is eating.")