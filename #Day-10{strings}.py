# Python Strings
# text in the single quotation marks, or double quotation marks

a = "Python Tutorial" # Python tutorial is a string and "a" is a variable which store string value
print(a)

'''Strings are Arrays'''
'''
strings in Python are arrays of bytes representing unicode characters
Square brackets can be used to access elements of the string
'''

a1 = "Python Tutorial"
print(a1[1]) #o/p:- y, "1" is the index value and start indexing at "0"


'''Looping Through a String'''

for i in "python":
    print(i)
    
    
'''String Length'''
x = "python"
print(len(x))

'''Check word or text is present in the string or not'''

# text or word present in the string
p = "python tutorial helps in many it fields"
print("python" in p)  # return true, because "python" word present in the "p", and return a boolean character

# # text or word not present in the string
print("language" not in p) # return true, because "language" word not present in the "p", and return a boolean characterr