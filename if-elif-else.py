
# Using if, elif, elif and else statements
# They only ensure one block of code runs(True).
age = 65

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40
print(f"Your admission cost is ${price}.")

# Using multiple if statements.
# It ensures all conditions are checked for and those True printed.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print('\nAdding mushrooms.')
if 'peperoni' in requested_toppings:
    print('Adding peperoni')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
print('\nFinished making your pizza!')

