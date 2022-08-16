import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import sounddevice as sd
import soundfile as sf
from scipy.interpolate import interp1d
import math


def kwant(x, bit):
    xtype = x.dtype
    if x.dtype == np.float32:
        m = -1
        n = 1
    else:
        m = np.iinfo(xtype).min
        n = np.iinfo(xtype).max
    x = x.astype(np.float32)
    Za = (x - m) / (n - m)
    Zb = Za * (2 ** bit - 1)
    Zb = np.round(Zb)
    Za = Zb / (2 ** bit - 1)
    Zc = (Za * (n - m)) + m
    return Zc.astype(xtype)


def decy(x, fs, n):
    return x[::int(fs/n)]


def interp(x, fs, new_fs, metoda):
    T = (x.size - 1) / fs
    t = np.linspace(0, T, x.size)
    t1 = np.linspace(0, T, np.ceil(T * new_fs).astype(int))
    met_int = interp1d(t, x, kind=metoda)
    return met_int(t1)


def plotingKwan(data, fs, title):
    for i in range(len(bits)):
        plt.subplot(int(len(bits) / 2), 2, i + 1)
        plt.suptitle("Widmo w skali decybelowej dla " + title)

        sound = kwant(data, bits[i])
        yf = scipy.fftpack.fft(sound, new_fs)

        plt.plot(np.arange(0, fs / 2, fs / new_fs), 20 * np.log10(np.abs(yf[:new_fs // 2])))
        plt.title("Kwantyzacja: " + str(bits[i]) + " bitowa")
    plt.show()


def plotingDecy(data, fs, title):
    for i in range(len(freq)):
        plt.subplot(int(len(freq) / 2), 2, i + 1)
        plt.suptitle("Widmo w skali decybelowej dla" + title)

        sound = decy(data, fs, freq[i])
        yf = scipy.fftpack.fft(sound, new_fs)

        plt.plot(np.arange(0, freq[i] / 2, freq[i] / new_fs), 20 * np.log10(np.abs(yf[:new_fs // 2])))
        plt.title("Decymacja dla czestotliwosci " + str(freq[i]) + " Hz")
    plt.show()


def plotingInterp(data, fs, title, metoda):
    freqs = freq + [16950]
    for i in range(len(freqs)):
        plt.subplot(math.ceil(len(freqs) / 2), 2, i + 1)
        plt.subplots_adjust(hspace=0.5)
        plt.suptitle("Widmo w skali decybelowej dla " + title)

        if metoda == 'linear':
            sound = interp(data, fs, freqs[i], 'linear')
            sub_title = "liniowa"
        else:
            sound = interp(data, fs, freqs[i], 'cubic')
            sub_title = "nieliniowa"

        yf = scipy.fftpack.fft(sound, new_fs)

        plt.plot(np.arange(0, freqs[i] / 2, freqs[i] / new_fs), 20 * np.log10(np.abs(yf[:new_fs // 2])))
        plt.title("Interpolacja " + sub_title + " dla czestotliwosci " + str(freqs[i]) + " Hz")
    plt.show()


# x = np.arange(np.iinfo(np.int16).min, np.iinfo(np.int16).max, 100, dtype=np.int16)
# data, fs = sf.read('sin_60Hz.wav', dtype=np.int32)
# data, fs = sf.read('sin_440Hz.wav', dtype=np.int32)
# data, fs = sf.read('sin_8000Hz.wav', dtype=np.int32)
# print(data)
bits = [4, 8, 16, 24]
new_fs = 2 ** 8
freq = [2000, 4000, 8000, 16000, 24000, 41000]

# Plotowanie Kwantyzacja
# plotingKwan(data,fs,'sinus 60 Hz')
# plotingKwan(data,fs,'sinus 440 Hz')
# plotingKwan(data,fs,'sinus 8000 Hz')

# Plotowanie Decymacja
# plotingDecy(data, fs, 'sinus 60hz')
# plotingDecy(data, fs, 'sinus 440hz')
# plotingDecy(data, fs, 'sinus 8000hz')

# Plotowanie Interpolacja liniowa
# plotingInterp(data,fs,'sinus 60hz', 'linear')
# plotingInterp(data,fs,'sinus 440hz', 'linear')
# plotingInterp(data,fs,'sinus 8000hz', 'linear')

# Plotowanie Interpolacja nieliniowa
# plotingInterp(data,fs,'sinus 60hz', 'cubic')
# plotingInterp(data,fs,'sinus 440hz', 'cubic')
# plotingInterp(data,fs,'sinus 8000hz', 'cubic')

data, fs = sf.read('sing_high1.wav', dtype=np.int32)
#data, fs = sf.read('sing_medium1.wav', dtype=np.int32)
#data, fs = sf.read('sing_low1.wav', dtype=np.int32)

kwantyzacja = "Kwantyzacja"
bitowa = "bitowa"

# for i in range(len(bits)):
#     print(kwantyzacja, bits[i], bitowa)
#     sd.play(kwant(data, bits[i]))
#     sd.wait()

decymacja =  "decymacja dla"
czesto = "hz"

# for i in range(len(freq)):
#     print(decymacja, freq[i], czesto)
#     sd.play(decy(data, fs, freq[i]))
#     sd.wait()

inter = "interpolacja liniowa dla"
#
# for i in range(len(freq)):
#     print(inter, freq[i], czesto)
#     sd.play(interp(data,fs,freq[i],'cubic'))
#     sd.wait()

