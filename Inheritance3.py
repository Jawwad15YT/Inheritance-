class Car:
    def __init__(self, Price, Speed):
        self.Price = Price
        self.Speed = Speed

    def Move(self):
        print("The car is currently moving.")

class Truck(Car):
    pass

Bespoke = Truck("5lakhs", "66mph")

Bespoke.Move()
