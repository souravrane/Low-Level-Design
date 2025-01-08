from car import Car

if __name__ == "__main__":
    car1 = Car(1000, 200)
    car2 = Car(2000, 300)
    car3 = Car(1500, 250)
    car4 = Car(2500, 350)

    cars = [car3, car2, car1, car4]

    # Sorting the cars based on price
    cars.sort()
    print(cars)