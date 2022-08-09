import numpy as np
import pylab as plt


def clock(t, f, ft):
    clk = []
    temp = np.arange(0, 1 / f / 2 / ft)
    for i in np.arange(0, t, 1 / f):
        for j in temp:
            clk.append(1)
        for j in temp:
            clk.append(0)
    return clk


def S2BS(s):
    result = []
    for c in s:
        bit = bin(ord(c))[2:]
        if len(bit) < 8:
            bit = '0' + bit
        result.extend([int(x) for x in bit])
    return result


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


t = 1.6
f = 10
ft = 0.01
input = S2BS('hi')

print(input)
# [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]

czas = np.arange(0, t, ft)
clk = clock(t, f, ft)
plt.subplot(2,1,1)
plt.plot(czas, clk)
plt.title("Clock")

plt.subplot(2,1,2)
man = Manchester(input, f, ft)
plt.plot(czas, man)
plt.title("Manchester")
plt.show()

output = dekoManchester(man, f, ft)

print(output)
# [0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1]
