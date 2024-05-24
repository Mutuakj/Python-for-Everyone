'''
We still have a variable that is the smallest so far.
The first time through the loop smallest is None,
so we take the first value to be the smallest.
The "is" and "is not" Operators
Python has an (is) operator that can be used
in logical expressions.
It implies "is the same as"
Its similar to, but stronger than ==
"is not" is also a logical operator
'''
smallest = None
print('Before', smallest)
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)
