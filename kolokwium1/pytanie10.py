from PIL import Image, ImageFilter
import numpy as np

im = Image.open('obraz2.jpg')
print(im.size)
r, g, b = im.split()

#szary1
def szary1(w, h):
    t = (w, h)
    tab = np.zeros(t, dtype=np.uint8)
    kolor = 255 - int(w / 2) + 1
    for k in range(int(w / 2)):
        for i in range(k, w - k):
            for j in range(k, h - k):
                tab[i, j] = kolor
        kolor = kolor + 30
    return tab

tab = szary1(338,486)
b = Image.fromarray(tab).convert('L')

mix_sz = Image.merge('RGB', (r, g, b))

