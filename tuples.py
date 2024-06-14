
# Tuples: They are immutable lists. They use parentheses() unlike Lists which use square brackets[].
# To define a tuple with one character, one has to use a trailing comma; eg. (3,)

dimensions = (200, 50)
print('Original dimensions')
for dimension in dimensions:
    print(dimension)

# Assigning a new value to a variable that represents a tuple

dimensions = (400, 80)
print('\nModified dimensions')
for dimension in dimensions:
    print(dimension)

old_menu = ('ugali', 'pizza', 'matoke', 'mukimo', 'muthokoi')
print("This is buffet hotel old menu")
for food in old_menu:
    print(food.title())

'''old_menu [0] = 'Matumbo'

print("This will return an intentional error. Remember tuples are immutable.")
for food in old_menu:
    print(food) '''

old_menu = ('ugali', 'pizza', 'cookies', 'rice', 'fish', 'pilau', 'junk food')

print("\nThis is buffet hotel's new menu")
for food in old_menu:
    print(food.title())