# Variables
dashes = "------------------"
# Every variable is connected to a value.  Those values can be strings, integers, floats, lists, functions, and Dictionaries
message = "Hello Github World :)"
print(message)

message = "Hello Python Crash Course"
print(message)

message = "Reassigning variables gives them new value."
print(message)


print(dashes)
# Variables in python are generally lowercase and use snake_case for python.

# It's better to think of variables as jars with labels.  Where you can change out the contents but not the label.  and The jar also remains the same reference point in the code.

# Try it yourself exercises.
first_name = "Dimitri"
last_name = "Nakos"
print(first_name + last_name)

print(dashes)
# Simple variable methods

# Changing case in a string with Methods

# Title() gives uppercase to the first letter of every word in the string.
message = "final fantasy tactics"
print(message.title())
# Upper() give uppercase to all letter in a string.
message = message.upper()
print(message)
# Lower() gives lowercase to all letters in a string.
message = message.lower()
print(message)

print(dashes)
# "f strings" can be used in variables and printed in as the variable and pass the variable through itself.
best_game_series = "Final Fantasy"
best_game = "Tactics"
best_game_ever = f"{best_game_series} {best_game}"
# This can simplify a print variable/
print(best_game_ever)

print(dashes)
# Format() to leave variables open and assign them later in the order they were provided.
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# Adding whitespace to strings with tabs or newlines

print(dashes)
# Tabs
print("Hello")
print("\tHello")

print(dashes)
# Newline
languages = "Python, JavaScript, C++, Ruby"
lang_lines = "\nPython, \nJavaScript, \nC++, \nRuby"
lang_lines_tabs = "\n\tPython, \n\tJavaScript, \n\tC++, \n\tRuby"
print("Languages: " + languages)
print("Languages: " + lang_lines)
print("Languages: " + lang_lines_tabs)

print(dashes)
# Stripping whitespace from strings.
message = "    The world is yours     ."
print(message.strip())

# Strip space from the left of strings
message = "      Hello."
print(message.lstrip())

# Strip soace from the right of strings
message = "Hello       ."
print(message.rstrip())


