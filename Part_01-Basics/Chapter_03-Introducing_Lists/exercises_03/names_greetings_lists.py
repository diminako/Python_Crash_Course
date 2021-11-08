# 3-1 Names - Store a List of your friends names. print  each persons name by accessing each element in the list one at a time.
# 3-2 Greetings - Using the names list print the same message to a different person each time.
# 3-3 Your Own list - make a list of your favorite transportation.  Print several statements using these modes of transportation.

# 3-1 Names and 3-2 Greetings
name_list = ["Dimitri", "Emily", "John", "Brian", "Rachel"]
for i in name_list:
    print(f"Hello, {i}.  I hope you're well.")

# 3-3 My own list.
transports = ["car", "bike", "boat", "plane"]
for i in transports:
    if(i == "plane" or i == "boat"):
        print(f"I like to travel to Greece in a {i}")
    else:
        print(f"I like to ride my {i} to get to my location.")
