# Inheritance
# The __initi__() method for a child class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling the gas tank.")

'''creating a child of Car parent class'''
class Electric(Car):
    '''Represent aspects of a car, specific to electric vehicles.'''

    def __init__(self, make, model, year):
        '''Initialize the attributes of the parent class.'''
        super().__init__(make, model, year)
# Defining Attributes and Methods for the child class.
        '''Add attributes specific to this child class.'''
        self.batter_size = 75

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.batter_size}-kWh battery.')

    def charge_battery(self):
        print("Charging the electric battery.")

# Overiding Methods from the Parent Class
    def fill_gas_tank(self):
        print("This vehicle has no gas tank.")
        self.charge_battery()


my_tesla = Electric('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

# Instances as Attributes.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling the gas tank.")

# Defining an attribute Instance
class Battery:
    '''A simple attempt to model a battery for an electric car.'''
    def __init__(self, battery_size=75):
        '''Initialize the battery's attributes.'''
        self.battery_size = battery_size

    def describe_battery(self):
        '''Print a statement describing the battery size.'''
        print(f'This car has a {self.battery_size}-kWh battery.')

    def charge_battery(self):
        print("Charging the electric battery.")

    def fill_gas_tank(self):
        print("This vehicle has no gas tank.")
        self.charge_battery()
    
    def get_range(self):
        '''Print a statement about the range this battery provides.'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')
# End of defining an attribute Instance

class Electric(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


dimis_tesla = Electric('tesla', 'model s', 2019)

print(dimis_tesla.get_descriptive_name())
dimis_tesla.battery.describe_battery()
dimis_tesla.battery.fill_gas_tank()
dimis_tesla.battery.get_range()
