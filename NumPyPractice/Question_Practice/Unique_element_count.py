import numpy as np

arr = np.array([1,2,3,3,3,2,2,4,5])

unique, counts = np.unique(arr, return_counts = True)

print("Unique Values: ", unique)
print("Counts: ", counts)