# Python- Random Number

'''Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers'''

import random

print(random.randrange(1,10)) #o/p:- generate any number between 1 to 10 randomly

'''Python Random Module'''
'''Python has a built-in module that you can use to make random numbers.
The random module has a set of methods'''

# 1. random()
# Returns a random float number between 0 and 1

print(random.random())

# 2. randint()
# returns a number between 3 and 9 (both included)

print(random.randint(3, 9))

# 3. randrange()
# returns a number between 3 (included) and 9 (not included)

print(random.randrange(3, 9))