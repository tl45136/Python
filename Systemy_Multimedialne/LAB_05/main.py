import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import soundfile as sf

A = 87.6


def quantization(x, bit):
    xtype = x.dtype
    if np.issubdtype(x.dtype, np.floating):
        m = -1
        n = 1
    elif np.issubdtype(x.dtype, np.integer):
        m = np.iinfo(xtype).min
        n = np.iinfo(xtype).max
    x = x.astype(np.float32)
    Za = (x - m) / (n - m)
    Zb = Za * (2 ** bit - 1)
    Zb = np.round(Zb)
    Za = Zb / (2 ** bit - 1)
    Zc = (Za * (n - m)) + m
    return Zc.astype(xtype)


def aLawCompression(sound):
    x = np.zeros(sound.shape[0])
    idx = np.abs(sound) < 1 / A
    x[idx] = np.sign(sound[idx]) * (A * np.abs(sound[idx]) / (1 + np.log(A)))
    x[~idx] = np.sign(sound[~idx]) * ((1 + np.log(A * np.abs(sound[~idx]))) / (1 + np.log(A)))
    return x


def aLawDecompression(sound):
    y = np.zeros(sound.shape[0])
    idx = np.abs(sound) < 1 / (1 + np.log(A))
    y[idx] = np.sign(sound[idx]) * ((np.abs(sound[idx]) * (1 + np.log(A))) / A)
    y[~idx] = np.sign(sound[~idx]) * (np.exp(np.abs(sound[~idx]) * (1 + np.log(A)) - 1) / A)
    return y


def DPCMcompression(sound, bits):
    output = np.zeros(sound.shape[0])
    output[0] = sound[0]
    E = sound[0]
    for i in range(1, len(sound)):
        output[i] = quantization(sound[i] - E, bits)
        E += output[i]
    return output


def DPCMdecompression(sound):
    output = np.zeros(sound.shape[0])
    output[0] = sound[0]
    for i in range(1, len(sound)):
        output[i] = output[i - 1] + sound[i]
    return output


def plotAlaw():
    x = np.linspace(-1, 1, 1000)

    aLawComp = aLawCompression(x)

    aLawCompQuant = np.zeros(aLawComp.shape[0])
    for i in range(aLawComp.shape[0]):
        aLawCompQuant[i] = quantization(aLawComp[i], 8)

    aLawDecomp = aLawDecompression(aLawCompQuant)
    plt.subplot(1, 4, 1)
    plt.title("Oryginal")
    plt.plot(x, x)
    plt.subplot(1, 4, 2)
    plt.title("Kompresja a-law")
    plt.plot(x, aLawComp)
    plt.subplot(1, 4, 3)
    plt.title("Kompresja a-law po kwantyzacji do 8-bitow")
    plt.plot(x, aLawCompQuant)
    plt.subplot(1, 4, 4)
    plt.title("Dekompresja a-law")
    plt.plot(x, aLawDecomp)
    plt.show()


def plotDPCM():
    x = np.linspace(-1, 1, 1000)
    y = 0.9 * np.sin(np.pi * x * 4)

    dpcmComp = DPCMcompression(y, 8)
    dpcmDecomp = DPCMdecompression(dpcmComp)

    plt.subplot(1, 3, 1)
    plt.title("Oryginal")
    plt.plot(x, y)
    plt.subplot(1, 3, 2)
    plt.title("Kompresja DPCM")
    plt.plot(x, dpcmComp)
    plt.subplot(1, 3, 3)
    plt.title("Dekompresja DPCM")
    plt.plot(x, dpcmDecomp)
    plt.show()


# plotAlaw()
# plotDPCM()
#
# singL, fsSingL = sf.read("sounds/sing_low1.wav", dtype=np.float32)
#
# aLawCompL = aLawCompression(singL)
# dpcmCompL = DPCMcompression(singL, 8)
#
# print("sing_low1.wav - oryginal")
# sd.play(singL, fsSingL)
# sd.wait()
# print("sing_low1.wav - kompresja A-law")
# sd.play(aLawCompL, fsSingL)
# sd.wait()
# print("sing_low1.wav - kompresja DPCM")
# sd.play(dpcmCompL, fsSingL)
# sd.wait()
#
# dpcm8bit = DPCMdecompression(DPCMcompression(singL, 8))
# dpcm6bit = DPCMdecompression(DPCMcompression(singL, 6))
# dpcm4bit = DPCMdecompression(DPCMcompression(singL, 4))
# dpcm2bit = DPCMdecompression(DPCMcompression(singL, 2))
# print("DPCM - kwantyzacja 8 bitow")
# sd.play(dpcm8bit, fsSingL)
# sd.wait()
# print("DPCM - kwantyzacja 6 bitow")
# sd.play(dpcm6bit, fsSingL)
# sd.wait()
# print("DPCM - kwantyzacja 4 bitow")
# sd.play(dpcm4bit, fsSingL)
# sd.wait()
# print("DPCM - kwantyzacja 2 bitow")
# sd.play(dpcm2bit, fsSingL)
# sd.wait()
#
# aLawComp = aLawCompression(singL)
# quant8 = np.zeros(len(singL))
# quant6 = np.zeros(len(singL))
# quant4 = np.zeros(len(singL))
# quant2 = np.zeros(len(singL))
# for i in range(len(quant8)):
#     quant8[i] = quantization(aLawComp[i], 8)
#     quant6[i] = quantization(aLawComp[i], 6)
#     quant4[i] = quantization(aLawComp[i], 4)
#     quant2[i] = quantization(aLawComp[i], 2)
#
# print("A-law - kwantyzacja 8 bitow")
# aLaw8bit = aLawDecompression(quant8)
# sd.play(aLaw8bit, fsSingL)
# sd.wait()
# print("A-law - kwantyzacja 6 bitow")
# aLaw6bit = aLawDecompression(quant6)
# sd.play(aLaw6bit, fsSingL)
# sd.wait()
# print("A-law - kwantyzacja 4 bitow")
# aLaw4bit = aLawDecompression(quant4)
# sd.play(aLaw4bit, fsSingL)
# sd.wait()
# print("A-law - kwantyzacja 2 bitow")
# aLaw2bit = aLawDecompression(quant2)
# sd.play(aLaw2bit, fsSingL)
# sd.wait()
#
# singM, fsSingM = sf.read("sounds/sing_medium1.wav", dtype=np.float32)
#
# aLawCompM = aLawCompression(singM)
# dpcmCompM = DPCMcompression(singM,8)
#
# print("sing_medium1.wav - oryginal")
# sd.play(singM, fsSingM)
# sd.wait()
# print("sing_medium1.wav - kompresja A-law")
# sd.play(aLawCompM, fsSingM)
# sd.wait()
# print("sing_medium1.wav - kompresja DPCM")
# sd.play(dpcmCompM, fsSingM)
# sd.wait()
#
# aLawComp = aLawCompression(singM)
# quant8 = np.zeros(len(singM))
# quant6 = np.zeros(len(singM))
# quant4 = np.zeros(len(singM))
# quant2 = np.zeros(len(singM))
# for i in range(len(quant8)):
#     quant8[i] = quantization(aLawComp[i], 8)
#     quant6[i] = quantization(aLawComp[i], 6)
#     quant4[i] = quantization(aLawComp[i], 4)
#     quant2[i] = quantization(aLawComp[i], 2)
#
# print("A-law - kwantyzacja 8 bitow")
# aLaw8bit = aLawDecompression(quant8)
# sd.play(aLaw8bit, fsSingM)
# sd.wait()
# print("A-law - kwantyzacja 6 bitow")
# aLaw6bit = aLawDecompression(quant6)
# sd.play(aLaw6bit, fsSingM)
# sd.wait()
# print("A-law - kwantyzacja 4 bitow")
# aLaw4bit = aLawDecompression(quant4)
# sd.play(aLaw4bit, fsSingM)
# sd.wait()
# print("A-law - kwantyzacja 2 bitow")
# aLaw2bit = aLawDecompression(quant2)
# sd.play(aLaw2bit, fsSingM)
# sd.wait()
#
# dpcm8bit = DPCMdecompression(DPCMcompression(singM, 8))
# dpcm6bit = DPCMdecompression(DPCMcompression(singM, 6))
# dpcm4bit = DPCMdecompression(DPCMcompression(singM, 4))
# dpcm2bit = DPCMdecompression(DPCMcompression(singM, 2))
# print("DPCM - kwantyzacja 8 bitow")
# sd.play(dpcm8bit, fsSingM)
# sd.wait()
# print("DPCM - kwantyzacja 6 bitow")
# sd.play(dpcm6bit, fsSingM)
# sd.wait()
# print("DPCM - kwantyzacja 4 bitow")
# sd.play(dpcm4bit, fsSingM)
# sd.wait()
# print("DPCM - kwantyzacja 2 bitow")
# sd.play(dpcm2bit, fsSingM)
# sd.wait()
#
# singH, fsSingH = sf.read("sounds/sing_high2.wav", dtype=np.float32)
#
# aLawCompH = aLawCompression(singH)
# dpcmCompH = aLawCompression(singH)
#
# print("sing_high1.wav - oryginal")
# sd.play(singH, fsSingH)
# sd.wait()
# print("sing_high1.wav - kompresja A-law")
# sd.play(aLawCompH, fsSingH)
# sd.wait()
# print("sing_high1.wav - kompresja DPCM")
# sd.play(dpcmCompH, fsSingH)
# sd.wait()
#
# dpcm8bit = DPCMdecompression(DPCMcompression(singH, 8))
# dpcm6bit = DPCMdecompression(DPCMcompression(singH, 6))
# dpcm4bit = DPCMdecompression(DPCMcompression(singH, 4))
# dpcm2bit = DPCMdecompression(DPCMcompression(singH, 2))
# print("DPCM - kwantyzacja 8 bitow")
# sd.play(dpcm8bit, fsSingH)
# sd.wait()
# print("DPCM - kwantyzacja 6 bitow")
# sd.play(dpcm6bit, fsSingH)
# sd.wait()
# print("DPCM - kwantyzacja 4 bitow")
# sd.play(dpcm4bit, fsSingH)
# sd.wait()
# print("DPCM - kwantyzacja 2 bitow")
# sd.play(dpcm2bit, fsSingH)
# sd.wait()
# aLawComp = aLawCompression(singH)
# quant8 = np.zeros(len(singH))
# quant6 = np.zeros(len(singH))
# quant4 = np.zeros(len(singH))
# quant2 = np.zeros(len(singH))
# for i in range(len(quant8)):
#     quant8[i] = quantization(aLawComp[i], 8)
#     quant6[i] = quantization(aLawComp[i], 6)
#     quant4[i] = quantization(aLawComp[i], 4)
#     quant2[i] = quantization(aLawComp[i], 2)
#
# print("A-law - kwantyzacja 8 bitow")
# aLaw8bit = aLawDecompression(quant8)
# sd.play(aLaw8bit, fsSingH)
# sd.wait()
# print("A-law - kwantyzacja 6 bitow")
# aLaw6bit = aLawDecompression(quant6)
# sd.play(aLaw6bit, fsSingH)
# sd.wait()
# print("A-law - kwantyzacja 4 bitow")
# aLaw4bit = aLawDecompression(quant4)
# sd.play(aLaw4bit, fsSingH)
# sd.wait()
# print("A-law - kwantyzacja 2 bitow")
# aLaw2bit = aLawDecompression(quant2)
# sd.play(aLaw2bit, fsSingH)
# sd.wait()
