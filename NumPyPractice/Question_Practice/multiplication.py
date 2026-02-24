import numpy as np

A = np.array([[1,2],[3,5]])

B = np.array([[6,7],[9,7]])

# Matrix multiplication
result = np.matmul(A, B)

# OR
# result = A @ B

print(result)

# Formula -- C[i][j] = Sum of A[i][k] * B[k][j]