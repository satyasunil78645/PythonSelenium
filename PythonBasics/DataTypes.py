print("------------------- Integer -------------------")
value = 1
value += 2
print(value)  # 3

print(2 + 3)  # 5

# type function - prints type of the variable
print(type(2 + 3))  # <class 'int'>

print(type(0.5))  # <class 'float'>

num = 10 > 5  # True
print(num)

# String - we can define string with single or double quotes
name = 'Satya sunil'
print(len(name))
print(name[0])  # S
print(name[-1])  # l
print(name[6:11])  # Sunil
print(name[6:15])  # Sunil
print(name[1:])  # atya sunil
print(name[:5])  # Satya
print(name[::-1])  # reverse the order - linus aytaS
print(name[0:6:2])  # [start: stop: step over] - Sta


# String methods
quote = 'it is not a joke'
print(quote.upper())  # IT IS NOT A JOKE
print(quote.capitalize())  # It is not a joke
print(quote.lower())  # it is not a joke
print(quote.replace('not', ' '))  # it is   a joke

# -------
Name = 'John'
age = 25
print(f'hi {Name} you are {age} years old')  # hi John you are  25 years old
print('hi {} you are {} years old'.format(Name, age))  # hi John you are  25 years old


# Conversions
# int to string
age = 35
age_as_string = str(35)

# Boolean
print(bool(35))  # true
print(bool("Rolf"))  # true
print(bool(0))  # false
print(bool(""))  # false


