import numpy as np

# np.nan_to_num(array, nan=value) default - 0

arr = np.array([1,2,np.nan, 3, 4, np.nan, 6])
cleaned_arr = np.nan_to_num(arr, nan=100)
print(cleaned_arr)
