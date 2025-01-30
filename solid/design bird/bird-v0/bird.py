from birdType import BirdType
from color import Color
from size import Size

class Bird:
    def __init__(self, name: str, weight: int, color: Color, size: Size, birdType: BirdType) -> None:
        self.__name = name
        self.__birdType = birdType
        self.__color = color
        self.__size = size
    
    '''
    Issue : Fly method does not account for all birds, because not all birds can fly.
    '''
    def fly(self) -> None:
        if(self.__birdType == BirdType.PENGUIN):
            print("Penguins can't fly")
        elif(self.__birdType == BirdType.SPARROW):
            print("Sparrow is flying")
        # and so on...

    def eat(self) -> None:
        pass

    def sleep(self) -> None:
        pass 