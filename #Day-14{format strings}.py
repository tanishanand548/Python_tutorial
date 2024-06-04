# Python - Format Strings
# we can combine strings and numbers by using f-strings

'''To specify a string as an f-string, simply put an "f" in front of the string literal, and add curly brackets "{}" as placeholders for variables and other operations'''

days = 13
p = f"python tutorial days {days}"
print(p)

'''Display the price with 2 decimals'''
price = 59
txt = f"The price is {price:.2f} INR" #".2f" means "f" show float character and "2" show decimal place up to, and "." show decimal
print(txt)

'''Perform a math operation in the placeholder'''
txt = f"The price is {20 * 20} INR"
print(txt)