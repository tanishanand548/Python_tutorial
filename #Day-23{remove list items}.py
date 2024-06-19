# Remove List Items
'''remove() method removes the specified item'''

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

'''If there are more than one item with the specified value, the remove() method removes the first occurrence'''

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist) #o/p:- ["apple", "cherry", "banana", "kiwi"]


# The pop() method removes the specified index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

'''If you do not specify the index, the pop() method removes the last item'''

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

'''The del keyword can also delete the list completely'''

thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)