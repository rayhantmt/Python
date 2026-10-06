import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Element-wise:\n", A * B)
print("Matrix multiply:\n", A @ B)