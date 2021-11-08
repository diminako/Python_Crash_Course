dashes = "-------------"

# Integers
print(2 + 2) # 4
print(2 - 2) # 0
print(2 * 3) # 6
print(3 / 2) # 1.5

print(dashes)
# Exponents
print(3 ** 2) # 9
print(3 ** 3) # 27
print(10 ** 6) # 1000000

print(dashes)
#  PEMDAS  You can't assume a number next to the parenthesis will get multiplied.  You must be explicit.
number = 3 * 4 * (2 + 2 - 1) ** 3
print(number)

print(dashes)
# Floats

print(0.1 + 0.2) # 0.3
print(0.2 + 0.2) # 0.4
print(2 * 0.1) # 0.2
print(2 * 0.2) # 0.4

print(dashes)
# Sometimes coding languages can do provide unexpected results like this. So be aware this can happen.
print(0.2 + 0.1) # 0.30000000000004
print(3 * 0.1) # 0.30000000000004

print(dashes)
# Integers and Floats - When you divide any two numbers, even if they are integers that result in a whole number, you'll always get a float.  If you mix an integer and a float you will always get a float as well.
print(4 / 2) # 2.0
print(1 + 2.0) # 3.0
print(2 * 3.0) # 6.0
print(3.0 ** 2) # 9.0

print(dashes)
# Underscore large numbers to make them more readable.
large_number = 4_000_500
print(large_number)

#  Multiple assignments
x, y, z = 1, 2, 3
print(x)
print(z)
print(y)

# Constants - NOTE python doesn't have constants but programmers use CAPITAL to denote that these variables are to be treated as constants.
MAX_CONNECTIONS = 5_000
print(MAX_CONNECTIONS)


