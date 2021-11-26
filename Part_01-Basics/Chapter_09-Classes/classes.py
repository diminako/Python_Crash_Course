# Creating and using a Class
# creating the dog class

class Dog:
    '''A simple attempt to model a dog.'''
    def __init__(self, name, age):
        '''initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''simulate a dog sitting in a response to a command.'''
        print(f'{self.name} is now sitting.')

    def roll_over(self):
        '''simulate a dog rolling over in response toa command.'''
        print(f'{self.name} rolled over!')

# Making an instance from a class
my_dog = Dog('Tunde', 4)

print(f'My dog\'s name is {my_dog.name.title()}')
print(f'My dog is {my_dog.age} years old.')
my_dog.sit()
my_dog.roll_over()

# creating multiple instances using the original Dog class
charlies_dog = Dog('snoopy', 7)
emilys_dog = Dog('shelly', 15)

print(f'Emily\'s dog is named {emilys_dog.name.title()}.  {emilys_dog.name.title()} was {emilys_dog.age} years old.')
print(f'Charley Brown has a famous dog named {charlies_dog.name.title()}.')
charlies_dog.sit()
emilys_dog.sit()
my_dog.sit()
print('Good dogies!')

# Working with classes and instances
# the car class
class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

# Setting a default value for an attribute
class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car\'s mileage.'''
        print(f'This car has {self.odometer_reading} miles on it.')

your_car = Car('audi', 'a4', 2019)
print(your_car.get_descriptive_name())
your_car.read_odometer()

# Modifying an attribute value

# Modifying an attribute directly...
your_car.odometer_reading = 50
your_car.read_odometer()

# Modifying an attribute's value through a method.
class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car\'s mileage.'''
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value.'''
        self.odometer_reading = mileage

dimis_car = Car('toyota', 'tacoma', 2021)
print(dimis_car.get_descriptive_name())
dimis_car.update_odometer(115)
dimis_car.read_odometer()

# Added instruction onto the method.
class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''Return a neatly formatted descriptive name.'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        '''Print a statement showing the car\'s mileage.'''
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        '''Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

dimis_car = Car('toyota', 'tacoma', 2021)
print(dimis_car.get_descriptive_name())
dimis_car.update_odometer(115)
dimis_car.read_odometer()

# increment an Attribute's value through a method.