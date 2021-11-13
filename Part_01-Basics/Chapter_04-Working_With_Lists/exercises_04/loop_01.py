# Exercise 4-1 Pizzas - make a loop to print a sentence about each pizza.  print a statement outside of the loop.
pizza = ["pepperoni", "Meatlovers", "Supreme"]
for za in pizza:
    print(f"I absolutely love {za} Pizza.")
print(f"I love all pizzas but I really love {pizza[0]} the best!")

print("---------------")
# Exercise 4-1 and 4-2 Animals - make a list of 3 animals that have common characteristics.  loop over and print their names.  modify it to a sentence.  add a line outside of the loop about their commonality.
animals = ["bear", "tiger", "zebra", "penguin"]
for animal in animals:
    print(animal)
for animal in animals:
    print(f"{animal}'s look so cool!")
print("All of these animals would not make great pets!")

print("---------------")
# Exercise 4-3 Count to Tweny - for loop to print 1-20
for value in range(1,21):
    print(value)

print("---------------")
# Exercise 4-4 One Million - Make a list from 1 - 100.  Not doing 1 mill just cause.
list_to_100 = list(range(0, 101, 5))
print(list_to_100)

print("---------------")
# Exercise 4-5 Summing a Million - sum to 1 mill and see the min and max to verify then sum the list
list_to_million = list(range(1,1000001))
print(min(list_to_million))
print(max(list_to_million))
print(sum(list_to_million))


print("---------------")
# Exercise 4-6 Odd Numbers - use the third argument in range to make a list of odd numbers 1-20. print them.
list_for_odds = list(range(1,21, 2))
print(list_for_odds)
for odd in list_for_odds:
    print(odd)

print("---------------")
# Exercise 4-7 Threes - Make a list of multiples of 3 from 3 to thirty use a for loop and print the numbers in your list.
multiples_of_three = list(range(1,31))
for threes in multiples_of_three:
    if(threes % 3 == 0):
        print(threes)

print("---------------")
# Exercise 4-8 Cubes - make a list of the cube of each 1-10.  print their values.
cubed_of_ten = list(range(1,11))
for each in cubed_of_ten:
    print(each**3)


print("---------------")
# Exercise 4-9 Cube Comprehension - use a list comprehenssion to create a list of the cubed values of 1-10
cubed_vals = [value**3 for value in range(1,11)]
print(cubed_vals)

# Exercise 4-10 Slices - make a list and print the first three Items "The first three items are:", print three middle items, and print the last three items.
new_list = ["ff3", "chrono trigger", "ff5", "tactics", "surfing", "dragoon", "black mage", "panthers"]
first_three = new_list[:3] # get the first 3 elements starting at default position 0
print(first_three)
find_middle = int(len(new_list) / 2 - 1) #find the length and get the middle index
middle_three = new_list[(find_middle - 1):(find_middle + 2)] # use that variable to get 3 elements
print(middle_three)
last_three = new_list[-3:]  # Get the starting variable by index position 3 from reverse till the end.
print(last_three)

# Exercise 4-11 My Pizzas, Your Pizzas - using 4-1 make a copy of the list of pizzas.  name it friends_pizzas.  Add a pizza to the oiginal list.  add a different pizza to the list friends_pizzas.  prove they are different. print them using for loops
friends_pizza = pizza[:]
pizza.append("veggie")
friends_pizza.append("eggplant")
for za in pizza:
    print(za)
print("---------------")
for za in friends_pizza:
    print(za)

# Exercise 4-13 Buffet - five foods in a tuple.  use a for loop to print them. try to modify (prompting an error). rewrite the tuple adding two different items. for loop it to print the revised menu.
food_tuple = ("pizza", "sub", "calzone", "stromboli", "pasta")
for food in food_tuple:
    print(f"The restaurant has {food}.")
# tuple[4] = "hamburger" # will throw an error for trying to change a tuple element.
new_food_tuple = ("pizza", "sub", "calzone", "pepperoni", "ham")
for food in new_food_tuple:
    print(f"The restaurant has {food}.")