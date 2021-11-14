# Exercise 5-1 Conditional Tests - write some conditionals and print whether true or false.
car = "BMW"
car == "bmw"
print(car == "BMW")

candle = "wood wick"
candle == "woodwick"
candle == "WoodWick"
print(candle == "wood wick")


string_0 = "Hello"
string_0 == "Hello"
print(string_0 == "hello")
print(string_0 != "ello")
print(string_0.lower() == "hello")
print(1 <= 2 and 3 >= 3)

my_list = ["cars", "final fantasy", "surf"]
print("cars" in my_list and 3 == 3)
print("sports" in my_list)

# Exercise 5-3 Alien Colors #1 - imaging an alien shot down in a game.  Create a variable called alien_color and assign it a value
# "green", "red", or "yellow".  write an if statement to test if the aliens color is green.  if it is print that the player earned
# 5 points.  write a version that passes and one that fails
alien_color = "red"
if alien_color == "green":
    print("You earned 5 points!")
else:
    print("the alien is not green!")

# Exercise 5-4 Alien Colors #2 - choose a color like the previous exercise.  if the alien is green, print a statement that the
# earned 5 points for shooting the alien.  if not green statement that the player earned 10 points. write a version with if and
#  one with an else block.
if alien_color == "green":
    print("you earned 5 points.")
if alien_color is not "green":
    print("You earned 10 points.")

if alien_color is "red":
    print("Grats you earned 20 points")
else:
    print("Game Over!")

# Exercise 5-5 Alien Colors #3 - turn ur if-else chain to an if-elif-else chain.  if green player earns 5 points.  if yellow
# player earns 10 points.  if red player earns 15 points.  
if alien_color is "green":
    print("You earned 5 points.")
elif alien_color is "yellow":
    print("You earned 10 points.")
else:
    print("You earned 15 points!")

# Exercise 5-6 Stages of Life - write an if-elif-else chain.  for a persons stages of life.set age and then test if person is < 2
# they are a baby. =2 <4 toddler. =4 <13 kid. =13 <20 a teenager. =20 <65 adult. >=65 elder.
age = 67
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >=13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are an adult.")
else:
    print("You are an elder.")

# Exercise 5-7 Favorite Fruit - make a list of favorite fruits write if statesments that check for fruits in list.
# five if statements that check whether a certain kind of fruit is in your list.  if fruit is in list print(you really like {fruit})
fruits = ["banana", "strawberry", "orange", "apple", "cherry"]

if "banana" in fruits:
    print("You really like bananas!")
if "strawberry" in fruits:
    print("You really like strawberries!")
if "tomatoe" not in fruits:
    print("Tomatoes aren't fruits anyway.")
if "orange" in fruits:
    print("You really like oranges.")
if "apple" in fruits:
    print("Apples are delicious.")
if "cherry" in fruits:
    print("Cherry pie is awesome.")

# Exercise 5-8 Hello Admin - 
# Exercise 5-9 No Users -
# Exercise 5-10 Checking Usernames -
# Exercise 5-11 Ordinal Numbers - 