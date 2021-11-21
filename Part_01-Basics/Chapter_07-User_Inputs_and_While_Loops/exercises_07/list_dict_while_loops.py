# Exercise 7-8 Deli - make a list called sandwich_orders fill with name of sandwiches.  make empty list finished_sandwiches.  loop thru sandwich orders and print a message for each order. as each sandwich is made move it to finished after all sandwiches are made print a message listing each made.
sandwich_orders = ['reuben', 'blt', 'pbj', 'baloney', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"{made_sandwich}, coming right up!")
    finished_sandwiches.append(made_sandwich)
print("Orders are complete!")
for sandwich in finished_sandwiches:
    print(f"We are now out of {sandwich} sandwiches.")
print(sandwich_orders)

# Exercise 7-9 No Pastrami - using sandwich orders make sure patstrami appears at least 3 times. print a message saying the restaurant has run out of pastrami and use a while loop to remove all pastrami sandwiches.
sandwich_orders = ['reuben', 'pastrami', 'pbj', 'pastrami', 'baloney', 'tuna', 'pastrami']
finished_sandwiches = []

print("86 Pastrami!  We are out of Pastrami!!!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    made_sandwich = sandwich_orders.pop()
    print(f"{made_sandwich}, coming right up!")
    finished_sandwiches.append(made_sandwich)
print("Orders are complete!")
print(f"We are now out of all sandwiches.")
print(finished_sandwiches)

# Exercise 7-10 Dream vacation - poll people about their dream vacation.  write a prompt "if you can visit one place in the world, where would you go? include a block of code that prints the results of the poll."
poll_active = True
dream_vacations = {}

while poll_active:
    name = input("What is you name?  ")
    location = input("Where is you dream vacation?  ")
    dream_vacations[name] = location
    repeat = input("would you like another pol? (yes/no)  ")
    if repeat == 'no':
        print("Polling has stopped.")
        poll_active = False
print(dream_vacations)
for name, location in dream_vacations.items():
    print(f"{name.title()} want to visit {location.title()}.")
