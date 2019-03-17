import numpy as np

a = np.array([0, 1, 2, 3, 4, 5, 6])

print(a.size)
print(a.ndim)

u = [1, 0]
v = [0, 1]

z = []
for n, m in zip(u, v):
    z.append(n - m)

print(z)

p = np.array([0, 1])
q = np.array([1, 0])

r = p - q

print(r)

s = np.array([0, 1])

r = 2 * s

print(r)

p = np.array([0, 1])
q = np.array([1, 0])

r = p * q

print(r)

p = np.array([2, 3])
q = np.array([1, 2])

r = np.dot(p, q)

print(r)

print(np.array([1, -1]) * np.array([1, 1]))

print(np.dot(np.array([1, -1]), np.array([1, 1])))
