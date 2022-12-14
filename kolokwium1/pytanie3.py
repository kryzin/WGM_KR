import numpy as np

def rysuj_pasy_pionowe(w, h, g):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    for j in range(h): # kolumny
        for i in range(w): # wiersze
            if i > (i - g):
                tab[j,i] = 0
            if i < g:
                tab[j,i] = 0
            else: tab[j,i] = 1
    tab = tab * 255
    obraz = Image.fromarray(tab)  # tworzy obraz
    obraz.show()

rysuj_pasy_pionowe(400,200,20)