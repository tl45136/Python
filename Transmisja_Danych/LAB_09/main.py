import numpy as np
import matplotlib.pyplot as plt


def S2BS(s):
    result = []
    for c in s:
        b = bin(ord(c))[2:]
        if len(b) < 8:
            b = '0' + b
        result.extend([int(x) for x in b])
    return result


def split(x, num):
    size = int(len(x) / num)
    x = np.array(x)
    return np.resize(x, (size, num))


def expand(bits):
    return bits.flatten()


def Hamming_encoder(d):
    shape = d.shape[0]
    enc = np.zeros((shape, 7))
    for i in range(shape):
        enc[i] = np.dot(G, d[i]) % 2
    return enc


def flipbit(bit):
    if (bit == 0):
        return 1
    else:
        return 0


def Manchester(s, f, ft):
    encode = []
    temp = np.arange(0, 1 / f / 2 / ft)
    for i in s:
        if i == 1:
            for j in temp:
                encode.append(-1)
            for j in temp:
                encode.append(1)
        else:
            for j in temp:
                encode.append(1)
            for j in temp:
                encode.append(-1)
    return encode


def dekoManchester(s, f, ft):
    decode = []
    k = 0
    isLast = False
    last = s[0]
    for i in s:
        k += 1
        if last < i:
            isLast = True
        last = i
        if k == 1 / f / ft:
            if isLast:
                decode.append(1)
            else:
                decode.append(0)
            k = 0
            last = 1
            isLast = False
    return decode


def Hamming_decoder(d):
    shape = d.shape[0]
    dec = np.zeros((shape, 4))
    for i in range(shape):
        p = np.dot(H, d[i].T) % 2
        h = int(p[0] * 2 ** 0 + p[1] * 2 ** 1 + p[2] * 2 ** 2)
        if h > 0:
            d[i, h - 1] = flipbit(d[i, h - 1])
            print(i, h)
        dec[i] = [d[i, 2], d[i, 4], d[i, 5], d[i, 6]]
    return dec


def Bit2S(b):
    c = []
    temp = 0
    s = ''
    for i in range(int(len(b) / 8)):
        c.append('')
        for j in range(8):
            c[i] = c[i] + str(int(b[temp]))
            temp += 1
        s = s + chr(int(c[i], 2))
    return s


x = S2BS('Hi')
G = np.array([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

H = np.array([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])
print(x)
# [0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
f = 10
ft = 0.01
# zad2
x = split(x, 4)
x = Hamming_encoder(x)
print(x)
# [[1. 0. 0. 1. 1. 0. 0.] [1. 1. 1. 0. 0. 0. 0.] [1. 1. 0. 0. 1. 1. 0.] [0. 0. 1. 1. 0. 0. 1.]]
x = expand(x)

x = Manchester(x, f, ft)
print(x)
# [-1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1]
time = np.arange(0, len(x), 1)
plt.plot(time, x)
plt.title("Manchester")
plt.show()

x = dekoManchester(x, f, ft)
print(x)
# [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1]
x = split(x, 7)

x = Hamming_decoder(x)
print(x)
# [[0. 1. 0. 0.][1. 0. 0. 0.][0. 1. 1. 0.][1. 0. 0. 1.]]
x = expand(x)
text = Bit2S(x)
print(text)
# Hi
