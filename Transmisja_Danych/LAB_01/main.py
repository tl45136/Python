import math
import pylab as plt
import numpy as np


# 45136
# x=6t^2+3t+1

def funkcja(c, b, a):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Brak miejsca zerowego")
    elif delta == 0:
        t1 = (-b) / (2 * a)
        print("Jest jedno miejsce zerowe:")
        print(t1)
    else:
        t1 = (-b + (math.sqrt(delta))) / (2 * a)
        t2 = (-b - (math.sqrt(delta))) / (2 * a)
        print("Sa dwa miejsca zerowe:")
        print(t1)
        print(t2)
    plt.figure(figsize=(10, 8), dpi=100)
    t = np.arange(-10, 10, 0.01)
    xt = a * t ** 2 + b * t + c
    plt.xlabel('oś t')
    plt.ylabel('oś xt')
    plt.title('wykres xt=6t^2+3t+1')
    plt.plot(t, xt)
    plt.show()

    return xt


xt = funkcja(1, 3, 6)


def x(i):
    a = 6
    b = 3
    c = 1
    return a * i ** b + b * i + c


t = np.arange(0, 1, 1 / 22050)
yt = np.zeros(np.size(t))
for i in range(np.size(t)):
    yt[i] = 2 * (x(t[i]) ** 2) + 12 * np.cos(t[i])


plt.xlabel('oś t')
plt.ylabel('oś yt')
plt.title('wykres y(t) = 2*x(t)^2+12*cos(t)')
plt.plot(t, yt)
plt.show()

zt = np.zeros(np.size(t))
for i in range(np.size(t)):
    zt[i] = np.sin(2 * np.pi * 7 * t[i]) * x(t[i]) - 0.2 * np.log10(abs(yt[i]) + np.pi)
plt.xlabel('oś t')
plt.ylabel('oś zt')
plt.title('wykres z(t) = sin(2*pi*7*t)*x(t)-0.2*log10(|y(t)|+pi)')
plt.plot(t, zt)
plt.show()

ut = np.zeros(np.size(t))
for i in range(np.size(t)):
    ut[i] = np.sqrt(abs(yt[i] * yt[i] * zt[i])) - 1.8 * np.sin(0.4 * t[i] * zt[i] * x(t[i]))

plt.xlabel('oś t')
plt.ylabel('oś ut')
plt.title('wykres u(t) = sqrt(|y(t)*y(t)*z(t)|)-1.8*sin(0.4*t*z(t)*x(t)')
plt.plot(t, ut)
plt.show()

vt = np.zeros(np.size(t))
for i in range(np.size(t)):
    if 0.22 > t[i] >= 0:
        vt[i] = (1 - 7 * t[i]) * np.sin((2 * np.pi * t[i] * 10) / (t[i] + 0.04))
    elif 0.22 <= t[i] < 0.7:
        vt[i] = 0.63 * t[i] * np.sin(125 * t[i])
    else:
        vt[i] = t[i] ** (-0.662) + 0.77 * np.sin(8 * t[i])
plt.xlabel('oś t')
plt.ylabel('oś vt')
plt.title('wykres v(t)')
plt.plot(t, vt)
plt.show()
n = [2, 4, 99]
pt = np.zeros(np.size(t))
for i in range(np.size(t)):
    for j in range(1, 2):
        pt[i] += (np.cos(12 * t[i] * j ** 2) + np.cos(16 * t[i] * j)) / j ** 2

plt.xlabel('oś t')
plt.ylabel('oś pt')
plt.title('wykres p(t) dla N=2')
plt.plot(t, pt)
plt.show()
pt = np.zeros(np.size(t))
for i in range(np.size(t)):
    for j in range(1, 4):
        pt[i] += (np.cos(12 * t[i] * j ** 2) + np.cos(16 * t[i] * j)) / j ** 2

plt.xlabel('oś t')
plt.ylabel('oś pt')
plt.title('wykres p(t) dla N = 4')
plt.plot(t, pt)
plt.show()

pt = np.zeros(np.size(t))
for i in range(np.size(t)):
    for j in range(1, 63):
        pt[i] += (np.cos(12 * t[i] * j ** 2) + np.cos(16 * t[i] * j)) / j ** 2

plt.xlabel('oś t')
plt.ylabel('oś pt')
plt.title('wykres p(t) dla N=63')
plt.plot(t, pt)
plt.show()

