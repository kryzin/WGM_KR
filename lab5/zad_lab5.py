from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# zadanie 1
# zmieniłam rozmiar obrazu na mniejszy, żeby lepiej było widać zadanie 2
obraz = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab4/obraz.jpg')
inicjaly = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/inicjaly.jpg')

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

#-----------------------------------------------------------------
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

#--------------------------------------------------------------
# zadanie 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    inicjaly3 = inicjaly.copy()
    inicjaly3 = inicjaly3.convert(mode="RGB")
    obraz3 = obraz.copy()
    w, h = inicjaly3.size
    ini_t = inicjaly3.load()
    obr_t = obraz3.load()
    for i, j in zakres(w, h):
        p = ini_t[i,j]
        if p[0] == 0:
            ini_t[i,j] = kolor
    w1, h1 = obraz3.size
    for i, j in zakres(w, h):
        if i + m < w1 and j + n < h1:
            p = ini_t[i,j]
            obr_t[i+m,j+n] = p
    return obraz3

# plt.imshow(wstaw_inicjaly_load(obraz, inicjaly,540,350, (255,0,0)))
# plt.show()

def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    obraz3 = obraz.copy()
    w, h = obraz.size
    w0, h0 = inicjaly.size
    ob3 = obraz3.load()
    ini = inicjaly.load()
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if ini[i,j] == 0:
                ob3[i+m,j+n] = (ob3[i+m,j+n][0] + x, ob3[i+m,j+n][1] + y, ob3[i+m,j+n][2] + z)
    return obraz3

# plt.imshow(wstaw_inicjaly_maska_load(obraz,inicjaly,250,180, 100,100,100))
# plt.show()

#--------------------------------------------------------------
# zadanie 4.1
def kontrast(obraz, wsp_kontrastu): # wsp 0-100
    obraz4 = obraz.copy()
    mn = ((255 + wsp_kontrastu) / 255)**2
    obraz4 = obraz4.point(lambda i: 128 + (i - 128)*mn )
    return obraz4

# im1 = kontrast(obraz,0)
# im2 = kontrast(obraz,50)
# im3 = kontrast(obraz,100)
#
# plt.figure(figsize=(100, 100))
# plt.subplot(1,3,1)
# plt.imshow(im1)
# plt.axis('off')
# plt.subplot(1,3,2)
# plt.imshow(im2)
# plt.axis('off')
# plt.subplot(1,3,3)
# plt.imshow(im3)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig4_1.png')
# plt.show()

# zadanie 4.3 (nie ma 4.2)

def transformacja_logarytmiczna(obraz):
    obraz5 = obraz.copy()
    obraz5 = obraz5.point(lambda i: 255 * np.log(1 + i/255))
    obraz5.save('obraz4_3.png')
    return obraz5

# plt.imshow(transformacja_logarytmiczna(obraz))
# plt.show()

# zadanie 4.4

def transformacja_gamma(obraz, gamma): # gamma > 0
    obraz6 = obraz.copy()
    obraz6 = obraz6.point(lambda i: (i/255)**(1/gamma)*255)
    obraz6.save('obraz4_4.png')
    return obraz6

# im1 = transformacja_gamma(obraz,0.4)
# im2 = transformacja_gamma(obraz,16)
# im3 = transformacja_gamma(obraz,1000)
#
# plt.figure(figsize=(100, 100))
# plt.subplot(1,3,1)
# plt.imshow(im1)
# plt.axis('off')
# plt.subplot(1,3,2)
# plt.imshow(im2)
# plt.axis('off')
# plt.subplot(1,3,3)
# plt.imshow(im3)
# plt.axis('off')
# plt.subplots_adjust(wspace=0.05, hspace=0.05)
# plt.savefig('fig4_4.png')
# plt.show()

#-------------------------------------------------
# zadanie 5

def pixel_100(obraz):
    obraz7 = obraz.copy()
    w, h = obraz7.size
    tab = obraz7.load()
    for i,j in zakres(w, h):
        tab[i,j] = (tab[i,j][0] + 100, tab[i,j][1] + 100, tab[i,j][2] + 100)
    return obraz7

# plt.imshow(pixel_100(obraz))
# plt.show()



# T = np.array(obraz, dtype='uint8')
# T += 100
# obraz_wynik = Image.fromarray(T, "RGB")
# obraz_wynik.show()

