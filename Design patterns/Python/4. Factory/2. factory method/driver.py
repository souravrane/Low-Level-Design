from factory_method import SUVFactory, SedanFactory, CoupeFactory

def main():
    factories = [SUVFactory(), SedanFactory(), CoupeFactory()]

    for factory in factories:
        car = factory.create_car()
        print(car.specs())

main()