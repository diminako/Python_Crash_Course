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


print(friends_list)
# 3-5 Changing Guest List - one of your guest can't make it. 
print(f"{cant_make_it} and {friends_list[2]} can't make it to the party.")
print(friends_list)
friends_list.pop(2)
friends_list.insert(2, "Matt")
print(friends_list)
for i in friends_list:
    print(f"Hello, {i}, you are in the final dinner list.")





# 3-6 More Guests






# Shrinking Guest List