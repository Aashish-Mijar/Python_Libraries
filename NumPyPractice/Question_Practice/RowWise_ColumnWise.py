import numpy as np

arr = np.array([[1,3,4],[5,6,7]])

# Column-wise sum
print("Column Sum:", np.sum(arr, axis = 0))

# Row-wise sum
print("Row Sum: ", np.sum(arr, axis = 1))
