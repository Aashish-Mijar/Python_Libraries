import numpy as np

a = np.array([1,3,4])
b = np.array([6,7,8])

# Vertical stacking
vertical = np.vstack((a, b))

# Horizontal stacking
horizontal = np.hstack((a, b))

print("Vertical:\n", vertical)

print("Horizontal:\n", horizontal)