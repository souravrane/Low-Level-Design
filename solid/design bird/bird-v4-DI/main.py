from eagle import Eagle
from penguine import Penguine
from sparrow import Sparrow
from color import Color
from size import Size
from birdType import BirdType
from flyable import Flyable
from strongBeak import StrongBeak
from weakBeak import weakBeak

def flyall(birds : list[Flyable]):
    for bird in birds:
        bird.fly()

if __name__ == "__main__":
    strongBeak = StrongBeak(10.0, "Calcium")
    eagle = Eagle("Henry", 20, Color.WHITE, Size.LARGE, strongBeak)

    weakBeak = weakBeak(2.0, "Paper")
    eagle = Eagle("Henry", 20, Color.WHITE, Size.LARGE, weakBeak)

    eagle.fly()
    eagle.eat()
    

    sparrow = Sparrow("Chew Tai", 5, Color.YELLOW, Size.SMALL, weakBeak)
    flyall([eagle, sparrow])

