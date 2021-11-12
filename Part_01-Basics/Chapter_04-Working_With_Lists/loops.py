# for loops
magicians = ["David", "Dimitri", "John Chi"]
for magician in magicians:
    print(magician)

for i in magicians:
    print(f"{i.upper()}, Wow!  Your really are magic!\n")

for i in magicians:
    print(f"{i}, That was a great trick!")
    print(f"I can't wait to see your next trick {i}.\n")

# This is where indentation starts becoming more and more important.
# Errors that you will see will look like:
# IndentationError: expected an indented block
# IndentationError: unexpected indent



# Numerical Lists

# range will loop through number but not create a List
for value in range(1,6):
    print(value) # gives you 1-5.  At 6 it stops before proceeding. 

# list() to turn range into a list.
numbers = list(range(1,6))
print(numbers) # creates a List of [1, 2, 3, 4, 5]

even_numbers = list(range(0, 51, 5))
print(even_numbers) # creates [0,5,10,15,20,25,30,35,40,45,50]

squares = [] # create an empty List
for value in range(1, 11): # loop through a range of 1-10
    square = value ** 2 # create a variable square and for each iteration of value save the squared value of it.
    squares.append(square) # append the squared value to the list
print(squares) # Print the newly made list.
# Same Code below...
squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

# Simple statistics with a list of numbers
digits = list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehension generates lists with patterned values
list_compre = [value**2 for value in range(1,11)]
print(list_compre)

# slicing a list
# slicing takes two parameters.  list[index you want to start at, the index you want to stop at before reaching.]
players = ["charles", "martina", "micheal", "florence", "eli"]
print(players[0:3]) # Starting at index 0 give me players 0, 1, 2 and STOPS before going onto the player at index 3.
print(players[2:4]) # Starts at index 2 and returns players in position 2 and 3 and stops before 4.

# If you omit the first value the slice will begin at the start of the List
print(players[:3])
# To include the rest of a list give the first index and leave the second value out.
print(players[3:])
# To print the last 3 players you can use syntax like this
print(players[-3:])

# Looping through a slice
cars = ["BMW", "VW", "Porsche", "Volvo", "Dodge", "Toyota", "Hyundai"]
print("Here are the cars I like.")
for car in cars[:3]:
    print(f"I really like {car}")

# Copying a slice
my_foods = ["pizza", "torta", "sandwich", "soda", "sub"]
friends_foods = my_foods[:] # without [:] these lists would not become two separate lists.  Instead friends_foods would keep my_foods values and add onto them no matter what.

print(my_foods)
print(friends_foods)

my_foods.append("beer")
friends_foods.append("cocktail")

print(my_foods)
print(friends_foods)

