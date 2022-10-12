from PIL import Image   # Python Imaging Library
import numpy as np

#
# inicjaly = Image.open("lab2/bs.bmp") # wczytywanie obrazu
# # obrazek.show()
# print("tryb", inicjaly.mode)
# print("format", inicjaly.format)
# print("rozmiar", inicjaly.size)
#
#
# t_inicjaly = np.asarray(inicjaly)
# print("typ danych tablicy", t_inicjaly.dtype)  # typ danych przechowywanych w tablicy
# print("rozmiar tablicy", t_inicjaly.shape)  # rozmiar tablicy - warto porównac z wymiarami obrazka
# print("***************************************")
#
# def wstaw_inicjaly(t_inicjaly):
#     h0, w0 = t_inicjaly.shape
#     print(h0,w0)
#     t = (2*h0, 2*w0) # rozmiar tablicy
#     tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
#     for i in range(25, 25+h0-1):
#         for j in range(50, 50+w0-1):
#             tab[i][j]=t_inicjaly[i-25][j-50]
#     tab = tab.astype(bool)
#     po_wstawieniu = Image.fromarray(tab)
#     return po_wstawieniu
# po_wstawieniu = wstaw_inicjaly(t_inicjaly)
# po_wstawieniu.show()
#
def rysuj_ramke(w, h, dzielnik):
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    ile = int((h/grub)/2)
    for k in range(1,ile+1):
        z1 = h - grub*k
        z2 = w - grub*k
        tab[grub*k:z1, grub*k:z2] = k%2
    return tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości


tab = rysuj_ramke(500, 350, 8)
im_ramka = Image.fromarray(tab)
im_ramka.show()

# def rysuj_pasy_pionowe(w, h, dzielnik): # w, h   -  rozmiar obrazu
#     t = (h, w)  # rozmiar tablicy
#     tab = np.ones(t, dtype=np.uint8)
#     # jaki bedzie efekt, gdy np.ones zamienimy na np.zeros?
#     grub = int(w / dzielnik)  # liczba pasów = 9 o grubości 10
#     print(grub)
#     for k in range(dzielnik):  # uwaga k = 0,1,2,3,4,5,8   bez dziewiatki
#         for g in range(grub):
#             i = k * grub + g  # i - indeks wiersza, j - indeks kolumny
#             for j in range(h):
#                 tab[j, i] = k % 2  # reszta z dzielenia przez dwa
#     tab = tab * 255  # alternatywny sposób uzyskania tablicy obrazu czarnobiałego ale w trybie odcieni szarości
#     obraz = Image.fromarray(tab)  # tworzy obraz
#     obraz.show()
#
# rysuj_pasy_pionowe(480, 320, 8)








