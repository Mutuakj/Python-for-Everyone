while True:
    print('Who are you?')
    name = input()
    if name != 'Joseph':
        continue
    print('Hello, Joseph. What is the password? (It is a fish.)')
    password = input()
    if password == 'sword1':
        print('Access granted.')
        break
    else:
        print('Access denied.')





