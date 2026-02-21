import numpy as np

arr = np.array([10, np.nan, 30, np.nan, 50])

arr = np.nan_to_num(arr, nan = 0)

print(arr)