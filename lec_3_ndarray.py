import numpy as np

a = np.zeros((2, 3))
print(a)

a[0, 2] = 5
print(a)

b = np.ones((3, 2))
print(b)

c = np.ndarray((3, 2))
print(c)

print(type(a), type(b), type(c))