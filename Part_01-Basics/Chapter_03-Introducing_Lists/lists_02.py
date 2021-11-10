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

