# Organizing a List

# Sort() sorts Lists alphabetically permanentally
cars = ["Mercedes", "BMW", "Dodge", "VW", "Chrysler"]
cars.sort()
print(cars)

# sort(reverse=True) reverses the alphabetical order permanentally
cars.sort(reverse=True)
print(cars)

cars = ["Mercedes", "BMW", "Dodge", "VW", "Chrysler"]
# sorted() allows you to temporarily have a sorted list
print("Here is the original List")
print(cars)

print("Here is the sorted List")
print(sorted(cars))

print("Here is the original List again.")
print(cars)

# reverse() reverses the order of the List permanentally but can be reversed again by calling the action again.
print("Here is the reversed List")
cars.reverse()
print(cars)

print("Here is the original List again.")
cars.reverse()
print(cars)

# length of List
length_of_list = len(cars)
print(length_of_list)

