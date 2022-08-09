import numpy as np
import pylab as plt


def S2BS(s):
    result = []
    for c in s:
        bit = bin(ord(c))[2:]
        if len(bit) < 8:
            bit = '0' + bit
        result.extend([int(x) for x in bit])
    return result


def za1(A1, f, t, phi):
    return A1 * np.sin(2 * np.pi * f * t + phi)


def za2(A2, f, t, phi):
    return A2 * np.sin(2 * np.pi * f * t + phi)


def DFT(n):
    xk = []
    for i in range(len(n)):
        temp = 0
        for j in range(len(n)):
            temp += n[j] * np.exp(1j * 2 * np.pi / len(n)) ** (-i * j)
        xk.append(temp)
    return xk


def M(x):
    Re = np.real(x)
    Im = np.imag(x)
    mk = []
    for i in range(0, len(Re)):
        mk.append(np.sqrt(Re[i] ** 2 + Im[i] ** 2))
    return mk



def sygASK():
    N = 1 / Tb
    f = N / Tb
    ASK = []
    for t in czas:
        if x[int(t)] == 0:
            ASK.append(za1(A1, f, t, phi))
        else:
            ASK.append(za2(A2, f, t, phi))
    return ASK


def widmoASK():
    N = 2
    f = N / Tb
    wASK = []
    for t in czas2:
        if x[int(t)] == 0:
            wASK.append(za1(A1, f, t, phi))
        else:
            wASK.append(za2(A2, f, t, phi))
    return wASK


x = S2BS('text')
print(x)
# [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0]
A1 = 1
A2 = 0
Tb = 1
phi = 0
czas = np.arange(0, len(x), 0.1)
czas2 = np.arange(0, 10, 0.1)

ASK = sygASK()
wASK = widmoASK()
plt.plot(czas, ASK)
plt.title("Zad2 dla ASK")
plt.xlabel('czas')
plt.show()

plt.plot(czas2, wASK)
plt.title("Zad3 dla ASK")
plt.xlabel('czas')
plt.show()

plt.plot(czas, M(DFT(ASK)))
plt.title("Zad4 Widmo dla ASK")
plt.show()

max = np.max(ASK)
min = np.min(ASK)
w = max - min
print(w)
# W = 1.9021130325903224
