class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)



# ✅ Why use super().__init__(make, model, year)?

# You're inside the ElectricCar class, which inherits from Car.

# But Car has its own constructor (__init__) that sets up:

#     self.make

#     self.model

#     self.year

#     self.odometer_reading

# If you don’t call that constructor, the base class (Car) doesn't get 
# initialized — and those attributes won't exist in your ElectricCar object.

# 🔬 super() means:

#     “Get the parent class (Car) and run its methods.”

# So:

# super().__init__(make, model, year)

# s the same as saying:

# Car.__init__(self, make, model, year)









my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
