import numpy as np
import matplotlib.pyplot as plt

A = 6
B = 3
C = 1
a = 1.0
f = B
fi = C * np.pi


def DFT(n):
    xk = []
    for i in range(len(n)):
        temp = 0
        for j in range(len(n)):
            temp += n[j] * np.exp(1j * 2 * np.pi / len(n)) ** (-i * j)
        xk.append(temp)
    return xk


def sygnal(t):
    return a * np.sin(2 * np.pi * f * t)


def mAmplitudy(kA, f, t):
    return (kA * sygnal(t) + 1) * np.cos(2 * np.pi * 10 * f * t)


def mFazy(kP, f, t):
    return np.cos(2 * np.pi * 10 * f * t + kP * sygnal(t))


def M(x):
    temp = []
    for i in range(0, len(np.real(x))):
        temp.append(np.sqrt(np.real(x[i]) ** 2 + np.imag(x[i]) ** 2))
    return temp


def pasmo(x):
    fmax = max(x)
    fmin = min(i for i in x if i > 0)
    W = fmax - fmin
    print("Maximum: ", fmax)
    print("Minimum: ", fmin)
    print("W: ", W)


t = np.arange(0, 1, 0.001)
plt.plot(t, sygnal(t))
plt.title("Sygnal informacyjny")
plt.show()

plt.subplot(2, 1, 1)
plt.plot(t, mAmplitudy(0.4, f, t))
plt.title("Modulacja amplitudy dla kA = 0.4")
plt.subplot(2, 1, 2)
plt.plot(t, mFazy(1.5, f, t))
plt.title("Modulacja fazy dla kP = 1.5")
plt.show()

plt.subplot(2, 1, 1)
plt.plot(t, mAmplitudy(3, f, t))
plt.title("Modulacja amplitudy dla kA = 3")
plt.subplot(2, 1, 2)
plt.plot(t, mFazy(1, f, t))
plt.title("Modulacja fazy dla kP = 1")
plt.show()

plt.subplot(2, 1, 1)
plt.plot(t, mAmplitudy(37, f, t))
plt.title("Modulacja amplitudy dla kA = BA+1")
plt.subplot(2, 1, 2)
plt.plot(t, mFazy(64, f, t))
plt.title("Modulacja fazy dla kP = AB+1")
plt.show()

# t = np.arange(0,1,0.001)
t = np.linspace(0, 1, 500)
plt.subplot(2, 1, 1)
plt.plot(t, M(DFT(mAmplitudy(0.4, f, t))))
plt.title("Modulacja amplitudy dla kA = 0.4")
plt.subplot(2, 1, 2)
plt.plot(t, M(DFT(mFazy(1.5, f, t))))
plt.title("Modulacja fazy dla kP = 1.5")
plt.show()

plt.subplot(2, 1, 1)
plt.plot(t, M(DFT(mAmplitudy(3, f, t))))
plt.title("Modulacja amplitudy dla kA = 3")
plt.subplot(2, 1, 2)
plt.plot(t, M(DFT(mFazy(1, f, t))))
plt.title("Modulacja fazy dla kP = 1")
plt.show()

plt.subplot(2, 1, 1)
plt.plot(t, M(DFT(mAmplitudy(37, f, t))))
plt.title("Modulacja amplitudy dla kA = BA+1")
plt.subplot(2, 1, 2)
plt.plot(t, M(DFT(mFazy(64, f, t))))
plt.title("Modulacja fazy dla kP = AB+1")
plt.show()

# A1 = mAmplitudy(0.4, f, t)
# F1 = mFazy(1.5, f, t)
# A2 = mAmplitudy(3, f, t)
# F2 = mFazy(1, f, t)
# A3 = mAmplitudy(37, f, t)
# F3 = mFazy(64, f, t)
#
# pasmo(A1)
# pasmo(F1)
# pasmo(A2)
# pasmo(F2)
# pasmo(A3)
# pasmo(F3)

# kA = 0.4
# Maximum:  1.3804226065180614
# Minimum:  1.572375224777654e-16
# W:  1.3804226065180611
#
# kP = 1.5
# Maximum:  1.0
# Minimum:  0.012835451067674902
# W:  0.9871645489323251
#
# kA = 3
# Maximum:  3.853169548885461
# Minimum:  2.881228256826616e-15
# W:  3.8531695488854583
#
# kP = 1
# Maximum:  1.0
# Minimum:  0.004379664425653673
# W:  0.9956203355743464
#
# kA = 37
# Maximum:  36.189091102920685
# Minimum:  2.348444116120549e-15
# W:  36.189091102920685
#
# kP = 64
# Maximum:  1.0
# Minimum:  0.008231128194089762
# W:  0.9917688718059102
