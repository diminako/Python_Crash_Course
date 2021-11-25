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