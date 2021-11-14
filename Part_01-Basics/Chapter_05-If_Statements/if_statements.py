# If Statements
cars = ["audi", "bmw", "mercedes", "Volkswagen"]
for car in cars:
    if (car == "bmw"):
        print(car.upper())
    else:
        print(car.title())

car = "bmw"
# car == "bmw"  # True
# car == "audi". # False

# car = "audi"
# car == "Audi"  # False due to the upper case letter
# car.title() == "Audi". # True because it's checking against the same case.

# Checking for inequality
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Numerical comparisons
age = 18
age == 18 #  True

answer = 17
if answer != 42:
    print("That is not the correct answer.  Please try again!")

age = 19
age < 21  # True
age <= 21  # True
age > 21  # False
age >= 21  # False

# Checking multiple conditions
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21  # False
age_1 = 22
age_0 >= 21 and age_1 >= 21  # True
# (age_0 >= 21) and (age_1 >= 21)

# Checking whether a value is in a list
requested_topping = ["mushrooms", "onions", "pineapple"]
"mushrooms" in requested_topping  # True
"pepperoni" in requested_topping  # False

# Checking if a value is not in a list
banned_users = ["andrew", "carolina", "david"]
user = "marie"
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Boolean Expressions
game_active = True
can_edit = False

# if Statements
conditional_test = True
if conditional_test:
    print(conditional_test)

age = 19
if age >= 18:
    print("You are old enough to vote!")

# if/else statements
age = 17
if age >= 18:
    print("You should go vote!")
else:
    print("Grow up.")

# if-elif-else chain
age = 5
if age < 4:
    print("admission is free.")
elif age < 13:
    print("young children get a discount")
else:
    print("Pay up.")

if age < 4:
    price = 0
elif age < 13:
    price = 10
else:
    price = 20
print(f"Your cost for admission is {price}")

# Multiple elif blocks
cars = ["bmw", "mercedes", "honda", "toyota", "chevy"]

if "hevy" in cars:
    print(f"that there's a {cars[-1]}.")
elif "mw" in cars:
    print(f"I dunno what that is but it aint no BMW")
elif "mercedes" in cars:
    print("neat")
else:
    print("word yeah")

# else blocks aren't required.  you can omit an else block if you don't want the program to react.
if "bmw" not in cars:
    print("It should be doe")

# Testing Multiple Conditions.
requested_topping = ["mushrooms", "extra cheese"]

if "mushrooms" in requested_topping:
    print("adding mushrooms.")
if "perpperoni" in requested_topping:
    print("adding pepperoni.")
if "extra cheese" in requested_topping:
    print("adding extra cheese.")

print("\nFinished making your pizza!")

