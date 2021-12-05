# Exceptions - special objects used to manage errors that arise during a program's execution.

# Handling ZeroDivisionError Exception
# print(5/0)  # Throws error ZeroDivisionError: division by zero

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")

# Using Exceptions to prevent crashes
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number =='q':
        break
    try:  # Must tell python to attempt use this calculation
        answer = int(first_number) / int(second_number)
    # print(answer)  printing out answer this way would cause an errorif the second number is 0.
    except ZeroDivisionError:
        print("You can't divide by zero.")
    else:
        print(answer)

# Handling the FileNotFoundError Exception
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8')as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, The file {filename} does not exist.")
# Analyzing text
else:
    # Count the approximat number of words in the file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")

# Working with Multiple files.
def count_words(filename):
    '''count the approximate number of words in a file.'''
    try:
        with open(filename, encoding='utf-8')as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, The file {filename} does not exist.")
    # Analyzing text
    else:
        # Count the approximat number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt']
for filename in filenames:
    count_words(filename)

# Failing silently.  This passes the error even if it throws a problem.
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")