# Access List Items
'''List items are indexed and you can access them by referring to the index number'''

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Check if Item Exists

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")