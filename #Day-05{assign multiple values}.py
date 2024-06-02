# Python Variables - Assign Multiple Values

'''
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line
Note: Make sure the number of variables matches the number of values, or else you will get an error.
'''
p, y, t = "python", "tutorial", "day"
print(p, y, t) #o/p:- python tutorial day

'''
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line
'''
p = y = t = "python"
print(p, y, t) #o/p:- python python python

'''
Unpack a Collection
If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpackings
'''
a = ["python", "tutorial", "day"]
p, y, t = a
print(p, y, t) #o/p:- python tutorial day