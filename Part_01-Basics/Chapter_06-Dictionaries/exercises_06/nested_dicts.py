# Exercise 6-7 People - use exercise 6-1.  make 2 new dicts representing diff people. store all 3 in a list.  loop thru list
# as you loop thrugh print everything you know about them.
people_list = [
    {
    'first_name': 'dimitri',
    'last_name': 'nakos',
    'age': 36,
    'city': 'charlotte',
}, {
    'first_name': 'emily',
    'last_name': 'pruitt',
    'age': 32,
    'city': 'oxford',

}, {
    'first_name': 'john',
    'last_name': 'chi',
    'age': 35,
    'city': 'chicago',
},
]
for people in people_list:
    for people_info in people.keys():
        print(f"{people_info}:  {people[people_info]}")

# Exercise 6-8 Pets - make several dictionaries of pets. include animal, owner. sotre in a list called pets. loop thru list
# and print each thing you know about them.
pets = [
    {
        'animal': 'dog',
        'pet_name': 'tunde',
        'owner_name': 'dimitri,'
    }, {

        'animal': 'cat',
        'pet_name': 'who cares its a cat',
        'owner_name': 'someone that owns cats',
    }, {
        'animal': 'tiger',
        'pet_name': 'butch',
        'owner_name': 'mike',
    },
]
for pet in pets:
    if len(pet.get('pet_name')) > 10:
        print(f"{pet.get('owner_name').capitalize()} has a {pet.get('animal')} named {pet.get('pet_name')}.")
    else:
        print(f"{pet.get('owner_name').title()} has a {pet.get('animal')} named {pet.get('pet_name').title()}.")

# Exercise 6-9 Favorite Places - make a dict called faorite_places. store a name to a place. 3 of them loop through and print.
favorite_places = {
    'dimitri': 'greece',
    'emily': 'charlotte',
    'john': 'home',
}
for people, favs in favorite_places.items():
    print(f"{people.title()}'s favorite place is {favs.title()}.")

# Exercise 6-10 Favorite Numbers - make a dict of people with the value as their fav numbers(lists) print them along with their nums
favorite_numbers = {
    'dimitri': [7, 3],
    'sabin': [5],
    'ronnie': [10, 15],
    'john': [1, 3, 3, 7],
    'brian': [100],
    'emily': [12]
}
for person, nums in favorite_numbers.items():
    print(f"{person.title()}'s favorite num(s) are: ")
    for num in nums:
        print(f"\t{num}")

# Exercise 6-11 Cities - make a dict cities. three different cities as keys. country, pop, and a fact. print all the info.
cities = {
    'charlotte': {
        'country': 'usa',
        'population': 2_000_000,
        'fact': "it sucks",
    },
    'athens': {
        'country': 'greece',
        'population': 7_000_000,
        'fact': "it's legit.'",
    },
    'chicago': {
        'country': 'usa',
        'population': 4_000_000,
        'fact': "it's cold'",
    },
}
for city, city_info in cities.items():
    print(f"{city.title()} is in {city_info.get('country')}.  It has a population of {city_info.get('population')} and {city_info.get('fact')}.")
# Exercise 6-12