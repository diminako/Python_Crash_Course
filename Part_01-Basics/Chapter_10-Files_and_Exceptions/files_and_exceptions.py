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
