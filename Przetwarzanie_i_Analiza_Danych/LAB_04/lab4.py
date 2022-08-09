import numpy as np
import matplotlib.pyplot as plt


# dysketyzacja
# 1
def sygnal(f, Fs):
    dt = 1 / Fs
    t = np.arange(0, 1, dt)  # czas
    st = np.sin(2 * np.pi * f * t)
    return t, st


def wykres(f, Fs):
    t, st = sygnal(f, Fs)
    plt.plot(t, st)
    plt.show()


wykres(10, 20)
wykres(10, 21)
wykres(10, 30)
wykres(10, 45)
wykres(10, 50)
wykres(10, 100)
wykres(10, 150)
wykres(10, 200)
wykres(10, 250)
wykres(10, 1000)

# 4 Twierdzenie Nyquista
# 5 Aliasing


# kwantyzacja
# 1
#wczytanie obrazka
image = plt.imread('game.png')
plt.imshow(image)
plt.show()
# 2
#zwraca iosc wymiarow
print("{}".format(image.ndim))
# 3
#najglębszy wymiar oraz jego wartosc
print("{}".format(image.shape))
# 4
#przekształcanie do skali szarości
R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]
image1 = (np.maximum(R, G, B) + np.minimum(R, G, B)) / 2
image2 = (R + G + B) / 3
image3 = 0.21 * R + 0.72 * G + 0.07 * B

#wyswietlenie skali szarosci
plt.imshow(image1, cmap='gray')
plt.title("Wyznaczona jakosnosc piksela")
plt.show()
plt.imshow(image2, cmap='gray')
plt.title("Usredniona jasnosc piksela")
plt.show()
plt.imshow(image3, cmap='gray')
plt.title("Wyznaczona iluminacja piksela")
plt.show()
# 5
#histogramy
plt.hist(image1.ravel(), bins=256, range=(0.0, 1.0))
plt.title("Wyznaczona jakosnosc piksela")
plt.show()
plt.hist(image2.ravel(), bins=256, range=(0.0, 1.0))
plt.title("Usredniona jasnosc piksela")
plt.show()
plt.hist(image3.ravel(), bins=256, range=(0.0, 1.0))
plt.title("Wyznaczona iluminacja piksela")
plt.show()
# 6
plt.hist(image1.ravel(), bins=16, range=(0.0, 1.0))
plt.title("Zredukowana liczba kolorow do 16")
plt.show()
# 7
#redukcja do 16 kolorow oraz histogram
_, bins = np.histogram(image, 16)
newimag = bins[np.digitize(image, bins) - 1]
plt.imshow(newimag)
plt.show()









# binaryzacja
image = plt.imread('gradient.png')
R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]

image = (np.maximum(R, G, B) + np.minimum(R, G, B)) / 2
plt.imshow(image, cmap='gray')
plt.show()
plt.hist(image.ravel(), bins=256)
plt.show()
