""" Rules for Python variables:
        A variable name must start with a letter or the underscore character
        A variable name cannot start with a number
        A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
        Variable names are case-sensitive (age, Age and AGE are three different variables) """

# Legal variables
my_var = "John"
_my_var = "John"
myVar = "John"

#  Illegal variables
""" 
2mover = "John"
my-var = "John"
my var = "John """

#  Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Apple"
print(x)
print(y)
print(z)

#  Unpack a list:
fruits = ["apple", "banana", "cherry"]
x1, y1, z1 = fruits
print(x1)
print(y1)
print(z1)

# ---> Global variables
"""Variables that are created outside of a function Global variables can be used by everyone, both inside of 
functions and outside."""

"""Normally, when you create a variable inside a function, that variable is local, and can only be used inside that 
function To create a global variable inside a function, you can use the - global -  keyword. """

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"  # global variable


def my_func():
    global x  # changing the global variable inside the function, we use globa  l
    x = "fantastic"


my_func()

print("Python is " + x)
