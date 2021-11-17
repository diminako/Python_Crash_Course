# Exercise 7-1 Rental Car - ask what kind of car a user would like.  print a message with that car.
car = input("What kind of car would you like to buy? ")
print(f"Let me see if I can find a {car} for you...")

# Exercise 7-2 Restaurant Seating - Ask how many people are dining.  greater than 8 they gotta wait.
dinner_guests = int(input("How many guests will you be having tonight?  "))
if dinner_guests > 8:
    print(f"I'm sorry we will need to get a table ready for {dinner_guests} people.")
else:
    print(f"If your {dinner_guests} dinner guests are here then right this way!")

# Exercise 7-3 Multiples of Ten - 
for num in range(1,101):
    if num % 10 == 0:
        print(f"{num} is a multiple of ten.")
number = int(input("give me a number..."))
if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print("Your choice of {number} is not a multiple of ten.")