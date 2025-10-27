class Car:
    def specs() -> str:
        raise NotImplementedError()

class Bike:
    def specs() -> str:
        raise NotImplementedError()
    

# Economy Vehicles

class EconomyCar(Car):
    def specs(self) -> str: return "Economy car with 1.2L engine"

class EconomyBike(Bike):
    def specs(self): return "Economy Bike with 100cc engine"


# Sports Vehicles

class SportsCar(Car):
    def specs(self): return "Sports Car with V8 engine"

class SportsBike(Bike):
    def specs(self): return "Sports Bike with 600cc engine"
