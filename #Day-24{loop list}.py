# Loop Lists

'''You can loop through the list items by using a for loop'''

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
# Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  
# Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1


# A short hand for loop that will print all items in a list

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]