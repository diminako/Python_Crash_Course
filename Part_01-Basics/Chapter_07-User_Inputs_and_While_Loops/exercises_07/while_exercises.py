# Exercise 7-4 Pizza Toppings - add a loop that prompts the user to enter toppings.  until they hit quit.  print out the pizza topping they asked for.
prompt = "\nWhat pizza topping would you like? "
prompt += "\nType 'quit' when you are done adding toppings..."

toppings = []
active = True

while active:
    add_topping = input(prompt)

    if add_topping =='quit':
        break
    else:
        toppings.append(add_topping)

print("You are going to get these toppings:")
for topping in toppings:
    print(f"{topping}")
print(toppings)

# Exercise 7-5 Movie Tickets -  movie ticket with different prices based on age.
age = ''
while age == '':
    age = input("what is your age?")
    if age == '':
        continue

    if int(age) < 10:
        print("Your ticket is $10.")
    elif int(age) < 20:
        print("Youre ticket is $20.")
    else:
        print("Your ticket is $30.")

# Exercise 7-6 Three Exits - exit from a while loop using 3 different methods. conditional test to stop the loop. active variable. and a break statement.
active = True
while active: # Active variable test
    answer = input("Please type in 'not active' to stop this.")
    if answer == 'not active':
        active = False
    else:
        print("God help us!!!")

number = 0
while number < 10:
    print(number)
    number += 1
    if number == 5:
        break  # Break statement to stop the while loop

number = 0
while number <= 10: # Conditional exit
    print(number)
    number += 1

# Exercise 7-7 Infinite loop
# number = 0
# while number < 5:
#     print("never gonna give you up")  # Number will never increment past 0 without a way for it to increase so this loop will run forever.

