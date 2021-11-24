# Passing an arbitrary number of arguments.
def make_pizza(*toppings):
    print(toppings)

make_pizza('pepperoni')
make_pizza('pepperoni', 'green peppers', 'mushrooms')

def make_pizza(*toppings):
    print('\nMaking a pizza with the following toppings: ')
    for topping in toppings:
        print(f'- {topping}')

pizza_toppings = ['mushroooms', 'green peppers', 'onions']
make_pizza('pepperoni')
make_pizza('pepperoni', 'green peppers', 'mushrooms')
make_pizza(pizza_toppings)  # doesn't work the same way with an array.

# Mixing positional and arbitrary arguments
def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'{topping}')

make_pizza('pepperoni')
make_pizza('pepperoni', 'green peppers', 'mushrooms')

# Using Arbitrary keyword arguments
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile(
    'albert', 'einstein',
    location = 'princeton',
    field = 'physics',
)

print(user_profile)

