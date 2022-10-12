from PIL import Image
import numpy as np

# zadanie 1
obraz_wstawiany = Image.open("kr.bmp")
t_obrazu = np.asarray(obraz_wstawiany)
h_m, w_m = t_obrazu.shape

def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    t = (wsp * h_m, wsp * w_m)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(25, 25+h_m-1):
        for j in range(50, 50+w_m-1):
            tab[i][j]=t_obrazu[i-25][j-50]
    tab = tab.astype(bool)
    po_wstawieniu = Image.fromarray(tab)
    po_wstawieniu.save("po_wstawieniu.bmp")
    return po_wstawieniu

# po_wstawieniu = wstaw_obraz(obraz_wstawiany, w_m, h_m, 5)
# po_wstawieniu.show()


# zadanie 3
#***********************************************************************************************
def rysuj_ramke(w, h, dzielnik):# obraz1 ramka na przemian grubosc (min(w,h)/dzielnik)
    t = (h, w)
    tab = np.zeros(t, dtype=np.uint8)
    grub = int(min(w, h) / dzielnik)
    ile = int((h/grub)/2) # ilość wszystkich ramek
    for k in range(1,ile):
        z1 = h - grub*k
        z2 = w - grub*k
        tab[grub*k:z1, grub*k:z2] = k%2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    # im_ramka.show()
    return obraz

# obraz1 = rysuj_ramke(480, 320, 8)
# obraz1.save("obraz1.bmp")

#**********************************************************
def rysuj_pasy_pionowe(w, h, dzielnik):# obraz2 pionowe pasy grubosc (w/dzielnik)- od lewej czarny
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w / dzielnik)
    # print(grub)
    for k in range(dzielnik): # k={0,...,7}
        for g in range(grub): # g={0,...,60}
            i = k * grub + g
            for j in range(h):
                tab[j, i] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    # obraz.show()
    return obraz

# obraz2 = rysuj_pasy_pionowe(480,320,8)
# obraz2.save("obraz2.bmp")

#**********************************************************
def rysuj_prostokaty(w, h, m, n):# obraz3 w wybranym punkcie stykaja sie prostokaty czarny gora po lewo dol po prawo
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[n:h, m:w] = 0
    tab[0:n, 0:m] = 0
    tab = tab * 255
    obraz = Image.fromarray(tab)
    # obraz.show()
    return obraz

# obraz3 = rysuj_prostokaty(480, 320, 100, 50)
# obraz3.save("obraz3.bmp")

#**********************************************************
def rysuj_proste_ramki(w, h, m, n, dzielnik):# obraz4 dowolny
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    # tab[0:n, 0:m]
    grub = int(min(n,m)/dzielnik)
    ile = int((n / grub) / 2)  # ilość wszystkich ramek
    for k in range(ile):
        z1 = n - grub * k
        z2 = m - grub * k
        tab[grub * k:z1, grub * k:z2] = k % 2
    # tab[n:h, m:w]
    ile = int((h-n/grub)/2)
    for k in range(ile):
        z1 = n + grub * k
        z2 = m + grub * k
        tab[z1:h-grub*k, z2:w-grub*k] = k % 2
    tab = tab * 255
    obraz = Image.fromarray(tab)
    # obraz.show()
    return obraz

obraz4 = rysuj_proste_ramki(480,320,100,50,8)
obraz4.save("obraz4.bmp")

