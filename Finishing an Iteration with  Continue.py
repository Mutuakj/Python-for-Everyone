'''
The 'Continue' statement
jumps to the "top" of the loop and starts the next iteration.
'''
while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')
