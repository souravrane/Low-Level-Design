from eagle import Eagle
from sparrow import Sparrow
from color import Color
from size import Size

if __name__ == "__main__":
    sparrow = Sparrow("Jackie", 10, Color.BLUE, Size.SMALL)
    sparrow.fly()
    eagle = Eagle("Henry", 20, Color.WHITE, Size.LARGE)
    eagle.fly()
