# Nesting
# List of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens
aliens = []

# Make 10 green aliens
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# print the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens there are.
print(f'Total number of aliens: {len(aliens)}')

# alter the fir 3 aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]:
    print(alien)
print('...')

# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza. With the following toppings:")
for topping in pizza['toppings']:
    print(f'\t{topping}')


fav_langs = {
    'john': ['python', 'ruby'],
    'dimitri': ['python'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
}
for name, langs in fav_langs.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for lang in langs:
        print(f"\t{lang.title()}")

# A dictionary in a dictionary
users = {
    'dnakos': {
        'first': 'dimitri',
        'last': 'nakos',
        'location': 'charlotte',
    },
    'jchi': {
        'first': 'john',
        'last': 'chi',
        'location': 'monroe',
    }
}

for username, user_info in users.items():
    print(f"\nUsername:  {username}")
    full_name = (f"{user_info['first']} {user_info['last']}")
    location = user_info['location']

    print(f"\tFull nume:  {full_name.title()}")
    print(f"\tLocation:  {location.title()}")

