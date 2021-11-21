# Using a while loop with Lists and Dictionaries

# Moving Items from One List to Another
# Start with users that need to be verified, and an empty list to hold confirmed users.
unconfirmed_users = ['alice','brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.  move each verified uer into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)

# Removing all instances of specified values from a list
pets = ['dog','cat', 'goldfish', 'rabbit', 'cat', 'cat', 'lizard']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)

# Filling a dictionary with user input.
responses = {}
# Set a flag to indicate tht polling is active.
polling_active = True

while polling_active:
    # Prompt for the users name and response.
    name = input("\nWhat is your name?  ")
    response = input("Whic mountain would you like to climb someday?  ")
    # store the responses in the dictionary
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond?  (yes/no)  ")
    if repeat == 'no':
        polling_active = False

# Polling is complete.  Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
