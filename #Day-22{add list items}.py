# Add List Items
'''Adding more elements in the list'''

# Append Items
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Insert Items (use indexing)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) 

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
''' you can add any iterable object (tuples, sets, dictionaries etc.), with the help of "extend()" method'''
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) #tuple and list