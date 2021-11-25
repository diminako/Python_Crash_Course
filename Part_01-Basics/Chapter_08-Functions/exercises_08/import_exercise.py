# Exercise 8-15 Printing Models  Put the functions for the example printing_models.py in a separate file.  Write an import statement at the top to use printing modules here.
from funct_import import print_models, show_completed_models

unprinted_designs = ['NES', 'SNES', 'GBA']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Exercise 8-16 Imports
import funct_import
from funct_import import print_models, show_completed_models
from funct_import import print_models as p_m
import funct_import as fi
from funct_import import *

funct_import.show_completed_models(completed_models)