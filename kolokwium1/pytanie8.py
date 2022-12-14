from PIL import Image, ImageFilter
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

maska1 = Image.open('maska1.jpg')
obraz5 = Image.open('obraz5.jpg')

def jeden(obraz5, maska1):
    maska = np.asarray(maska1)
    obraz = np.asarray(obraz5)
    h,w = obraz.shape
    h1,w1 = maska.shape
    t = (h, w, 3)
    tab_t = np.zeros(t, dtype=np.uint8)
    for j in range(w):
        for i in range(h):
            if j > w - w1:
                if i < h1:
                    tab_t[i,j] = tab[i,j]
    return tab_t

obraz3 = Image.fromarray(jeden(obraz5,maska1))
obraz3.show()


