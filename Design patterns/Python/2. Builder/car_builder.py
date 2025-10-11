from car import Car
from typing import List, Optional, Self

class CarBuilder:
    def __init__(self) -> None:
        self._type: Optional[str] = None
        self._color: Optional[str] = None
        self._engine: Optional[str] = None
        self._transmission: Optional[str] = None
        self._sunroof: bool = False
        self._features: List[str] = []


    # ---- Fluent setters ----
    def set_type(self, type_: str) -> Self:
        self._type = type_; return self

    def set_color(self, color: str) -> Self:
        self._color = color; return self

    def set_engine(self, engine: str) -> Self:
        self._engine = engine; return self

    def set_transmission(self, transmission: str) -> Self:
        self._transmission = transmission; return self

    def add_feature(self, *features: str) -> Self:
        self._features.extend(features); return self

    def add_sunroof(self) -> Self:
        self._sunroof = True; return self
    

    # ---- Build & validate ----
    def build(self) -> Car:
        missing = [k for k,v in {
            "type": self._type,
            "color": self._color,
            "engine": self._engine,
            "transmission": self._transmission
        }.items() if v is None]
        
        if missing: raise ValueError(f"Missing required fields : {','.join(missing)}")

        return Car(
            type=self._type,                
            color=self._color,              
            engine=self._engine,            
            transmission=self._transmission,
            sunroof=self._sunroof,
            features=tuple(self._features),
        )
    

def main():
    my_car = (CarBuilder()
              .set_color("Red")
              .set_type("Sedan")
              .set_transmission("Automatic")
              .set_engine("V8")
              .add_feature("Wireless radio", "Hybrid fuel")
              .add_sunroof()
              .build())

    print(my_car)

if __name__ == "__main__":
    main()