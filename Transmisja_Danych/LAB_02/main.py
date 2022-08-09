import numpy as np
import matplotlib.pyplot as plt


def TonProsty(A, f, Fi, t):
    return A * np.sin(2 * np.pi * f * t + Fi)


def Kwantyzacja(q, Y):
    return Y / (2 / (2 ** q))


t = np.arange(0, 6, 0.01)
x = np.zeros(np.size(t))
y = np.zeros(np.size(t))
for i in range(np.size(t)):
    x[i] = TonProsty(1, 3, 1 * np.pi, t[i])
    y[i] = Kwantyzacja(16, TonProsty(1, 3, 1 * np.pi, t[i]))

plt.step(t, x)
plt.title("Ton Prosty")
plt.show()
plt.step(t, y)
plt.title("Kwantyzacja")
plt.show()
t = np.arange(0, 6, 0.005)
z = np.zeros(np.size(t))
for j in range(np.size(t)):
    z[j] = Kwantyzacja(8, TonProsty(1, 3, 1 * np.pi, t[j]))


plt.step(t, z)
plt.title("Kwantyzacja z q=8")
plt.show()
