# The 'Break' statement is used to exit the currently executing loop.
while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)
print('Done!')
