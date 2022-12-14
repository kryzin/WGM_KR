from PIL import Image
import numpy as np

print("*** zadanie 2 ***")
inicjaly = Image.open("inicjaly.bmp")
# inicjaly.show()
print("tryb:", inicjaly.mode)
print("format:", inicjaly.format)
print("rozmiar:", inicjaly.size)

#3
dane_obrazu = np.asarray(inicjaly)
# print(dane_obrazu)
dane_int = dane_obrazu * 1
# print(dane_int)
# obraz_dane = Image.fromarray(dane_obrazu)
# obraz_dane.show()
# zapis = open("inicjaly.txt","w")
# print(dane_int, file=zapis)

print()
print("*** zadanie 4 ***")
print("typ danych tablicy:", dane_obrazu.dtype)
print("rozmiar tablicy:", dane_obrazu.shape)
print("liczba elementow:", dane_obrazu.size)
print("wymiar tablicy:", dane_obrazu.ndim)
print("rozmiar wyrazu tablicy:", dane_obrazu.itemsize)

# SPRAWDŹ WARTOŚĆ PIKSELA PO ADRESIE
# print("podaj adres piksela (a,b)")
# print(" a :")
# a = input()
# a = int(a)
# print(" b :")
# b = input()
# b = int(b)
# print(dane_obrazu[(b,a)])

# print()
# print("*** zadanie 5 ***")
# tablica = np.loadtxt("inicjaly.txt", dtype=np.bool_)
# print("typ danych tablicy :", tablica.dtype)
# print("rozmiar tablicy :", tablica.shape)
# print("wymiar tablicy :", tablica.ndim)
# porownanie = tablica == dane_obrazu
# print("czy są równe:",porownanie.all())

print()
print("*** zadanie 6 ***")
tablica2 = np.loadtxt("inicjaly.txt", dtype=np.int_)
print("typ danych tablicy 2 :", tablica2.dtype)
print("rozmiar tablicy 2 :", tablica2.shape)
print("wymiar tablicy 2 :", tablica2.ndim)
porownanie = tablica2 == dane_obrazu
print("czy są równe:")
print(porownanie.all())
obraz_int = Image.fromarray(tablica2)
print("tryb:", obraz_int.mode)
print("format:", obraz_int.format)
print("rozmiar:", obraz_int.size)
obraz_int.show()

