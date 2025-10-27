from car_factory import CarFactory

def main():
    car1 = CarFactory.create_car("suv")
    car2 = CarFactory.create_car("sedan")
    car3 = CarFactory.create_car("coupe")

    print(car1)
    print(car2)
    print(car3)



if __name__ == "__main__":
    main()