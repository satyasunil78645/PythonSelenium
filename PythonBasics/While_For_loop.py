# while
""" Wth the while loop we can execute a set of statements as long as a condition is true """

# Exit the loop when i is 3:
print("-------break--------")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue to the next iteration if i is 3:
print("-------Continue--------")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

""" With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc. """
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

for x in range(6):
    print(x)

for x in range(10, 21):
    print(x)

# -->  Increment the sequence with 3 (default is 1):
for x in range(2, 10, 2):  # Increment the sequence by 2
    print(x)  # 2 4 6 8
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
