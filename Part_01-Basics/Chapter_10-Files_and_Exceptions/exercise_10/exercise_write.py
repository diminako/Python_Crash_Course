# Exercise 10-3 Guest - Write a program that prompts the user for their name.  When they respond, write their name to a file called guest.txt
new_name = input("What is your name?  ")
with open('guests.txt', 'w') as file_object:
    file_object.write(new_name)

# Exercise 10-4 Guest Book - Write a while loop that prompts the users for their name.  When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt.  Make sure each entry appears on a new line in the file.
active = True

while active:
    new_name = input('What is your name?  ')
    if new_name == 'q':
        active = False
        break
    else:
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(f'{new_name}\n')
        print('type q to quit')

# Exercise 10-5 Programming Poll - Write a while loop that asks people why they like programming.  Each time someone enters a reason, add their reason to a file that stores all the responses.

active = True

while active:
    new_name = input('Why do you like programming?  ')
    if new_name == 'q':
        active = False
        break
    else:
        with open('reasons.txt', 'a') as file_object:
            file_object.write(f'{new_name}\n')
        print('type q to quit')