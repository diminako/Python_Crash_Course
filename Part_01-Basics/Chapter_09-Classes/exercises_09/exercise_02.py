# Exercise 9-10 Imported Restaurant - Using your latest Restaurant class, store it in a module.  make a separate file that imports Restaurant's methods to show that the import statement is working properly.
from exercise_modules import Restaurant
pinkys = Restaurant('pinkys', 'american')
pinkys.describe_restaurant()

# Exercise 9-11 Imported Admin - Start with your work from exercise 9-8 store the classes User and priveleges and admin in one module and createa  separate file.  import and show the inheritance is working as well.
from admin_module import *
dimitri = Admin('dimitri', 'pass1234')
dimitri.does_user_have_access()
