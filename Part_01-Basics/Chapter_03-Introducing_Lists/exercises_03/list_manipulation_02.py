# Exercise 3-8 Seeing the World.  list 5 locations in the world. print in original order. use sorted() to print and alphabetical list.  print your list again.  reverse your list with sorted(). print the original array to show u haven't altered it.  use reverse() and print it to show the original has changed.  use reverse again and print. use sort() and print it.  use sort and reverse and then print it.

locations = ["Greece", "Chicago", "Italy", "Zimbabwe", "South Korea"]
print(locations)

print(sorted(locations))

print(locations)

print(sorted(locations, reverse=True))

print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

# Exercise 3-9 Length of List - get the length of a List
len(locations)
