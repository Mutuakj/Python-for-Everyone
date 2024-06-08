# Lists,
cars = ['jaguar', 'range', 'audi', 'bmw']
# Modifying
cars[1] = 'Discovery'
# Appending(Adds the new element at the end of the list)
cars.append('porsche')
# Inserting(adds the new element at the specified index)
cars.insert(4, 'subaru')
cars.insert(5, 'toyota')
cars.insert(6, 'suzuki')
cars.insert(7, 'mark x')
# Deleting an element within a list
del cars[5]
# Popping an element from the List
my_first_car = cars.pop()
# We can also use remove to remove an element from a list
cars.remove('mark x')

message = f"Python will buy me {cars[0].title()} one day."
print(message)
message = f"I am confident that I will buy {cars[1].title()} soon."
print(message)
message = f"For the records, I will buy an {cars[2].title()} by 2025."
print(message)
message = f"I know a {cars[3].upper()} cX5 will look good on me."
print(message)
message = f"Hard work in Python enabled me to purchase a {cars[4].title()}."
print(message)
message = f"With passion in Python, I can start by buying a {cars[5].title()}."
print(message)
message = f"For your information, my first car was a {cars.pop(4).title()}."
print(message)
