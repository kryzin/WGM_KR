from PIL import Image
import numpy as np

def rysuj_ramke(w, h, dzielnik):# ramki w coraz jaśniejszym odcieniu szarości
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    ile = int((h/grub)/2)
    for k in range(1,ile):
        z1 = h - grub*k
        z2 = w - grub*k
        tab[grub*k:z1, grub*k:z2] = (k * grub) % 256
    return tab

obraz1_1 = Image.fromarray(rysuj_ramke(480, 320, 8))
obraz1_1.save("obraz1_1.jpg")
obraz1_1.save("obraz1_1.png")
#******************************************************************
def rysuj_proste_ramki(w, h, m, n, dzielnik):# obraz4 dowolny
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = 125 # szary dla lepszej widoczności
    # tab[0:n, 0:m]
    grub = int(2 * (min(n,m)/dzielnik))
    ile = int((n / grub))  # ilość wszystkich ramek
    for k in range(ile):
        z1 = n - grub * k
        z2 = m - grub * k
        tab[grub * k:z1, grub * k:z2] = (k * grub) % 256
    # tab[n:h, m:w]
    ile = int((h-n/grub)/2)
    for k in range(ile):
        z1 = n + grub * k
        z2 = m + grub * k
        tab[z1:h-grub*k, z2:w-grub*k] = 255 - ((k * grub) % 256)
    return tab

obraz1_2 = Image.fromarray(rysuj_proste_ramki(480, 320, 150, 150, 20))
obraz1_2.save("obraz1_2.jpg")
obraz1_2.save("obraz1_2.png")
#******************************************************************
def negatyw(tab): # negatyw kolorowy/odcienie szarości
    neg = 255 - tab
    return neg

obraz1_1N = Image.fromarray(negatyw(rysuj_ramke(480, 320, 8)))
obraz1_1N.save("obraz1_1N.jpg")
obraz1_1N.save("obraz1_1N.png")

obraz1_2N = Image.fromarray(negatyw(rysuj_proste_ramki(480, 320, 150, 150, 20)))
obraz1_2N.save("obraz1_2N.jpg")
obraz1_2N.save("obraz1_2N.png")
#******************************************************************
def rysuj_pasy_pionowe(w, h, dzielnik):# obraz2 pionowe pasy kolorowe
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = [k * grub, 0, 255 - (k * grub)]
    return tab

obraz2 = Image.fromarray(rysuj_pasy_pionowe(480,320,8))
obraz2.save("obraz2.jpg")
obraz2.save("obraz2.png")
obraz2N = Image.fromarray(negatyw(rysuj_pasy_pionowe(480, 320, 8)))
obraz2N.save("obraz2N.jpg")
obraz2N.save("obraz2N.png")
# #******************************************************************
inicjaly = Image.open("inicjaly.bmp")
t_inicjaly = np.asarray(inicjaly)
t_inicjaly = t_inicjaly * 255
h, w = t_inicjaly.shape

def inicjaly_kolor(tab, w, h, dzielnik):
    t = (h, w, 3)
    tab_t = np.zeros(t, dtype=np.uint8)
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if tab[i, j] == 255:
                    tab_t[i, j] = tab[i, j]
                else:
                    if k % 3 == 0:
                        tab_t[i, j] = [200, 0, 100]
                    elif k % 3 == 1:
                        tab_t[i, j] = [100, 200, 0]
                    else:
                        tab_t[i, j] = [0, 100, 200]
    return tab_t

obraz3 = Image.fromarray(inicjaly_kolor(t_inicjaly, w, h, 5))
obraz3.save("obraz3.jpg")
obraz3.save("obraz3.png")
