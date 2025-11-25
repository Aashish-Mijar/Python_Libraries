"""
 slicing 
 array[start:stop:step]
 negative step, -1  reverse
"""
import numpy as np

arr = np.array([2,3,6,74,12,34])

print(arr[1:5])
print(arr[:4])
print(arr[::2])
print(arr[::-1])