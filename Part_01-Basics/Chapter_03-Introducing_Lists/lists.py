# Lists are variables containing an ordered list of values.  They are represented with [ ] square brackets.
bicycles = ["trek", "cannondale", "redline", "speialized"]
print(bicycles) # this return the list as it's information form.
# ["trek", "cannondale", "redline", "speialized"]

# Accessing elements in a List
print(bicycles[0]) # prints "trek"

print(bicycles[0].title()) # prints "Trek"

# Index starts at position 0, Not 1
bicycles = ["trek", "cannondale", "redline", "speialized"]
print(bicycles[1])
print(bicycles[3])

# Python has special syntax for getting the last element of a List [-1]
print(bicycles[-1]) # prints "speialized"
print(bicycles[-2]) # prints "redline"

# Using individual values from Lists
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)


# Changing, Adding, and removing Elements in a List
# Changing elements by index
motorcyles = ["Honda", "Suzuki", "Ducati"]
print(motorcyles)

motorcyles(0) = "Yamaha"
print(motorcyles)

# Adding Elements to a list
motorcyles.append("Harley") # Appending adds the new element to the end of the list.
print(motorcyles)

motorcyles = []
print(motorcyles)
motorcyles.append("Honda")
motorcyles.append("Ducati")
motorcyles.append("Suzuki")
motorcyles.append("Yamah")
print(motorcyles)

# Insert elements into an index of a list and shift the rest of the elements to a new index.
motorcyles.insert(1, "Indian")
print(motorcyles)

# Removing Elements from a list. del permanently removes that value.
print(motorcyles)
del motorcyles(2)
print(motorcyles)

# Removing an Item using pop() Method.  Allows you to reassign that value to a new variable.
cars = ["VW", "Honda", "Toyota", "BMW", "Mercedes"]
print(cars)

popped_car = cars.pop()
print(cars)
print(popped_car)

# pop() can also include the index you wish to use.
cars.append(popped_car)
popped_car = cars.pop(1)
print(f"I'm not a fan of {popped_car}")
cars.append(popped_car)

# Removing an Item by Value
print(cars)
cars.remove("Honda")
print(cars)

cars.append(popped_car)

too_ugly = "Honda"
cars.remove(too_ugly)
print(cars)
print(f"\n {too_ugly} is too ugly of a car for me")



