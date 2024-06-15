
# They store a variables key and value.
# It is wrapped in braces {}
# E.g.
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Starting with an empty dictionary
space_0 = {}

space_0['color'] = 'purple'
space_0['points'] = 15
print(space_0)

space_x = {'color': 'maroon'}
print(f"Space_x color is {space_x['color'].title()}")

# space_x = {'color': 'blue'} OR
space_x['color'] = 'white'
print(f"Space_x color is now {space_x['color'].title()}")

favourite_languages = {
    'Joseph': 'python',
    'Michael': 'javascript',
    'Rachael': 'php',
    'Tracy': 'kotlin',
    'Cyrus': 'java',
    'Manuel': 'python',
    }

language = favourite_languages['Joseph'].title()
print(f"Joseph's favourite language is {language}")

# Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'firstname': 'enrico',
    'lastname': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"value: {value}\n")

# Best example showing looping through a dictionary.
favourite_languages = {
    'Joseph': 'python',
    'Michael': 'javascript',
    'Rachael': 'php',
    'Tracy': 'kotlin',
    'Cyrus': 'java',
    'Manuel': 'python',
    }
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

