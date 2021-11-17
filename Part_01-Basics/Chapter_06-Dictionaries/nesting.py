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

