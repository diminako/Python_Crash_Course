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

