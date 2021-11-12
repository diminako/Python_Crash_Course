# Tuples are immutable lists. aka Lists that can't be changed.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[1] = 100 # TypeError: 'tuple' object does not support item assignment
my_tuple = (3,)
print(my_tuple)
# my_tuple.append(5) # You are't allowed to append onto a tuple AttributeError: 'tuple' object has no attribute 'append'
print(my_tuple)

for dime in dimensions:
    print(dime)

# Modify a tuple - you can change the whole tuple itself but not the elements of it.
my_tuple = (3, 5)
print("Modifies my_tuple:")
print(my_tuple)