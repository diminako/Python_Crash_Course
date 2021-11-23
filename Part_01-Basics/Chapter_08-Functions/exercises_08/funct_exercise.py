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

print(make_album('Jimi Hendrix', 'Purple haze', 5))
print(make_album('Gorillaz', 'Gorillaz'))
print(make_album('Eminem', 'Marshal Mathers LP', 12))

# Exercise 8-8 User Album - Start you program from exercise 8-7 write a while loop that allows users to enter an album's artist and title.  Once you have that information, call make_album() with the user;s input and print the dictionary that's created.  Be sure to include a quit value in the while loop.
active = True

while active:
    print("Enter the information below... or enter q to quit at any moment...")
    artist = input("Who is the artist? ")
    album = input("What is the album? ")
    tracks = input("How many tracks are on the album? ")
    if artist == 'q' or album == 'q' or tracks == 'q':
        break
    tracks = int(tracks)
    if artist != '' and album != '' and tracks != '':
        print(make_album(artist, album, tracks))
        active = False

# Exercise 8-9 Messages - Make a list containing short messages. pass the list to a function called show_messages().  print each message.
messages = ['lol', 'lmao', 'rofl', 'ttyl']

def show_messages(list):
    for item in list:
        print(item)

show_messages(messages)

# Exercise 8-10 Sending messages - start with a copy of exercise 8-9 write a function called send_messages() that prints each text message and moves each message to a new list called sent message as it's printed.  after the function print both lists to see what is in them.
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"sending text: {current_message}")
        sent_messages.append(current_message)

def show_messages(list):
    for item in list:
        print(item)

messages = ['lol', 'lmao', 'rofl', 'ttyl']
sent_messages = []

send_messages(messages, sent_messages)
show_messages(sent_messages)

print(messages)
print(sent_messages)

# Exercise 8-11 Archived Messages - Start with your work from Exercise 8-10.  call the function send_messages() with a copy of the list of messages.  print the lists to check if it worked correctly.
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"sending text: {current_message}")
        sent_messages.append(current_message)

def show_messages(list):
    for item in list:
        print(item)

messages = ['lol', 'lmao', 'rofl', 'ttyl']
sent_messages = []

send_messages(messages[:], sent_messages)
show_messages(sent_messages)

print(messages)
print(sent_messages)