# Base class
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self):
        return self.rental_rate 


# Car subclass
class Car(Vehicle):
    def __init__(self, model, rental_rate, days):
        super().__init__(model, rental_rate)
        self.days = days

    def calculate_rental(self):
        return self.rental_rate * self.days


# Bike subclass
class Bike(Vehicle):
    def __init__(self, model, rental_rate, hours):
        super().__init__(model, rental_rate)
        self.hours = hours

    def calculate_rental(self):
        return self.rental_rate * self.hours


# Truck subclass
class Truck(Vehicle):
    def __init__(self, model, rental_rate, days, load):
        super().__init__(model, rental_rate)
        self.days = days
        self.load = load  # e.g., in tons

    def calculate_rental(self):
        load_charge = 500  # charge per ton
        return (self.rental_rate * self.days) + (load_charge * self.load)
