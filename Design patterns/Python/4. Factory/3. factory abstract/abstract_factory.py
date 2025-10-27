from abc import ABC, abstractmethod
from vehicle import EconomyBike, EconomyCar, SportsBike, SportsCar, Car, Bike

# Abstract factory
class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car: ...

    @abstractmethod
    def create_bike(self) -> Bike: ...


# Concrete factories

class EconomyVehicleFactory(VehicleFactory):
    def create_car(self) -> Car: return EconomyCar()
    
    def create_bike(self) -> Bike: return EconomyBike()


class SportsVehicleFactor(VehicleFactory):
    def create_car(self): return SportsCar()

    def create_bike(self): return SportsBike()