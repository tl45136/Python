import numpy as np


def S2BS(s):
    result = []
    for c in s:
        b = bin(ord(c))[2:]
        if len(b) < 8:
            b = '0' + b
        result.extend([int(x) for x in b])
    return result


def split(x):
    size = int(len(x) / 4)
    x = np.array(x)
    return np.resize(x, (size, 4))


def flipbit(b):
    if (b == 0):
        return 1
    else:
        return 0


def Hamming_encoder(d):
    shape = d.shape[0]
    enc = np.zeros((shape, 7))
    for i in range(shape):
        enc[i] = np.dot(G, d[i]) % 2
    return enc


def Hamming_decoder(d):
    shape = d.shape[0]
    dec = np.zeros((shape, 4))
    for i in range(shape):
        p = np.dot(H, d[i].T) % 2
        h = int(p[0] * 2 ** 0 + p[1] * 2 ** 1 + p[2] * 2 ** 2)
        if (h > 0):
            d[i, h - 1] = flipbit(d[i, h - 1])
            print(i, h)
        dec[i] = [d[i, 2], d[i, 4], d[i, 5], d[i, 6]]
    return dec


G = np.array([[1, 1, 0, 1], [1, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

H = np.array([[1, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 0, 1, 1], [0, 0, 0, 1, 1, 1, 1]])

x = S2BS('hi')
# w całości: [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
x = split(x)
# podzielone: [[0 1 1 0] [1 0 0 0] [0 1 1 0] [1 0 0 1]]
x = Hamming_encoder(x)
# zakodowane:[[1. 1. 0. 0. 1. 1. 0.] [1. 1. 1. 0. 0. 0. 0.] [1. 1. 0. 0. 1. 1. 0.] [0. 0. 1. 1. 0. 0. 1.]]
# negujemy bity na pozycjach:
# 0 4
# 1 4
# 2 4
# 3 4
for i in range(int(len(x))):
    x[i, 3] = flipbit(x[i, 3])
x = Hamming_decoder(x)
# odkodowane: [[0. 1. 1. 0.] [1. 0. 0. 0.] [0. 1. 1. 0.] [1. 0. 0. 1.]]
