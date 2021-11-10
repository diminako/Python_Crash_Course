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

