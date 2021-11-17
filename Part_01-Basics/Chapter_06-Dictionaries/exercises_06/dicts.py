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

# Exercise 6-4 Glossary 2 - add 5 more key-value pairs to glossary find a way to loop through in a clean way.
glossary = {
    'variables': 'keyword for a stored value.',
    'lists': 'an array of elements stored in an order.',
    'boolean': 'a value of True or False.',
    'if/else': 'logic performed depending on a True of False statement.',
    'dictionary': 'a way to organize a key-value pair.',
    'set': 'a way to provide unique elements from duplicates.',
    'operators': 'are different ways to manipulate elements.',
    'values': 'are stored elements.',
    'keys': 'a type of variable holding a value.',
    'loops': 'a way process lists and dicts.',
}

print(f"These are key words in python and their meaning. Sorted alphabetically.")
for words, meaning in sorted(glossary.items()):
    print(f"{words}: {meaning}")
# Exercise 6-5 Rivers - make a dict containing three major rivers and the country they run through. example 'nile': 'egypt'
# loop making a sentence about each.  loop the name of each river. loop to print the country.
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'euphrates': 'greece',
    'mississippi': 'usa',
}
for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

# Exercise 6-6 Polling - use fav_langs and create a dict. make a list of people iin and not in fav_langs.  loop thru. If they
# have a fav lang print their fav lang if not print that they should take the poll.
fav_langs = {
    'dimitri': 'python',
    'john': 'javascript',
    'emily': 'english',
    'brian': 'mysql',
}
poll_people = ['ronnie', 'dimitri', 'john', 'josh', 'andrew']

for people in poll_people:
    if people in fav_langs.keys():
        print(f"Nice {people}, You like {fav_langs.get(people)}.")
    else:
        print(f"{people}, why haven't you taken the poll yet?")

# for people, langs in fav_langs.items():           # This method looped through the fav_langs dict and missed people in the poll list
#     if people in poll_people:
#         print(f"Nice {people}, You like {langs}.")
#     else:
#         print(f"{people}, why haven't you taken the poll yet?")