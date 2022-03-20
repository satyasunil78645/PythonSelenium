# List
""" List is a collection which is ordered, changeable, and allow duplicate values.
    ordered -  it means that the items have a defined order, and that order will not change.
    changeable - meaning that we can change, add, and remove items in a list after it has been created.
    Duplicate - Since lists are indexed, lists can have items with the same value. """

# string int and boolean data type
values = ["abc", 34, True, 40, "male"]

print(values)  # ['abc', 34, True, 40, 'male']
print(type)  # <class 'type'>
print(values[1])  # 34  - prints 1st index value

# change the index value
values[1] = 55
print(values)  # ['abc', 55, True, 40, 'male']

# Add value in the list at the end using append() function
values.append("sunil")
print(values)  # ['abc', 55, True, 40, 'male', 'sunil']

# insert the value in the list at specific index
values.insert(0, 'satya')
print(values)  # ['satya', 'abc', 55, True, 40, 'male', 'sunil']

# reverse the list
values.reverse()
print(values)  # ['sunil', 'male', 40, True, 55, 'abc', 'satya']
# -------------------------------
# int data type
list2 = [1, 5, 7, 9, 3]

print(list2)  # [1, 5, 7, 9, 3]
print(type(list2))  # <class 'list'>

# String data type
fruits = ["apple", "banana", "cherry", "apple", "cherry"]

print(fruits)  # ['apple', 'banana', 'cherry', 'apple', 'cherry']
print(len(fruits))  # 5

# It is also possible to use the list() constructor when creating a new list.
new_list = list(("apple", "banana", "cherry"))  # note the double round-brackets

print(new_list)  # ['apple', 'banana', 'cherry']
print(type(new_list))  # <class 'list'>
