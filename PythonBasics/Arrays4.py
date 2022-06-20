from numpy import *

arr = array([1, 2, 3, 2, 4])
arr = arr + 1  # add 1 to each and every element
print(arr)  # [2 3 4 3 5]
print(sum(arr))  # 17
print(min(arr))  # 2
print(max(arr))  # 5
print(sort(arr))  # [2 3 3 4 5]
arr1 = array([1, 2, 3, 2, 4])
arr2 = array([2, 3, 4, 2, 4])
arr3 = arr1 + arr2
print(arr3)
print(concatenate([arr1, arr2]))  # print(concatenate([arr1, arr2]))

