# for loops
magicians = ["David", "Dimitri", "John Chi"]
for magician in magicians:
    print(magician)

for i in magicians:
    print(f"{i.upper()}, Wow!  Your really are magic!\n")

for i in magicians:
    print(f"{i}, That was a great trick!")
    print(f"I can't wait to see your next trick {i}.\n")

# This is where indentation starts becoming more and more important.
# Errors that you will see will look like:
# IndentationError: expected an indented block
# IndentationError: unexpected indent

