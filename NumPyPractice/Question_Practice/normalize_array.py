import numpy as np

arr = np.array([10, 30, 40, 50, 60])
normalized = (arr - np.min(arr)) / (np.max(arr) - np.min(arr))

print(normalized)