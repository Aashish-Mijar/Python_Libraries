"""
np.delete(array, index, axis = None)
flattern array
"""

import numpy as np

arr = np.array([2,7,43,65,23])
print(arr)
new_arr = np.delete(arr, 0)
print(new_arr)
