def functions(a, b):
    c = a + b
    d = a * b
    return c, d


a, b = functions(1, 3)
print(a)
print(b)

print("-------------------------------")


def person(name, age):
    print(name)
    print(age)


person(age='12', name='satya')
