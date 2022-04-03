a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# --> single line If statement
if a > b: print("a is greater than b")

# --> logical operators And & or
a = 200
b = 33
c = 500
if (a > b) and (c > a):
    print("Both conditions are True")

if a > b or a > c:
    print("At least one of the conditions is True")

# --> Nested if
x = 39
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
else:
    print("Not above 10")
