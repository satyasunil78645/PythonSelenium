""""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression
lambda arguments : expression """

x = lambda a: a + 10
print(x)
y = x(3)
print(y)


def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)
print(mytripler(2))
