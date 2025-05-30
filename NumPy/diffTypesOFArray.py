import numpy as np
a = np.zeros((2, 3))
print(a)
b = np.ones((3, 3), dtype='int32')
print(b)
print()
c = np.full((3, 2, 4), 99)
print(c)
print()
c = np.full_like(a, 4)
print(c)
print()
c = np.full(a.shape, 3)
print(c)
print()
c = np.random.rand(4, 2, 1)
print(c)
print()
c = np.random.random_sample(a.shape)
print(c)
print()
c = np.random.randint(7, size=(3, 2))  # 7--> 0 to 6
print(c)
print()
c = np.identity(3)
print(c)
print()
arr = [1, 2, 3]
r1 = np.repeat(arr, 3)
print(r1)
print()
arr = [[1, 2, 3]]
r1 = np.repeat(arr, 3, axis=0)
print(r1)
