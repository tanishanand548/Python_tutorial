# Python Casting
# Change one data types to another data types
# like "int" change to "float" or "str", similarly "float" to "int" or "str", and "str" to "int" or "float"

'''
Casting in python is therefore done using constructor functions

int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)

float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)

str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
'''

x = int(1.2) # convert float to int
y = int("1") # convert str to int

x1 = float(1) # convert int to float
y1 = float("1.25") # convert str to float

x2 = str(1) # convert int to str
y2 = str(1.25) # convert float to str