import numpy as np

arr_2d = np.array([[1,2],[4,5]])

#insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5,7], axis=0)

print(new_arr_2d)