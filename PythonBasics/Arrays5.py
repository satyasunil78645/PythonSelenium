from numpy import *

arr = array([[2, 3, 4, 2, 3, 3], [2, 3, 4, 3, 6, 8]])
print(arr)
print(arr.dtype)
print(arr.ndim)
flt = arr.flatten()
print(flt)
arr2 = flt.reshape(2, 2, 3)
print(arr2)

print("----------------------------------")
m = matrix('1 2 3; 4 5 6; 1 3 5')
print(m)

print(f"diagonal {m.diagonal()}")
print(m.max())