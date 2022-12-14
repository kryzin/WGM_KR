from PIL import Image
import numpy as np

def rysuj_ramke_kolor(w, h, dzielnik, kolor):
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = [255, 0, 0]
    grub = int(min(w, h) / dzielnik)
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = kolor
    return tab

kolor = 100, 200, 300
Image.fromarray(rysuj_ramke_kolor(100, 60, 3, kolor)).show()

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