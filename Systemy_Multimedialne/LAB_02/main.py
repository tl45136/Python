import matplotlib.pyplot as plt
import numpy as np


def colorFit(color, n):
    fit = np.linalg.norm(n - color, axis=1)
    return n[np.argmin(fit)]


def quantization(image, palette):
    imgcopy = image.copy()

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            imgcopy[x, y] = colorFit(image[x, y], palette)

    return imgcopy




def randomDithering(image):
    imgcopy = image.copy()
    randomValue = np.random.rand(image.shape[0], image.shape[1])

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            imgcopy[x, y] = image[x, y] > randomValue[x, y]

    return imgcopy


def organizedDithering(image, palette):
    imgcopy = image.copy()
    m2tresholdMap = np.array([[0, 8, 2, 10],
                              [12, 4, 14, 6],
                              [3, 11, 1, 9],
                              [15, 7, 13, 5]])
    mpre = 1 / 16 * (m2tresholdMap + 1) - 0.5

    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            imgcopy[x, y] = colorFit(imgcopy[x, y] + mpre[x % 4, y % 4], palette)

    return imgcopy


def max_value(arr):
    final = np.zeros(len(arr))

    for i in range(len(arr)):
        if arr[i] > 1:
            final[i] = 1
        elif arr[i] < 0:
            final[i] = 0
        else:
            final[i] = arr[i]
    return final


def floydSteinbergDithering(image, palette):
    imgcopy = image.copy()

    for x in range(1, image.shape[0] - 1):
        for y in range(1, image.shape[1] - 1):
            oldPixel = imgcopy[x, y].copy()
            newPixel = colorFit(oldPixel, palette)
            imgcopy[x, y] = newPixel
            quant_error = oldPixel - newPixel

            imgcopy[x + 1, y] = max_value(imgcopy[x + 1, y] + quant_error * 7 / 16)
            imgcopy[x - 1, y + 1] = max_value(imgcopy[x - 1, y + 1] + quant_error * 3 / 16)
            imgcopy[x, y + 1] = max_value(imgcopy[x, y + 1] + quant_error * 5 / 16)
            imgcopy[x + 1, y + 1] = max_value(imgcopy[x + 1, y + 1] + quant_error * 1 / 16)

    return imgcopy


def plotting(image, palette, title):
    randdit = 4
    colormap = None

    if len(image.shape) < 3:
        colormap = plt.cm.gray
    
    
    if len(palette) == 2:
        randdit = 5
        position = [1, 2, 3, 4, 5]
    else:
        position = [1, 2, 0, 3, 4]

    plt.subplot(1, randdit, position[0])
    plt.suptitle(title)
    plt.axis('off')
    plt.imshow(image, cmap=colormap)
    plt.title("Oryginał")

    plt.subplot(1, randdit, position[1])
    plt.axis('off')
    plt.imshow(quantization(image, palette), cmap=colormap)
    plt.title("Kwantyzacja")

    if randdit == 5:
        plt.subplot(1, randdit, position[2])
        plt.axis('off')
        plt.imshow(randomDithering(image), cmap=colormap)
        plt.title("1 bit metoda losowa")

    plt.subplot(1, randdit, position[3])
    plt.axis('off')
    plt.imshow(organizedDithering(image, palette), cmap=colormap)
    plt.title("Dithering zorganizowany")

    plt.subplot(1, randdit, position[4])
    plt.axis('off')
    plt.imshow(floydSteinbergDithering(image, palette), cmap=colormap)
    plt.title("Dithering Floyd-Steinberga")



    plt.show()


palette8bit = np.array([[0., 0., 0.],
                        [0., 0., 1.],
                        [0., 1., 0.],
                        [0., 1., 1.],
                        [1., 0., 0.],
                        [1., 0., 1.],
                        [1., 1., 0.],
                        [1., 1., 1.]])

palette16bit = np.array([[0, 0, 0],  # black
                         [0, 1, 1],  # aqua
                         [0, 0, 1],  # blue
                         [1, 0, 1],  # fuchsia
                         [0, 0.5, 0],  # green
                         [0.5, 0.5, 0.5],  # grey
                         [0, 1, 0],  # lime
                         [0.5, 0, 0],  # maroon
                         [0, 0, 0.5],  # navy
                         [0.5, 0.5, 0],  # olive
                         [0.5, 0, 0.5],  # purple
                         [1, 0, 0],  # red
                         [0.75, 0.75, 0.75],  # silver
                         [0, 0.5, 0.5],  # teal
                         [1, 1, 1],  # white
                         [1, 1, 0]])  # yellow




custom_palette = np.array([[0.6627451,  0.57647059, 0.15686275],
                                [0.57647059, 0.27058824, 0.08627451],
                                [0.1254902,  0.07843137, 0.05490196],
                                [0.81960784, 0.62352941, 0.37254902],
                                [0.43529412, 0.38823529, 0.14117647],
                                [0.41960784, 0.07843137, 0.05882353],
                                [0.6745098,  0.63921569, 0.56862745],
                                [0.2627451,  0.10980392, 0.0745098],
                                [0.50980392, 0.50980392, 0.49411765],
                                [0.2 ,       0.07058824, 0.0627451 ],
                                [0.83137255, 0.20784314, 0.14509804],
                                [0.63921569, 0.55294118, 0.10980392],
                                [0.6     ,   0.,         0.01960784],
                                [0.03137255, 0.02745098, 0.01176471],
                                [0.75294118, 0.63921569, 0.27058824],
                                [0.29803922, 0.29803922, 0.2745098]])



grayscale1bit = np.linspace(0, 1, 2).reshape((2, 1)).astype(float)
grayscale2bit = np.linspace(0, 1, 4).reshape((4, 1)).astype(float)
grayscale4bit = np.linspace(0, 1, 16).reshape((16, 1)).astype(float)


images = [plt.imread("0008.png"), plt.imread("0007.tif"),  
            plt.imread("0011.jpg"), plt.imread("0014.jpg"), plt.imread("0016.jpg")]  

for i in range(len(images)):
    if images[i].dtype != 'float32':
        images[i] = images[i].astype(float) / 255

# for i in range(0, 2):
#     plotting(images[i], grayscale1bit, "Dithering dla 1 bitu koloru")

# for i in range(0, 2):
#     plotting(images[i], grayscale2bit, "Dithering dla 2 bitu koloru")

# for i in range(0, 2):
#     plotting(images[i], grayscale4bit, "Dithering dla 4 bitu koloru")

# for i in range(2, 5):
#     plotting(images[i], palette8bit, "Dithering obrazów kolorowych dla palety 8 kolorów")

# for i in range(2, 5):
#     plotting(images[i], palette16bit, "Dithering obrazów kolorowych dla palety 16 kolorów")

plt.subplot(1, 3, 1)
plt.axis('off')
plt.imshow(quantization(images[3], palette16bit))
plt.title("Kwantyzacja")

plt.subplot(1, 3, 2)
plt.axis('off')
plt.suptitle("Kwantyzacja oparta na ręcznej palecie 16 kolorów")
plt.title("Oryginał")
plt.imshow(images[3])

plt.subplot(1, 3, 3)
plt.axis('off')
plt.title("Paleta dobrana ręcznie")
plt.imshow(quantization(images[3], custom_palette))
plt.show()

