# Tuple
""" A tuple is a collection which is ordered and unchangeable.
    Tuples are written with round brackets.
    Tuples are used to store multiple items in a single variable.
    Ordered: it means that the items have a defined order, and that order will not change.
    Unchangeable: which means that we cannot change, add or remove items after the tuple has been created.
    Allow duplicates: Since tuples are indexed, they can have items with the same value:"""

fruits = ("apple", "banana", "cherry", "grapes", "oranges")
print(fruits)  # ('apple', 'banana', 'cherry', 'grapes', 'oranges')
print(len(fruits))  # 5
print(fruits[1])  # banana
print(fruits[-1])  # oranges

#  --> tuple representation for a single value : remember the comma , :
tuple1 = ("apple",)
print(type(tuple1))  # <class 'tuple'>

# NOT a tuple
tuple2 = ("apple")  # <class 'str'>
print(type(tuple2))

# Check if "apple" is present in the tuple:
if 'apple' in fruits:
    print("yes, apple is in fruits tuple")
else:
    print("not in tuple")

""" Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
    But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple """

x = ("apple", "banana", "cherry")
y = list(x)  # converting into list
y[1] = "kiwi"  # update value to the list
x = tuple(y)  # converting back to Tuple
print(x)  # ('apple', 'kiwi', 'cherry')

# --> you can't remove any tuple value directly
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

y = list(x)
y.remove('apple')
print(y)  # ['kiwi', 'cherry']
x = tuple(y)
print(x)  # ('kiwi', 'cherry')

