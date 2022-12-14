from PIL import Image, ImageFilter
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# obraz = Image.open("obraz2.jpg")
# print("ropz obrazu",obraz.size)
# dane_obrazu = np.asarray(obraz)
# print("typ danych tablicy:", dane_obrazu.dtype)
# print("rozmiar tablicy:", dane_obrazu.shape)
# print("liczba elementow:", dane_obrazu.size)
# print("wymiar tablicy:", dane_obrazu.ndim)
# print("rozmiar wyrazu tablicy:", dane_obrazu.itemsize)
# print(dane_obrazu[205,89])

# SPRAWDŹ WARTOŚĆ PIKSELA PO ADRESIE
# print("podaj adres piksela (a,b)")
# print(" a :")
# a = input()
# a = int(a)
# print(" b :")
# b = input()
# b = int(b)
# print(dane_obrazu[(b,a)])

# im = Image.open('obraz2.jpg')
# imA = im.filter(ImageFilter.DETAIL)
# look = ImageChops.difference(im,imA)
# look.show()
#
# imB = im.filter(ImageFilter.Kernel(size=(3, 3), scale=15, offset=0, kernel=(-2, -2, -2, -2, 32, -2, -2, -2, -2)))
# look = ImageChops.difference(im,imB)
# look.show()
obraz1 = Image.open('obraz1.jpg')
r, g, b = obraz1.split()
image = Image.merge('RGB',(g,r,b))
image.show()
