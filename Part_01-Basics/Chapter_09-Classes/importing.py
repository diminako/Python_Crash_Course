# Importing Classes
# importing a single class.
'''Import a class from another file.'''
from base_car import Car

dimi_car = Car('toyota', 'tacoma', 2021)
print(dimi_car.get_descriptive_name())

dimi_car.odometer_reading = 80
dimi_car.read_odometer()

# Storing multiple classes in a module.
