# Set
"""" A set is a collection which is unordered, unchangeable*, and un-indexed
     Note: Set items are unchangeable, but you can remove items and add new items.
     Sets are written with curly brackets."""

# Set won't allow the duplicate values
data = {"apple", "banana", "cherry", "cherry", 10, 39, 10, 2}
print(data)  # {'apple', 'banana', 2, 'cherry', 39, 10}

animals = {"apple", "banana", "cherry"}
print(animals)

""" Once a set is created, you cannot change its items, but you can add new items. 
    To add one item to a set use the add() method """
animals.add("tiger")
print(animals)

# -------> adding item from another set into the current set
""" To add items from another set into the current set, use the update() method. """
set1 = {"apple", "banana", "cherry"}
set2 = {"pineapple", "mango", "papaya"}
set1.update(set2)
print(set1)

# -------> adding item from list into the current set
""" The object in the update() method does not have to be a set, 
    it can be any iterable object (tuples, lists, dictionaries etc.). """
test_set = {"apple", "banana", "cherry"}
my_list = ["kiwi", "orange"]

test_set.update(my_list)

# To remove an item in a set, use the remove(), or the discard() method.
test_remove = {"apple", "banana", "cherry"}
test_remove.remove("apple")
print(test_remove)  # {'banana', 'cherry'}

# The union() method returns a new set with all items from both sets:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
