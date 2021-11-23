# Exercise 8-1 Message - write a funct called siplay_message() that prints one sentence telling everyone what you are learning about in this chapter.  call the function and make sure it displays correctly.
def display_message():
    print("Functions are a way to stor longer sections of code to re-use where you can pass different parameters.")

display_message()

# Exercise 8-2 Favorite Book - write a function favorite_book().  accepts a parameter "title" print a message with that parameter.
def favorite_book(title):
    print(f"my favorite book is {title.title()}.")

favorite_book('The Shining')

# Exercise 8-3 T-Shirt - write a funct make_shirt() pass size and text.  print a sentence saying the size and message on it.  use positional and keyword arguments.
def make_shirt(size, label):
    print(f"This shirt is a {size} with the slogan '{label}.'")

make_shirt('small', 'sick shirt')
make_shirt(size='medium', label="That's pretty neat.")

# Exercise 8-4 Large Shirts - modify the last exercise for a large shirt that says i love python.  a medium shirt that has a default message and a shirt of any size that has a diff message.
make_shirt(size="Large", label="I Love Python")
make_shirt("Large", label="sick shirt")
make_shirt(size="medium", label="That's Pretty Neat")

# Exercise 8-5 Cities - write a funct called describe_city() accepts a city and country.  print a sentence. give the country a default value.
def describe_city(city, country):
    print(f"{city.title()} is in {country.title()}")

describe_city('Athens', 'Greece')
describe_city('Thessaloniki', 'Greece')
describe_city('Charlotte', country='Greece')

# Exercise 8-6 City Name - make a function called city_country() that takes in the name of a city and its country.  The function should return a string formatted like this |"Santiago, Chile"|  Call your function with at least three city-country pairs, and print the values that are returned.
def city_country(city, country):
    location = f'{city.title()}, {country.title()}'
    return location

print(city_country('charlotte', 'USA'))
print(city_country('athens', 'greece'))
print(city_country('raleigh', 'USA'))

# Exercise 8-7 Album - write a function called make_album() that builds a dictionary describing a music album.  the function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.  Use the function to make three dictionaries representing different albums.  Print each return value to show that the dictionaries are storing the album information correctly.  Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album.  If calling line includes a value for the number of songs, add that value to the album's dictionary.  Make at least one new function call that includes the number of songs on an album.
def make_album(artist_name, album_title, tracks=None):
    if tracks:
        music_album = {'artist': artist_name, 'album': album_title, 'tracks': tracks}
    else:
        music_album = {'artist': artist_name, 'album': album_title}
    return music_album

print(make_album())
print(make_album())
print(make_album())
# Exercise 8-8 User Album - Start you program from exercise 8-7 write a while loop that allows users to enter an album's artist and title.  Once you have that information, call make_album() with the user;s input and print the dictionary that's created.  Be sure to include a quit value in the while loop.