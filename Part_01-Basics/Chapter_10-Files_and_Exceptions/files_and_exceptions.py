# Files and Exceptions.

#  Reading from a file.
with open('pi_digits.txt') as file_object:
    contents  = file_object.read()
print(contents)
print(contents.rstrip())  # removes any whitespace

# File paths
with open('text_files/filename.txt') as file_object:
    contents = file_object.read()
print(contents)

# Relative file paths
file_path = '/Users/diminako/diminako/Books/Python_Crash_Course/Part_01-Basics/Chapter_10-Files_and_Exceptions/text_files/filename.txt'

# Reading line by line.
with open(file_path) as file_object:
    for line in file_object:
        print(line)

with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())  # Removes the extra line caused by the text files.

# Modifying a list of lines from a file.
file_name = 'text_files/filename.txt'
with open(file_name) as file:
    lines = file.readlines()

for line in lines:
    print(line.rstrip())

print(lines)

# working with a file's contents 
pi_file = 'pi_digits.txt'

with open(pi_file) as pi_txt:
    lines = pi_txt.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()  # or using .strip() to remove all whitespace.

print(pi_string)
print(len(pi_string))

# Large files: One million digits
filename = 'text_files/one_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f'{pi_string[:52]}...')
print(len(pi_string))

# Is my birthday in pi?
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("You are not special.")