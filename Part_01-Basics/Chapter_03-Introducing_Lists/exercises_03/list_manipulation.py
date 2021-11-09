# 3-4 Guest List - make a list of people to invite to dinner and print out a message to each of them.
friends_list = ["Dimitri", "Emily", "John", "Ronnie", "Brian", "Rachel"]
for i in friends_list:
    if (i == "Ronnie"):
        cant_make_it = i
        print(f"You aren't welcome here, {i}")
        friends_list.remove(i)
    else:
        print(f"Hello, {i}, I would like to invite you to my dinner party.")
print(cant_make_it)


# 3-5 Changing Guest List - one of your guest can't make it. 
print(friends_list)
print(f"{cant_make_it} and {friends_list[2]} can't make it to the party.")
friends_list.pop(2)
friends_list.insert(2, "Matt")

for i in friends_list:
    print(f"Hello, {i}, you are in the final dinner list.")

# 3-6 More Guests - let everyone know you found a bigger table.  you can inv 3 more guests.  insert someone at the beginning, middle and end of you table.  print new invitations.
print("Hello everyone!  I have found a bigger table and can invite 3 more guests.")
friends_list.insert(0, "Cloud")
friends_list.append("Sabin")
middle_of_group = round(len(friends_list) / 2)
friends_list.insert(middle_of_group, "Ramza")
for i in friends_list:
    print(f"Welcome {i}!  You are invited to dinner with us!")


# Shrinking Guest List - you found out the table wont arrive in time.  you only have room for 2 others.  tell them you can only inv two people.  pop() guests until two remain.  print a message each time u remove someone from the list that they cant come.  let the two left that they can still come.  at the end del the last two people and print an empty List.
print("Hello everyone!  Bad news... I can only invite two of you.  If you don't receive an invitation don't come.")
while (len(friends_list) > 2):
    popped = friends_list.pop()
    print(f"Sorry {popped}, you can't eat with us.")
for i in friends_list:
    print(f"Hell yeah, {i}.  Let's eat.")
