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
print(f"Original Y position: {alien_0['y_position']}")

#  Move the alien to the right
#  Determine how far to more the alin based on it's current speed
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

