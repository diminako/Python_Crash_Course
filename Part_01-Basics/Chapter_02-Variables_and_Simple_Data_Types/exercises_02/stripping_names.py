# Exercise 2-7 Stripping Names - Use a variable to represent a person's name, and include some whitespace characters at the beginning and end of the name.  Make sure you use each character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.  The print the name used each of the three stripping functions, lstrip(), rstrip(), strip().

first_name = "     Dimitri "
last_name = "Nakos        "
hello = "h e l l o,"

print(f"{hello.strip()} {first_name.lstrip()} {last_name.rstrip()}.")