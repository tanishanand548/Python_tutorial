# Python - Global Variables
# Variable created outside of the function called global variables

x = "Python" #this "x" is a global variable

def myfunc():
    print("This is " + x + " tutorial") #o/p:- This is Python tutorial

myfunc()

# Local Variable - variable created in the function called local variable

def myfunc1():
    x1 = "Python" #this "x1" is a local variable
    print("This is " + x1 + " tutorial")
myfunc1()

print(x1) #not know what is "x1", outside the function


'''Convert local variable to global variable, by using "global" keyword'''
def myfunc2():
    global x2 #converted local to global variable
    x2 = "Python"
myfunc2()
print("This is " + x2 + " tutorial")