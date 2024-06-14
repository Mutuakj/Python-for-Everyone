
# Checking for items in a list
requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print('\nFinished making your pizza.\n')

# Checking for special items in a list
requested_toppings = ['mushrooms', 'green pepper', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green pepper':
        print('We are sorry! We have run out of green pepper.')
    else:
        print(f"Adding {requested_topping}.")
print('\nFinished making your pizza!\n')

available_toppings = ['mushrooms', 'green pepper', 'peperoni', 'extra cheese',
                      'olives', 'pineapple']
requested_toppings = ['mushrooms', 'french fries', 'green pepper',]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping}.')
    else:
        print(f'Sorry, We do not have {requested_topping} now.')
print('\nFinished making your pizza!')
