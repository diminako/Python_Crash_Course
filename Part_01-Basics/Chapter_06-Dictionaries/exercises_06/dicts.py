# Dictionaries exercises

# Exercise 6-1 Person - Use a dictionary to store information about a person you know.  first, last names, age, city print each.
person = {
    'first_name': 'dimitri',
    'last_name': 'nakos',
    'age': 36,
    'city': 'charlotte',
}
print(person.get('first_name'))
print(person.get('last_name'))
print(person.get('age'))
print(person.get('city'))

for val in person:
    print(person.get(val))

# Exercise 6-2 Favorite Numbers - use a dict to store people's fav nums 5 names. print their names and the values.
fav_numbers = {
    'dimitri': 7,
    'ronnie': 18,
    'brian': 100,
    'john': 3,
    'emily': 12
}
for fav in fav_numbers:
    print(f"{fav.title()}'s favorite number is : {fav_numbers.get(fav)}")

# Exercise 6-3 Glossary - a dict can model an actual dictionary, or a glossary.  think of 5 programming words use these as keys
# store their meanings as values.  print each word and it's meaning as a neatly formatted output.
glossary = {
    'variables': 'keyword for a stored value.',
    'lists': 'an array of elements stored in an order.',
    'boolean': 'a value of True or False.',
    'if/else': 'logic performed depending on a True of False statement.',
    'dictionary': 'a way to organize a key-value pair.',
}

for key in glossary:
    print(f"a(n) {key} is {glossary.get(key)}")
