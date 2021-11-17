# While Loops
current = 1
while current <= 3:
    print(current)
    current += 1

# Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Using a flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program."

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# using break to Exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to the {city.title()}")

# Using continue in a loop
current_number = 0
while current_number <10:
    current_number += 1
    if current_number % 2 ==0:
        continue  #  Continue stop the rest of the loop from performing and return to the beginning of the next part of the loop

    print(current_number)

# Avoiding Infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1  #If you forget to increment the integer you will be stuck in a infinite loop


