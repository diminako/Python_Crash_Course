# Exercise 4-1 Pizzas - make a loop to print a sentence about each pizza.  print a statement outside of the loop.
pizza = ["pepperoni", "Meatlovers", "Supreme"]
for za in pizza:
    print(f"I absolutely love {za} Pizza.")
print(f"I love all pizzas but I really love {pizza[0]} the best!")

# Exercise 4-1 Animals - make a list of 3 animals that have common characteristics.  loop over and print their names.  modify it to a sentence.  add a line outside of the loop about their commonality.
animals = ["bear", "tiger", "zebra", "penguin"]
for animal in animals:
    print(animal)
for animal in animals:
    print(f"{animal}'s look so cool!")
print("All of these animals would not make great pets!")

