# dictionary can contain dictionaries, this is called nested dictionaries.
my_family = {
    "child1": {
        "name": "Emil",
        "year": 1992
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(my_family["child1"])
print(my_family['child1']['name'])
print(my_family.get('child1').get('name'))

# if you want to add three dictionaries into a new dictionary:
Emp1 = {
    "name": "Emil",
    "year": 2004
}
Emp2 = {
    "name": "Tobias",
    "year": 2007
}
Emp3 = {
    "name": "Linus",
    "year": 2011
}

Employee_dict = {
    "Emp1": Emp1,
    "Emp2": Emp2,
    "Emp3": Emp3,
    "Emp4": my_family["child1"]
}
# print(Employee_dict)
print(Employee_dict['Emp1']['name'])
print(Employee_dict.get('Emp1').get('name'))