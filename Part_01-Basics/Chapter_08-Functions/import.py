import modules  #import all of the functions from the modules.py file

modules.make_pizza(16, 'mushrooms', 'pepperoni', 'green peppers')

# Importing specific functions

from modules import make_pizza, say_hello  # With this method you don't need to use the 'modules.function_name()' when calling it due to it being explicit and the function is brought into this file. 
say_hello()

# Using as to give a function an Alias.
from modules import say_hello as sh
sh()

# Using as to give a module an alias.
import modules as mod
mod.make_pizza(14, "pepperoni")

# Importing all functions in a module
from modules import *  #This imports all the functions explicitely


