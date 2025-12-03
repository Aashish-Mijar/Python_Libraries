"""
np.insert(array, index, value, axis=None)
array - original array
index -
value -
axis -
axis = 0, row-wise
1 column wise
"""

import numpy as np

arr = np.array([10, 20,40,50,20])
print(arr)
new_arr = np.insert(arr, 2, 100, axis=0)
print(new_arr)

