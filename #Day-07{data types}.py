# Python Data Types
# Data types are categories of values that determine what kind of operations can be performed on them

'''Some built-in or default data types in python are as follow'''
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

x = "Python" #type- str
print(type(x))

x = 20	#type- int	
x = 20.5	#type- float	
x = 1j	#type- complex	
x = ["apple", "banana", "cherry"]	#type- list	
x = ("apple", "banana", "cherry")	#type- tuple	
x = range(6)	#type- range	
x = {"name" : "John", "age" : 36}	#type- dict	
x = {"apple", "banana", "cherry"}	#type- set	
x = frozenset({"apple", "banana", "cherry"})	#type- frozenset	
x = True	#type- bool	
x = b"Hello"	#type- bytes	
x = bytearray(5)	#type- bytearray	
x = memoryview(bytes(5))	#type- memoryview	
x = None #type- NoneType

x1 = 4 + 5j
print(x1.real, x1.imag) #to find real and imaginary part of the complex number in python 