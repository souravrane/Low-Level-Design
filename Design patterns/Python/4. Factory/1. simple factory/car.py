from dataclasses import dataclass

@dataclass
class Car:
    type: str
    engine: str
    transmission: str

    def spec(self) -> str:
        return f"{self.type} with {self.engine} engine and {self.transmission} transmission"