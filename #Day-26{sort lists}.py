# Sort Lists

'''sort() method that will sort the list alphanumerically, ascending, by default'''

# Sort list alphabetically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# sort descending, use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort the list based on how close the number is to 50 or any number
def myfunc(n):
  return abs(n - 50) #use any number instead of 50

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #o/p:- ['Kiwi', 'Orange', 'banana', 'cherry']

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #o/p:- ['banana', 'cherry', 'Kiwi', 'Orange']