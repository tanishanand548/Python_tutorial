# List Comprehension

'''List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list'''

# Without list Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

# With list Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# Only accept items that are not "apple"
newlist = [x for x in fruits if x != "apple"]
print(newlist) #o/p:- ['banana', 'cherry', 'kiwi', 'mango']

# With no if statement
newlist = [x for x in fruits]
print(newlist) #o/p:- ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# range() function to create an iterable
newlist = [x for x in range(10)]
# with condition
newlist = [x for x in range(10) if x < 5]

# new list to upper case
newlist = [x.upper() for x in fruits]

# replace all list elemet with"hello"
newlist = ['hello' for x in fruits]

# Return "orange" instead of "banana"
newlist = [x if x != "banana" else "orange" for x in fruits]