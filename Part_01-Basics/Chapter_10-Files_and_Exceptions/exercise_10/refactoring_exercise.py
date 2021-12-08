# Exercise 10-11 Favorite Number - write a program that prompts fpr the users favorite number . use json.dump() to store this number in a file.  write a separate program that reads this value and prints the message I know your favorite number is _____
import json

fav_num = input("What is you favorite number? ")
filename = 'fav_num.json'

with open(filename, 'w') as f:
    json.dump(fav_num, f) 

with open(filename) as f:
    favorite_number = json.load(f)

print(f'Your fav number is {favorite_number}')


# Exercise 10-12 Favorite Number Remembered - combine two programs if the number is already stored report the number to the user.  if not prompt for the users favorite number and store it in a file run it twice.

def get_stored_number():
    filename = 'nums.json'
    try:
        with open(filename) as f:
            nums = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return nums

def tell_nums():
    nums = get_stored_number()
    if nums:
        print(f"Here is you old number {nums}.")
    else:
        nums = input("What would you like your number to be?  ")
        filename = 'nums.json'
        with open(filename, 'w') as f:
            json.dump(nums, f)
            print(f"We'll remember your number is {nums}.")

tell_nums()


# Exercise 10-13 Verify user - The final listing for remember me.py assumes that the user has already entered their username or that the program is running for the first time.  we should modify it in case the current user is not the person who last used the program.  Before printing a welcome back message in the greet_user() ask the user if this is the correct username.  If it's not , call get_new_username() to get the correct username.

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    confirm_name = input(f"Is {username} your user name?  y/n")
    if confirm_name == 'y':
        if username:    
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")


greet_user()