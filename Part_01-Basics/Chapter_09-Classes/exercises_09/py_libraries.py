# Exercise 9-13 Dice - Make a class Die with one attribute called sides, which has a default value of 6.  Write a method called roll_die() that prints a random number between 1 and the number of sides the die has.  Make a 6 sided die and roll it 10 times.
from random import randint

# class Die:
#     def __init__(self, sides):
#         self.sides = sides
#     def roll_die(self):
#         print(randint(1, self.sides))

# six_sided = Die(6)
# dodecasided = Die(12)

# for roll in range(1, 10):
#     six_sided.roll_die()
# for roll in range(1, 10):
#     dodecasided.roll_die()

# Exercise 9-14 Lottery - Make a list or tuple containing a series of 10 numbers and 5 letters. randomly select four numbers or letters from the list and print a message saying that any ticket matching these four letters or numbers wins a prize.
# rando_list = [1, 5, 'd', 7, 3, 'i', 'm', 2, 4, 0, 6, 9, 8, 'n', 'a']
# rando_str = ''
# for i in range(0, 4):
#     rando_str += str(rando_list[randint(0, (len(rando_list) - 1))])

# print(rando_str)

# Exercise 9-15 Lottery Analysis - Use a loop to see how hard it might be to win the lottery you just modeled. Make a list of tuple called my_ticket write a loop that keeps pulling numbers until your ticket wins.  print a message reporting how many times the loop had to run. to get your winning ticket.
rando_list = [1, 5, 'd', 7, 3, 'i', 'm', 2, 4, 0, 6, 9, 8, 'n', 'a']
winning_ticket = 'dimi'
times_ran = 0
rando_str = ''

while rando_str != winning_ticket:
    rando_str = ''
    for i in range(0, 4):
        rando_str += str(rando_list[randint(0, (len(rando_list) - 1))])

    times_ran += 1
    if (rando_str == winning_ticket):
        print(f'Holy shit {winning_ticket} is the winner!')
        break

print(times_ran)

# Exercise 9-16