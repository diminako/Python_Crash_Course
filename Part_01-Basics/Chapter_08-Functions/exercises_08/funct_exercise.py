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
