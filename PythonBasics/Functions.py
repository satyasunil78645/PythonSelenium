# In Python a function is defined using the def keyword:
def my_function():
    print("Hello from a function")


def my_function_Parameter(f_name, l_name):
    print(f_name + " " + l_name)


my_function_Parameter("Emil", "password")


# If number of arguments are unknown, add a * before the parameter name:

def my_function1(*kids):
    print("The youngest child is " + kids[1])


my_function1("Emil", "Tobias", "Linus")


# You can also send arguments with the key = value syntax.
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function2(**kid):
    print("His last name is " + kid["lname"])


my_function2(fname="Tobias", lname="Refsnes")


# If we call the function without argument, it uses the default value:
def my_function3(country="Norway"):
    print("I am from " + country)


my_function3("India")
my_function3()


# Passing List as an arguments
def my_function4(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function4(fruits)
