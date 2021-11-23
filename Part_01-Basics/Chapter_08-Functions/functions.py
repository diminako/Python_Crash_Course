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

# Return values
# returning a simple value
def get_formatted_name(first_name, last_name):
    '''Return a full name, neatly formatted.'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# making an Argument optional
def get_formatted_name(first_name, middle_name, last_name):
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):  # The final parameter is optional so it has a value of an empty string.
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
musician = get_formatted_name('john', 'chi')
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age']= age
    return person

musician = build_person('jimi', 'hendrix', age=27)  #  You can pass the 3rd value without the 'age='
print(musician)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name

while True:
    print('\nPlease tell me your name:  ')
    print("(enter 'q' at any time to quit)")

    f_name = input('First Name: ')
    if f_name == 'q':
        break
    l_name = input('Last Name: ')
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

