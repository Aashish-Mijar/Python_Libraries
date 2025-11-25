import numpy as np

arr_1d = np.array([3,4,5])
arr_2d = np.array([[3,4,5],[7,8,9]])
arr_3d = np.array([[[3,4,5],[5,7,8],[9,6,8]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)