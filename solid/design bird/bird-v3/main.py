from eagle import Eagle
from penguine import Penguine
from sparrow import Sparrow
from color import Color
from size import Size
from birdType import BirdType
from flyable import Flyable

def flyall(birds : list[Flyable]):
    for bird in birds:
        bird.fly()

if __name__ == "__main__":
    penguine = Penguine("Jackie", 10, Color.BLUE, Size.SMALL)
    eagle = Eagle("Henry", 20, Color.WHITE, Size.LARGE)
    eagle.fly()
    eagle.eat()
    penguine.swim()
    penguine.eat()

    sparrow = Sparrow("Chew Tai", 5, Color.YELLOW, Size.SMALL)
    flyall([eagle, sparrow])

