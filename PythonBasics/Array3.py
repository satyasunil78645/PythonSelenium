from numpy import *
"""
- To work on multi dimensional array, we use numpy package
- numpy package is an 3rd party package, we can download with pip command
- Command is (Pip3 - 3 is version )--> pip3 install numpy 
- run this command in command prompt """
arr3 = array([[2, 3, 4], [2, 3, 4]])
print(arr3)

arr = array([1, 2, 3, 3, 1, 2, 3.2], int)  # no need to declare the data type like 'i'
print(arr.dtype)
print(arr)  # [1 2 3 3 1 2 3]


arr1 = array([1, 2, 3, 3, 1, 2, 3.2])  # -> convert all values into float if any one value is float number
print(arr1)  # [1.  2.  3.  3.  1.  2.  3.2]
print(arr1.dtype)  # float64

arange_1 = arange(1, 15, 2)  # 1 to 15 is the range, 2 is the difference b/w numbers
print(arange_1)  # [ 1  3  5  7  9 11 13]
