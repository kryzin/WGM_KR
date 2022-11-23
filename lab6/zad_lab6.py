from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

obraz = Image.open('D:/WGM_KR/lab4/obraz.jpg')
print("rozmiar", obraz.size)
#obraz.show()

# zadanie 1.1
def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

def rysuj_prostokat(obraz, m, n, a, b, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i == m)|(i == m+a): # lewy i prawy bok
            if (j > n)&(n+b > j):
                obraz1.putpixel((i,j), kolor)
        if (j == n)|(j == n+b): # górny i dolny bok
            if (i > m)&(m+a > i):
                obraz1.putpixel((i,j), kolor)
    return obraz1

# obraz1 = rysuj_prostokat(obraz,50,50,50,100,(100,0,255))
# obraz1.show()

# zadanie 1.2
def rysuj_kwadrat(obraz, m, n, a, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    if a%2 == 0: dziel = 0
    else: dziel = 1
    a = a - dziel
    for i, j in zakres(w, h):
        if (i == m + a/2)|(i == m - a/2): # prawy lewy
            if (j > n - a/2)&(n + a/2 > j):
                obraz1.putpixel((i,j), kolor)
        if (j == n + a/2)|(j == n - a/2): # góra dół
            if (i > m - a/2)&(m + a/2 > i):
                obraz1.putpixel((i,j), kolor)
    return obraz1

# obraz2 = rysuj_kwadrat(obraz, 320,200,100,(0,255,0))
# obraz2.show()

# zadanie 1.3
def rysuj_kwadrat_grub(obraz, m, n, a, kolor, grubosc):
    obraz1 = obraz.copy()
    w, h = obraz.size
    if a%2 == 0: dziel = 0
    else: dziel = 1
    a = a - dziel
    for i, j in zakres(w, h):
        if ((i <= m + a/2) & (i >= m + a/2 - grubosc))|((i >= m - a/2) & (i <= m - a/2 + grubosc)): # prawy lewy
            if (j > n - a/2)&(n + a/2 > j):
                obraz1.putpixel((i,j), kolor)
        if ((j <= n + a/2) & (j >= n + a/2 - grubosc))|((j >= n - a/2) & (j <= n - a/2 + grubosc)): # góra dół
            if (i > m - a/2)&(m + a/2 > i):
                obraz1.putpixel((i,j), kolor)
    return obraz1

# obraz3 = rysuj_kwadrat_grub(obraz, 320,200,100,(0,255,0),20)
# obraz3.show()

#---------------------------------------------------
# zadanie 2.1
def odbij_gora_dol(obraz):
    tab = obraz.load()
    obraz1 = obraz.copy()
    w, h = obraz.size
    tab1 = obraz1.load()
    for i in range(w):
        for j in range(h):
            tab1[i, j] = tab[i, h - 1 - j]
    return obraz1

# odbij_gora_dol(obraz).show()

# zadanie 2.2
def odbij_dol_na_gore(obraz):
    obraz1 = obraz.copy()
    w, h = obraz.size
    h1 = int(h / 2)
    tab = obraz1.load()
    for j in range(h1, h):
        for i in range(w):
            tab[i, h - j] = tab[i, j]
    return obraz1

# odbij_dol_na_gore(obraz).show()

# zadanie 2.3
def odbij_gore_na_dol(obraz):
    obraz1 = obraz.copy()
    w, h = obraz.size
    h1 = int(h / 2)
    tab = obraz1.load()
    for j in range(h1, h):
        for i in range(w):
            tab[i, j] = tab[i, h - j]
    return obraz1

# odbij_gore_na_dol(obraz).show()

# zadanie 2.4
def odbij_w_pionie(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1 - i, j]
    return img
# odbij_w_pionie(obraz).show()

def odbij_w_pionie1(im):
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px[w - 1 - i, j]
    return img
# odbij_w_pionie1(obraz).show()
# po zmianie dostajemy lustrzane odbicie, dzieje się tak bo odwracając chcemy pobierać piksele
# z już zmienionej połowy tablicy, więc robimy kopię
#------------------------------------------------------
# zadanie 3
def rysuj_kolo(obraz,m_s,n_s,r):
    obraz1 = obraz.copy()
    tab = obraz.load()
    tab1 = obraz1.load()
    w, h = obraz.size
    for i, j in zakres(w, h):# zostaje ucinany obraz
        if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:
            tab1[i,j] = tab[i + 200, j + 100]
    return obraz1
rysuj_kolo(obraz, 200,200,100).show()
