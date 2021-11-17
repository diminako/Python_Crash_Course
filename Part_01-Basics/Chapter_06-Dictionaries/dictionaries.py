# Dictionaries
alien_0 = {
    "color": 'green',
    'points': 5
}
print(alien_0['color'])
print(alien_0['points'])

# Dictionaries are key value pair variables.
alien_1 = {
    'color': 'red',
    'points': 10
}
print(alien_1['points'])

red_points = alien_1['points']
print(f"You just earned {red_points} points!")

# Adding new key-value pairs 
alien_0['position_x'] = 0
alien_0['position_y'] = 25
print(alien_0)

# Modifying values
alien_0['color'] = 'yellow'
print(alien_0['color'])

# Tracking values
alien_0 = {
    'x_position': 0,
    'y_position': 25,
    'speed': 'medium'
}
print(f"Original X position: {alien_0['x_position']}")
# print(f"Original Y position: {alien_0['y_position']}")

#  Move the alien to the right
#  Determine how far to more the alin based on it's current speed
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'New position: {alien_0["x_position"]}')

# Removing key-value pairs.
alien_0 = {
    'color': 'green',
    'points': 5
}

del alien_0['points']
print(alien_0)
alien_0['points'] = 5
print(alien_0)

# A dictionary of similar objects.
favorite_languages = {
    'dimitri': 'javascript',
    'emily': 'ruby',
    'john': 'c',
    'brian': 'sql',
}

language = favorite_languages['dimitri'].title()
print(f"Dimitri's favorite language is: {language}")

# using get() to Access Values (helps prevent error messages by providing a backup value if no value is assigned for that key)
print(favorite_languages.get('dimitri', "No value assigned"))
print(favorite_languages.get('edward', "No value assigned"))
print(favorite_languages.get('edward')) #  Not assigning a value to the backup value with return None "No value exists"


# looping through a dictionary

# looping through all key-value pairs
user_0 = {
    'name': 'diminako',
    'first': 'dimitri',
    'last': 'nakos',
}
print(user_0.items()) # prints out the items(key and values) inside a dictionary.

for key, value in user_0.items():
    print(key, value)

for person, favorite in favorite_languages.items():
    print(f"{person.title()} loves using {favorite.title()} to code in.")

# looping through all keys in a dictionary
for name in favorite_languages.keys(): # loop through keys
    print(name.title())
for name in favorite_languages.values(): # loop through values
    print(name.title())

# looping and finding associated elements in a dictionary and a list
favorite_languages = {
    'dimitri': 'javascript',
    'emily': 'ruby',
    'john': 'c',
    'brian': 'sql',
}
friends = ['dimitri', 'john']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you like {language}!  Cool!")

if 'erin' not in favorite_languages.keys():
    print('Erin please take our poll.')

# Looping through a Dictionary's keys in a particular order.
cars = {
    'vw': 'tiguan',
    'dodge': 'ram',
    'toyota': 'tundra',
    'bmw': 'm3',
}

for manufacturer in sorted(cars.keys()): # Sorts the dictionary before performing the loop. doesn't save it that way.
    print(f"{manufacturer.title()}")
print(cars.keys())

# looping through values in a dictionary
print("These are the selection of cars for today.")
for car in cars.values():
    print(car.title())
print('I want those in alphabetical order tho!')
for car in sorted(cars.values()):
    print(car.title())

fav_languages = {
    'dimitri': 'python',
    'brian': 'java',
    'john': 'python',
    'emiy': 'java',
    'ronnie': 'ruby',
    'ronnie': 'ruby',
}
print("These languages were mentioned.  Some more than once.")
for lang in set(fav_languages.values()):
    print(lang)

# Sets are similar to dicts but they have no value.  and will only display multiples of the same elemets once.
this_set_not_dict = {'python', 'ruby', 'python', 'python'}
print(this_set_not_dict)
