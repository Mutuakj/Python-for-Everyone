
total = 0
for num in range(10):
    total = total + num
print(total)

nums = []

for value in range(1, 11):
    nums.append(value**2)
print(nums)

# List compression
nums = [value**2 for value in range(1,11)]
print(nums)

# Slicing & Looping through a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

players.append('Maxwell')
print('Here are the last three players in my team:')
for player in players[3:]:
    print(player.title())



my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli']
my_friends_food = my_foods[:]

print('My favourite foods are:')
print(my_foods)
print('\nMy friends favourite foods are: ')
print(my_friends_food)

my_foods.append('cannoli')
my_friends_food.append('ice cream')

print('\nMy favourite foods are:')
print(my_foods)
print('\nMy friends favourite foods are: ')
print(my_friends_food)
