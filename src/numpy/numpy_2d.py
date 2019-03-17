import numpy as np

A = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7], [7, 8, 9]])

B = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])

C = np.dot(A, B)

print(C)
print(np.shape(C))
print(C.T)

a = np.array([0, 1, 0, 1, 0])

b = np.array([1, 0, 1, 0, 1])

print(a * b)

a = np.array([0, 1])

b = np.array([1, 0])

print(np.dot(a, b))

a = np.array([1, 1, 1, 1, 1])

print(a + 10)
