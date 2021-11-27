# Exercise 9-1 Restaurant.  Make a class called Restaurant.  The __init__() method for restaurant should store two attributes: a restaurant_name and cuisine_type.  Make a method called describe_restaurant() that prints these two pieces of information and a method called open_restaurant() that prints a message indicating that the restaurant is open.  Make an instance called restaurant from your class.  Print the two attributes individually and then call both methods.

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has delicious {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

pinkys = Restaurant('pinkys', 'diner')
pinkys.describe_restaurant()
ilios = Restaurant('ilios noche', 'greek')
ilios.describe_restaurant()

print(pinkys.restaurant_name)
print(pinkys.cuisine_type)
print(ilios.restaurant_name)
print(ilios.cuisine_type)

ilios.open_restaurant()
pinkys.open_restaurant()

# Exercise 9-2 Three Restaurants - Start with your class from exercise 9-1.  Create 3 different instances from the class and call describe_restaurant on all three.
mr_ks = Restaurant('mr. K\'s', 'diner')
great_wall = Restaurant('great wall of china south', 'chinese')
bossy_chicken = Restaurant('bossy beaulah\'s', 'chicken sandwhich')

mr_ks.describe_restaurant()
great_wall.describe_restaurant()
bossy_chicken.describe_restaurant()

# Exercise 9-3 make a class called User.  create two attributes called first_name and last_name and then create several other attributes that are typically stored in a users profile.  Make a method called describe_user() that prints a summary of the user's information.  Make another method called greet_user() that prints a personalized greeting to the user.  Create several instances representing different users, and call for both methods for each user.

class User():
    def __init__(self, first_name, last_name, fav_genre, fav_movie, fav_car):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_genre = fav_genre
        self.fav_movie = fav_movie
        self.fav_car = fav_car

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} love the {self.fav_genre}, their favorite movie is {self.fav_movie.title()} and they drive a {self.fav_car}.")

    def greet_user(self):
        print(f'Hello, {self.first_name.title()}!')

dimitri = User('dimitri', 'nakos', 'horror', 'half baked', 'm3')
john_chi = User('john', 'chi', 'thriller', 'momento', 'impreza')
emily = User('emily', 'pruitt', 'romantic', 'love actually', 'tiguan')

dimitri.describe_user()
john_chi.describe_user()
emily.describe_user()

dimitri.greet_user()
john_chi.greet_user()
emily.greet_user()

# Exercise 9-4 Number Served - Start with a program from 9-1 Add an attribute called number_served with a default value of 0.  Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print again.  Add a method called set_number_served() that lets you set the number of customers that have been served.  Call this method with a new number and print the value again.  Add a method called increment_number_served()  that lets you set the number of customers who've been served.  Call this method with any number you like that could represent how many customers were served in, say, a da of business.
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has delicious {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, customers):
        self.number_served = customers

    def increment_number_served(self, new_customers):
        self.number_served += new_customers

pinkys = Restaurant('pinkys', 'diner', 0)
print(pinkys.restaurant_name)
print(pinkys.number_served)
pinkys.number_served = 3
print(pinkys.number_served)
pinkys.set_number_served(5)
print(pinkys.number_served)
pinkys.increment_number_served(5)
print(pinkys.number_served)

# Exercise 9-5 Login Attempts - Add an attribute called login_attempts to your User class from 9-3  write a method called increment_login_attempts() that increments the value of login_attempts by 1. write another method called reset_login_attempts() that resets the value of login_attempts to 0.  Make an instance of the User class and call increment_login_attempts() several times.  Print the value of login attempts to make sure it was incremented properly, and then call reset_login_attempts to make sure it was incremented properly, and then call reset_login_attempts().  Print login_attempts again to make sure it was set to 0.
class User():
    def __init__(self, first_name, last_name, fav_car):
        self.first_name = first_name
        self.last_name = last_name
        self.fav_car = fav_car
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()} and they drive a {self.fav_car}.")

    def greet_user(self):
        print(f'Hello, {self.first_name.title()}!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

dimitri = User('dimitri', 'nakos', 'm3')
dimitri.increment_login_attempts()
print(dimitri.login_attempts)
dimitri.increment_login_attempts()
dimitri.increment_login_attempts()
dimitri.increment_login_attempts()
print(dimitri.login_attempts)
dimitri.reset_login_attempts()
print(dimitri.login_attempts)

# Exercise 9-6 Ice Cream Stand - An ice cream stand is a specific kind of restaurant.  Write a class called IceCreamStand that inherits from the restaurant class you wrote in Exercise 9-1 or 9-4.  Add an attribute called flavors that stores a list of ice cream flavors.  write a method that displays these flavors.  create an Instance of IceCreamStand and call this method.
class Restaurant:
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} has {self.cuisine}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine):
        super().__init__(restaurant_name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'mint']

    def flavors_available(self):
        for flavor in self.flavors:
            print(f'{flavor}')

ritas = IceCreamStand('ritas', 'ice cream')
ritas.flavors_available()

# Exercise 9-7 Admin - An administrator is a special kind of User.  Write a class called Admin that inherits from the User class you wrote in 9-3 or 9-5.  Add an attribute, privileges, that store a list of string like 'can add post', ' can delete post' , 'can ban user', and so on.  write a method to show_privileges() that lists the administrators set of privileges.  Create an instance of Admin and call your method.
# Exercise 9-8 make privileges an instance of attributes.
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", 'can delete post', 'can ban user', 'can create users']

    def show_privileges(self):
        print(f'{self.first_name.title()} {self.last_name.title()} has the following privileges: ')
        for privilege in self.privileges:
            print(f"{privilege}.")



dimitri = Admin('dimitri', 'nakos')
dimitri.show_privileges()

# Exercise 9-9 Battery Upgrade - Use the final version of electric car from this chapter.  Add a method to the Battery class called upgrade_battery() This method should check the battery size and set the capacity to 100 if it isn't already.  then call get_range() a second time after upgrading the battery you should see an increase to the car's range.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("Filling the gas tank.")

class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def charge_battery(self):
        print("Charging the electric battery.")

    def fill_gas_tank(self):
        print("This vehicle has no gas tank.")
        self.charge_battery()
    
    def upgrade_battery(self):
        if self.battery_size == 75:
            self.battery_size = 100
            print(f'This car\'s battery has been upgraded to {self.battery_size}-kWh.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')

class Electric(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


dimis_tesla = Electric('tesla', 'model s', 2019)

dimis_tesla.battery.get_range()
dimis_tesla.battery.upgrade_battery()
dimis_tesla.battery.get_range()