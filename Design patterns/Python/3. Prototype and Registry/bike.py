from dataclasses import dataclass
from typing import List
import copy

@dataclass
class Bike:
    model: str
    color: str
    gears: int
    accessories: List[str]

    def clone(self) -> "Bike":
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (f"Bike: {self.color} {self.model} "
                f"{self.gears}-speed accessories={self.accessories}")