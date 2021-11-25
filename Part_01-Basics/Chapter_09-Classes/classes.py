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