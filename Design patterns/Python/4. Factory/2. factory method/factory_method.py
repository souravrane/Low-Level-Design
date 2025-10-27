from abc import ABC, abstractmethod
from car import Car, SUV, Sedan, Coupe

# Creator
class CarFactory(ABC):
    @abstractmethod
    def create_car(self) -> Car: ...

# Concrete Factories
class SUVFactory(CarFactory):
    def create_car(self) -> Car:
        return SUV()

class SedanFactory(CarFactory):
    def create_car(self) -> Car:
        return Sedan()

class CoupeFactory(CarFactory):
    def create_car(self) -> Car:
        return Coupe()