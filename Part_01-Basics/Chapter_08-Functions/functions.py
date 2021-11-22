# Functions
def greet_user():
    '''Display a simple greeting'''
    print('Hello!')

greet_user()

# Passing information to a function 
def greet_user(username):
    '''Display a simple greeting'''
    print(f"Hello, {username.title()}.")

greet_user("Dimitri")

# Passing arguments
def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')  # Order matters in positional arguments.
describe_pet('dog', 'tunde')  # Order matters in positional arguments.

# Keyword arguments - name value pair that you pass into a function
def describe_pet(animal_type, pet_name):
    '''Display information about a pet.'''
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='giraffe', pet_name='harry')  # Order matters in positional arguments.
describe_pet(animal_type='donkey', pet_name='shrek')  # Order matters in positional arguments.

