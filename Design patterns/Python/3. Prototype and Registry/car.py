from dataclasses import dataclass
from typing import List
import copy

@dataclass
class Car:
    type: str
    color: str
    engine: str
    transmission: str
    features: List[str]

    def clone(self) -> "Car":
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return (f"Car: {self.color} {self.type} "
                f"({self.engine}, {self.transmission}) "
                f"features={self.features}")