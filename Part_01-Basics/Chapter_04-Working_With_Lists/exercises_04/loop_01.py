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