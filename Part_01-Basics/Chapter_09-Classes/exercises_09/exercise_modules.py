class Restaurant:
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
    
    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()} has delicious {self.cuisine} cuisine')

