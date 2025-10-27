from car import Car

class CarFactory:
    """Simple Factory to create Car objects based on type."""

    @staticmethod
    def create_car(car_type) -> Car:
        car_type = car_type.lower()

        if car_type == "suv":
            return Car("SUV", engine="Hybrid", transmission="Automatic")
        
        elif car_type == "sedan":
            return Car("Sedan", engine="Petrol", transmission="Automatic")
        
        elif car_type == "coupe":
            return Car("Coupe", engine="Electric", transmission="Automatic")
        
        else:
            return ValueError(f"Unknown car type {car_type}")