import numpy as np

a1 = np.array([5, 4, 3, 8])
print(a1)
print(a1.shape)

a2 = np.array(((4, 8, 10, 5), (5, 7, 3, 6), (4, 8, 10, 6)))
print(a2)
print(a2.shape)
a2.shape = (4, 3)
print(a2)
a2.shape = 2, -1
print(a2)

print(np.arange(0, 1, 0.2))
print(np.linspace(0, 1, 5))
print(np.geomspace(1, 10, 5))

print(np.zeros((3, 4)))
print(np.ones((2, 2, 3)))
print(np.ones((2, 2, 3)))
print(np.diag((4, 8, 5)))
print(np.random.random(5))
print(np.random.rand(5))
print(np.random.randn(5))

print(a2.dtype)
print(np.array([5, 4, 3, 8], dtype=np.complex128))
print(np.array([4, 8, 10, 5], dtype=np.float64))
print(np.array([4, 8, 10, 5], dtype='d').dtype)

print(set(np.sctypeDict.values()))

a = np.arange(12)
print(a[2], a[-2])

print(a[3:8])
print(a[:8])
a[3:5] = 90, 91
print(a[:-1])

print(a[::2])
print(a[::-1])
