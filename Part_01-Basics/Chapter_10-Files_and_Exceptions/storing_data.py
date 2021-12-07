# Storing data - JSON
# Using json.dump() and json.load()

import json

numbers = [1,3,5,7,9,11,13,15,17]

filename = 'numbers.json'
with open(filename,'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)

print(numbers)

# Saving and reading user-generated Data
username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}")
with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}")

# use Exceptions to check if a username is already in the file
try:
    with open(filename) as f:
        username = json.load(f)
except:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}")
else:
    print("welcome back")