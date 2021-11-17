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
