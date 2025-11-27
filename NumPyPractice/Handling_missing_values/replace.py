import numpy as np

# np.isinf() 10^1000
#1/0

arr = np.array([1,2,np.inf,4, -np.inf, 8])
print(np.isinf(arr))
cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf = -1000)
print(cleaned_arr)