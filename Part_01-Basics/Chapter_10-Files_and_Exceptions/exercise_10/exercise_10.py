# Exercise 10-1 Learning Python - Open a blank file.  write a few lines summarizing python so far.  start each phrase with... 'in python you can...' save the file as learning_python.txt in this directory.  write a program that reads the file and prints what you wrote 3 times.  print the contents once by readin the entire file, once by looping over the file_obect, and once by storing the lines in a list and then working with them outside the 'with' block.
filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.read()

def print_three_times(x):
    for i in range(1, 4):
        print(x)

# for line in lines:
#     print(line)

print_three_times(lines)
print(lines)

# Exercise 10-2 Learning C - you can use replace() method to replace any word in a string with a different word.  here's a quick example showing how to replace 'dog' with 'cat'
# message = "I really like dogs."
# message.replace('dog', 'cat')
# >>> 'I really like cats'
# read in each line from the file you just created, learning_python.txt, and replace the word python with the name of another language such as C.  Print each modified line to the screen.

def replace_with_js(x):
        print(x.replace('python', 'javascript'))

replace_with_js(lines)