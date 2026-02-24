import numpy as np

A = np.array([[2,1],[1,1]])

B = np.array([5,3])

solution = np.linalg.solve(A, B)

print("Solution (x, y): ", solution)