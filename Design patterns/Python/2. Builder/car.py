from dataclasses import dataclass
from typing import List, Tuple

@dataclass(frozen=True, slots=True)
class Car:
    type: str
    color: str
    engine: str
    transmission: str
    sunroof: bool = False
    features: Tuple[str, ...] = ()