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



