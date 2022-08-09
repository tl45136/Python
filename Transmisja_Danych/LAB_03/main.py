import numpy as np
import matplotlib.pyplot as plt
import math as m
import cmath


# 1
def DFT(k):
    tab = []
    wn = np.exp(1j * 2 * np.pi / len(k))
    for i in range(len(k)):
        s = 0
        for j in range(len(k)):
            s += k[j] * wn ** (-i * j)
        tab.append(s)
    return tab
    # n = len(x)
    # xk = []
    # wn = 2j * cmath.pi / n
    # for k in range(n):
    #     y = complex(0)
    #     for t in range(n):
    #         y += x[t] * np.exp(wn) ** (- k * t)
    #     xk.append(y)
    # return xk


# 2
A = 6
B = 3
C = 1
D = 5
E = 4
t = np.linspace(0, 631)


def Ton(n):
    Fi = C * np.pi
    return 1 * np.sin(2 * np.pi * B * t + Fi)


plt.subplot(1, 2, 1)
plt.plot(t, Ton(t), 'g', label='Ton Prosty')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(t, DFT(Ton(t)), 'b', label='DFT Tonu Prostego')
plt.legend()
plt.show()


def M(x):
    Re = np.real(x)
    Im = np.imag(x)
    mk = []
    for i in range(0, len(Re)):
        mk.append(np.sqrt(Re[i] ** 2 + Im[i] ** 2))
    return mk


def M_pri(x):
    return 10 * np.log10(x)


def skala(x, fs):
    n = len(x)
    fk = []
    for k in range(n):
        fk.append(k * (fs / n))
    return fk
    # n = np.size(x)
    # fk = np.zeros(np.size(x))
    # for k in range(n):
    #     fk[k] += k * (fs / n)
    # return fk


plt.plot(skala(DFT(Ton(t)), 631), M_pri(M(DFT(Ton(t)))))
plt.show()


def x(t):
    return A * t ** B + B * t + C


def y(t):
    return 2 * x(t) ** 2 + 12 * np.cos(t)


def z(t):
    return np.sin(2 * m.pi * 7 * t) * x(t) - 0.2 * np.log10(np.abs(y(t)) + (m.pi))


def u(t):
    return np.sqrt(np.abs(y(t) * y(t) * z(t))) - 1.8 * np.sin(0.4 * t * z(t) * x(t))


def v(x):
    tab = []
    for t in x:
        if (t < 0.22) and (t >= 0):
            tab.append((1 - 7 * t) * np.sin((2 * np.pi * t * 10) / (t + 0.04)))
        if (t >= 0.22) and (t < 0.7):
            tab.append(0.63 * t * np.sin(125 * t))
        if (t <= 1) and (t >= 0.7):
            tab.append((t ** (-0.662)) + 0.77 * np.sin(8 * t))
    return tab
    # if (t < 0.22) and (t >= 0):
    #     return (1 - 7 * t) * np.sin((2 * m.pi * t * 10) / (t + 0.04))
    # if (t >= 0.22) and (t < 0.7):
    #     return 0.63 * t * np.sin(125 * t)
    # if (t <= 1) and (t >= 0.7):
    #     return (t ** (-0.662)) + 0.77 * np.sin(8 * t)


def p(t, N):
    temp = 0
    for n in np.arange(1, N + 1):
        temp += ((np.cos(12 * t * n ** 2) + np.cos(16 * t * n)) / n ** 2)
    return temp


# t = np.arange(0, 10, 0.1)
# plt.plot(skala(x(t), 631), DFT(x(t)))
# plt.show()
# plt.plot(skala(y(t), 631), DFT(y(t)))
# plt.show()
# plt.plot(skala(z(t), 631), DFT(z(t)))
# plt.show()
# plt.plot(skala(u(t), 631), DFT(u(t)))
# plt.show()
# t = np.arange(0, 10, 0.1)
t1 = np.arange(0, 631, 0.1)
vt = v(t1)
X = DFT(vt)
M = M(X)
M_prim = M_pri(M)
fk = skala(X, 631)
plt.plot(fk, M_prim)
plt.show()

# plt.plot(skala(p(t, 2), 631), M_pri(M(DFT(p(t,2)))))
# plt.show()
t = np.arange(0, 10, 0.1)
pt2 = p(t, 2)
X = DFT(pt2)
M = M(X)
M_prim = M_pri(M)
fk = skala(X, 10)
plt.plot(fk, M_prim)
plt.title('Zad3 wykres widma amplitudowego dla p(t) n=2')
plt.show()
