class Car:
    def __init__(self, price: int, speed: int):
        self.price = price;
        self.speed = speed;

    # Implementing the less-than (<) operator for sorting (Similar to Comparable in Java)
    def __lt__(self, other):
        if not isinstance(other, Car):
            raise TypeError(f"Cannot compare Car with {type(other)}")
        return self.price < other.price

    # String representation of the object (similar to toString() in Java)
    def __repr__(self):
        return f"Car(price={self.price}, speed={self.speed})"

    
