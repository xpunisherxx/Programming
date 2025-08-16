"""This will be used later in the class"""
class Car:
    """A simple attempt to represent a car."""

    def __init__(self ,make ,model ,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        pass

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name= f"{self.year} {self.make} {self.model}"
        return long_name
    
    def read_odometer(self):
        """print a statement showing the cars mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self ,mileage):
        """
        Set the odometer reading to the given value
        reject the change if it agin tries to roll back the counter
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer")

    def increment_odometer(self ,miles):
        """Add the given amount of the odometer reaing """
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """These cars have gas tanks."""
        print("These cars does need a gas tank!")




class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self ,battery_size = 75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery")
        pass

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about the {range} miles on a full charge.")

class ElectricCar(Car):
    """Represent aspects of a car ,specific to electric vehicles."""

    def __init__(self ,make ,model ,year):
        """initializing the attributes of the parents class and then initialise
           attributes specific to an electric car
        """
        super().__init__(make ,model ,year)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")





# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


my_tesla = ElectricCar('tesla' ,"model's" ,2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
# is a special function that allows you to call
# a method from the parent class. This line tells Python to call the __init__()
# method from Car, which gives an ElectricCar instance all 
# the attributes
# defined in that method. The name super comes from a 
# convention of calling the parent class a superclass and the child class a subclass