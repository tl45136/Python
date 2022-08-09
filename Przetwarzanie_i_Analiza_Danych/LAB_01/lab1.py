import numpy as np
from numpy.lib.stride_tricks import as_strided

# tablice
a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a)
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np.transpose(b))
print(np.arange(0, 100, 1))
print(np.linspace(0.0, 2.0, num=10))
print(np.arange(0, 100, 5))

# liczby losowe
print(np.random.normal(size=20).round(2))
print(np.random.randint(low=1, high=1000, size=100))
print(np.zeros((3, 2)))
print(np.ones((3, 2)))
print(np.random.randint(100, size=(5, 5), dtype=np.int32))
# zadanie:
r = np.random.rand(10)
s = r.astype(int)
r1 = np.round(r, 0)
s1 = r1.astype(int)
print(np.equal(r1, s1))

# Selekcja danych
c = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=np.int32)
print(c)
print(c.ndim)
print(c.size)
print(c[0, (1, 3)])
print(c[0, :])
print(c[:, 0])
m = np.random.randint(0, 100, (20, 7))
print(m[:, 0:4], "\n")
# operacje matematyczne i logiczne
e = np.random.randint(0, 10, (3, 3))
f = np.random.randint(0, 10, (3, 3))
print(np.add(e, f))
print(np.multiply(e, f))
print(np.divide(e, f))
print(np.power(e, f))
print(np.power(f, e))
print(e >= 4)
print(e <= 1)
print(e != 4)
print(np.trace(f))
# dane statystyczne
print(np.sum(f))
print(np.min(f))
print(np.max(f))
print(np.std(f))
print(np.mean(f, axis=1))
print(np.mean(f, axis=0))
# rzutowanie wyymiarow
q = np.arange(0, 50)
w = np.reshape(q, (10, 5))
print(w)
print(np.resize(q, (10, 5)))
print(w.ravel())
j = np.arange(5)
k = np.arange(4)
k = k[:, np.newaxis]
print(np.add(j, k))
# sortowanie danych
u = np.random.randn(5, 5)
print(u, '\n')
print(np.sort(u, axis=1)[::-1], '\n')
print(np.sort(u, axis=0))
p = np.array([(1, 'MZ', 'mazowieckie'), (2, 'ZP', 'zachodniopomorskie'), (3, 'ML', 'małopolskie')])
p1 = np.resize(p, (3, 3))
print(p1[p1[:, 1].argsort()])
print(p1[1, 2])

# 3 Zadania podsumujace
# 1
a1 = np.random.randint(100, size=(5, 10))
print(a1)
print(np.trace(a1))
print(np.diag(a1))
# 2
a2 = np.random.normal(size=(3, 3)).round(2)
b2 = np.random.normal(size=(3, 3)).round(2)
print(a2 * b2)
# 3
a3 = np.random.randint(low=1, high=100, size=5)
b3 = np.random.randint(low=1, high=100, size=5)
print(a3 + b3)
# 4
a4 = np.random.normal(size=(4, 5))
b4 = np.random.normal(size=(5, 4))
print(a4 + np.transpose(b4))
# 5
print(((a4[:, 2]) * (a4[:, 3])))
print(((b4[:, 2]) * (b4[:, 3])))
# 6
a6 = np.random.normal(size=10)
b6 = np.random.uniform(size=10)
print(np.mean(a6), '\n', np.mean(b6))
print(np.std(a6), '\n', np.std(b6))
print(np.var(a6), '\n', np.var(b6))
print(np.equal(np.mean(a6), np.mean(b6)))
print(np.equal(np.std(a6), np.std(b6)))
print(np.equal(np.var(a6), np.var(b6)))
# 7
a7 = np.random.normal(size=(4, 4))
b7 = np.random.normal(size=(4, 4))
print(a7 * b7, '\n')  # mnoży element przez element
print(np.dot(a7, b7))  # mnoży skalarnie
# 8
a8 = np.random.normal(size=(5, 5))
print(as_strided(a8, shape=(3, 5)))
print(a8.strides)
# 9
a9 = np.random.randint(100, size=(5, 10))
b9 = np.random.randint(100, size=(5, 10))
print(np.vstack((a9, b9)))  # łączymy tablice jedna pod drugą
print(np.hstack((a9, b9)))  # łączymy tablice jedna kolo drugiej
# 10
a0 = np.arange(0, 24).reshape(4, 6)
s1 = a0.strides[0]
s2 = a0.strides[1]
a01 = np.amax(as_strided(a0, strides=(s1, s2), shape=(2, 3)))
a02 = np.amax(as_strided(a0 + 3, strides=(s1, s2), shape=(2, 3)))
a03 = np.amax(as_strided(a0 + 12, strides=(s1, s2), shape=(2, 3)))
a04 = np.amax(as_strided(a0 + 15, strides=(s1, s2), shape=(2, 3)))
print(a01, a02, a03, a04)
