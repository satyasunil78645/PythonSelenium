from array import *

arr = array('i', [])
n = int(input("Enter the length of the Array: "))

for i in range(n):
    x = int(input("Enter next number:"))
    arr.append(x)
print(arr)
print(f'0 index value is {arr[0]}')

val = int(input("Enter an array value to find index : "))
k = 0
for i in arr:
    if i == val:
        print(f'array value ==> {val} index is ==> {k} ')
        break
    else:
        print("Not a valid index")
    k += 1

