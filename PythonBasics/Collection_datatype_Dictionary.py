""" Dictionary:
    - Dictionaries are used to store data values in key:value pairs
    - A dictionary is a collection which is unordered, changeable and do not allow duplicates."""
from webbrowser import get

car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": ["red", "white", "blue"]
}
print(car_details)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': ['red', 'white', 'blue']}
print(car_details["brand"])  # Ford
# There is also a method called get() that will give you the same result:
print(car_details.get('model'))
print(car_details["color"][1])  # white
print(len(car_details))  # 3

car_details['year'] = 1900
print(car_details)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1900, 'color': ['red', 'white', 'blue']}

# ----------- Access Items -----------
x = car_details.get('year')
print('year ' + str(x))  # year 1900
print(f'year {x}')  # year 1900

# get list of keys
k = car_details.keys()
print(f'Total keys {k}')  # Total keys dict_keys(['brand', 'model', 'year', 'color'])

# Add new item to the dictionary
car_details['place'] = 'Hyderabad'
print(car_details.keys())  # dict_keys(['brand', 'model', 'year', 'color', 'place'])

# Update the place
car_details.update({'place': 'Bangalore'})
print(car_details['place'])  # Bangalore

# get all the list of values
print(car_details.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1900), ('color', ['red',
# 'white', 'blue']), ('place', 'Bangalore')])


# check the key condition
if 'model' in car_details:
    print('Yes details are there in the list')

# --> The pop() method removes the item with the specified key name:
car_details.pop('place')
print(car_details)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1900, 'color': ['red', 'white', 'blue']}

# --> The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
car_details['speed'] = 400
print(car_details)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1900, 'color': ['red', 'white', 'blue'],
# 'speed': 400}
car_details.popitem()
print(car_details)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 1900, 'color': ['red', 'white', 'blue']}

# --> The clear() method empties the dictionary:
""" car_details.clear() --> clear the dictionary object
print(car_details)  # {}"""

# --> Loop (Print all values in the dictionary, one by one:)
print("For loop starting ")
for x in car_details:
    print(car_details[x])  # Print all values in the dictionary, one by one:

print("you can use the keys() method to return the keys of a dictionary:")
for x in car_details.keys():
    print(x)

# --> copy of the dictionary
# 1st way
print("1st way to copy of the current dictionary ")
new_dictionary = car_details.copy()
print(new_dictionary)

# 2nd way to copy the dictionary is use dict() method to copy it
print("2nd way to copy of the current dictionary ")
new_dictionary1 = dict(car_details)
print(new_dictionary1)
