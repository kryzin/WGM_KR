from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# zadanie 1
# zmieniłam rozmiar obrazu na mniejszy, żeby lepiej było widać zadanie 2
obraz = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab4/obraz.jpg')
inicjaly = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/inicjaly.jpg')

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

# zadanie 2.1
def wstaw_inicjaly(obraz,inicjaly,m,n, kolor):
    inicjaly = inicjaly.convert(mode="RGB")
    w, h = inicjaly.size
    inicjaly1 = inicjaly.copy()
    for i,j in zakres(w, h):
        p = inicjaly.getpixel((i, j))
        if p[0]==0:
            inicjaly1.putpixel((i, j), kolor)
        else:
            inicjaly1.putpixel((i, j), (255,255,255))
    w1, h1 = obraz.size
    obraz1 = obraz.copy()
    for i, j in zakres(w, h):
        if i + m < w1 and j + n < h1:
            p = inicjaly1.getpixel((i, j))
            obraz1.putpixel((i + m, j + n), p)
    obraz1.save("obraz1.jpg")
    return obraz1

# plt.imshow(wstaw_inicjaly(obraz, inicjaly,540,350, (255,0,0)))
# plt.show()

# zadanie 2.2
def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    obraz2 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz2.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    obraz2.save("obraz2.jpg")
    return obraz2

# plt.imshow(wstaw_inicjaly_maska(obraz,inicjaly,250,180, 100,100,100))
# plt.show()

# zadanie 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    w, h = inicjaly.size
    pixele = inicjaly.load()
    for i, j in zakres(w, h):
        pixele[i, j] = func(pixele[i, j])
