from car import Car
from bike import Bike
from registry import PrototypeRegistry

def main():
    registry = PrototypeRegistry()

    # Create base prototypes of different classes
    family_suv = Car(
        type="SUV", color="Black", engine="Hybrid", transmission="Automatic",
        features=["Sunroof", "ADAS"]
    )

    sports_coupe = Car(
        type="Coupe", color="Red", engine="V8", transmission="Manual",
        features=["Launch Control"]
    )

    city_bike = Bike(
        model="City", color="Blue", gears=7, accessories=["Bell", "Rack"]
    )

    mtb_bike = Bike(
        model="MTB", color="Green", gears=21, accessories=["Suspension", "Bottle Cage"]
    )



    # Register under keys (mixed types allowed)
    registry.register("family_suv", family_suv)
    registry.register("sports_coupe", sports_coupe)
    registry.register("city_bike", city_bike)
    registry.register("mtb_bike", mtb_bike)


    # clone + override at a later point
    suv_blue = registry.get("family_suv", color="Blue", features=["360 Camera"])
    coupe_auto = registry.get("sports_coupe", transmission="Automatic" )
    city_bike_red = registry.get("city_bike", color="Red", accessories=["Basket", "Bell"])
    mtb_1x12 = registry.get("mtb_bike", gears=12, accessories=["Dropper Post", "Tubeless Kit"])

    # --- Show results ---
    print("Originals:")
    print(family_suv)
    print(sports_coupe)
    print(city_bike)
    print(mtb_bike)

    print("\nClones:")
    print(suv_blue)
    print(coupe_auto)
    print(city_bike_red)
    print(mtb_1x12)


if __name__ == "__main__":
    main()