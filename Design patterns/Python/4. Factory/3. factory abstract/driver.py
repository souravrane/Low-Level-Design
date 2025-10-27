from abstract_factory import EconomyVehicleFactory, SportsVehicleFactor, VehicleFactory

def get_factory(type: str) -> VehicleFactory:
    factory_map = {
        "economy": EconomyVehicleFactory(),
        "sports" : SportsVehicleFactor()
    }

    try:
        return factory_map[type]
    except:
        raise ValueError(f"Unknown family {type}")

def main():
    # user can change this to economy sports or any other factory type.
    family_type = "economy"

    factory = get_factory(family_type)

    car = factory.create_car()
    bike = factory.create_bike()

    print(car.specs())
    print(bike.specs())

main()