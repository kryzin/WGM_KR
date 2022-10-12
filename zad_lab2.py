from PIL import Image
import numpy as np

# zadanie 1
# obraz_wstawiany = Image.open("kr.bmp")
# t_obrazu = np.asarray(obraz_wstawiany)
# h_m, w_m = t_obrazu.shape

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

# zadanie 2
# wstaw1 = wstaw_obraz(obraz_wstawiany, w_m, h_m, 3)

# zadanie 3
# obraz1 ramka na przemian grubosc min(w,h)/dzielnik

# obraz2 pionowe pasy grubosc w/dzielnik- od lewej czarny
def rysuj_pasy_poziome(w, h, dzielnik):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(w/dzielnik)
    print(grub)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g 
            for j in range(w):
                tab[i, j] = k % 2  # reszta z dzielenia przez dwa
    obraz = Image.fromarray(tab)  # tworzy obraz
    obraz.show()

rysuj_pasy_poziome(480, 320, 8)
# obraz3 w wybranym punkcie stykaja sie prostokaty czarny gora po lewo dol po prawo

# obraz4 dowolny, cos ciekawego (pionowy i coraz ciensze?)

