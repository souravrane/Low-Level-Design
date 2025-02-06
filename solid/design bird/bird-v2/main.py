from bird import Bird
from eagle import Eagle
from penguine import Penguine
from color import Color
from size import Size

if __name__ == "__main__":
    penguine : Bird = Penguine("Jackie", 10, Color.BLUE, Size.SMALL)
    eagle : Bird = Eagle("Henry", 20, Color.WHITE, Size.LARGE)
    eagle.fly()
