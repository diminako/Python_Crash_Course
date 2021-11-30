# Importing Classes
# importing a single class.
'''Import a class from another file.'''
from base_car import Car

dimi_car = Car('toyota', 'tacoma', 2021)
print(dimi_car.get_descriptive_name())

dimi_car.odometer_reading = 80
dimi_car.read_odometer()

# Storing multiple classes in a module.  and importing multiple classes from a module.
from base_car import Battery, Electric
my_tesla = Electric('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# Importing an Entire module
import base_car
my_beetle = base_car.Car('Volkswagen', 'beetle', 1974)
dimis_tesla = base_car.Electric('tesla', 'model s', 2019)
print(my_beetle.get_descriptive_name())
print(dimis_tesla.get_descriptive_name())

# Importing all classes from a module.
from base_car import *

# Using aliases
from base_car import Car as CarBuild
from base_car import Electric as EVBuild

