from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# zadanie 1
im1 = Image.open('obraz.jpg')
print("tryb", im1.mode)
print("format", im1.format)
print("rozmiar", im1.size)
h, w = im1.size
# im1.show()

#---------------------------
# zadanie 2a
T = np.array(im1)
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r)

t_g = T[:, :, 1]
im_g = Image.fromarray(t_g)

t_b = T[:, :, 2]
im_b = Image.fromarray(t_b)
# zadanie 2b
im2 = Image.merge('RGB', (im_r, im_g, im_b))
diff = ImageChops.difference(im1, im2)
# zadanie 2c
t_im1 = np.asarray(im1)
t_im2 = np.asarray(im2)
porownanie = t_im1 == t_im2
czy_rowne = porownanie.all()
print("porównanie tablic im1 i im2: ",czy_rowne)

#-------------------------------
# zadanie 3
r, g, b = im1.split()
# permutacja dowolna kanałów
im3 = Image.merge('RGB',(g, r, b)) # zamiana r i g
im3.save('im3.jpg')
im3.save('im3.png')
im3j = Image.open('im3.jpg')
im3p = Image.open('im3.png')
# wczytać i porównać obrazy im3j im3p
o1j = Image.open('lab3/obraz1_1.jpg')
on1j = Image.open('lab3/obraz1_1N.jpg')
o1p = Image.open('lab3/obraz1_1.png')
on1p =Image.open('lab3/obraz1_1N.png')
o2j = oImage.open('lab3/obraz1_2.jpg')
on2j = Image.open('lab3/obraz1_2N.jpg')
o2p = Image.open('lab3/obraz1_2.png')
on2p = Image.open('lab3/obraz1_2N.png')

plt.figure(figsize=(32, 16))
plt.subplot(4,2,1)
plt.imshow(o1j)
plt.axis('off')
plt.subplot(4,2,2)
plt.imshow(o1p)
plt.axis('off')

plt.subplot(4,2,3)
plt.imshow(o2j)
plt.axis('off')
plt.subplot(4,2,4)
plt.imshow(o2p)
plt.axis('off')

plt.subplot(4,2,5)
plt.imshow(on1j)
plt.axis('off')
plt.subplot(4,2,6)
plt.imshow(on1p)
plt.axis('off')

plt.subplot(4,2,7)
plt.imshow(on2j)
plt.axis('off')
plt.subplot(4,2,8)
plt.imshow(on2p)
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig1.png')
plt.show()

#-------------------------------------
# zadanie 4
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

tab4 = rysuj_ramke(w, h, 8)
im4 = Image.fromarray(tab4)
# zadanie 4a
# dowolne 3 podmianki kanałów
r4, g4, b4 = im4.split()
t_r4 = np.asarray(r4)
t_g4 = np.asarray(g4)
t_b4 = np.asarray(b4)
# Zero = np.zeros(t_r4, dtype=np.uint8) typ match rgb
im4_1 = Image.merge('RGB',(Zero,g4,b4)) # usunięty r
im4_2 = Image.merge('RGB',(g4, r4, b4)) # zamienione r i g
im4_3 = Image.merge('RGB',(b4,g4,r4)) # zamienione r i b
# zadanie 4b
plt.figure(figsize=(32, 16))
plt.subplot(1,3,1)
plt.imshow(im4_1)
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(im4_2)
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(im4_3)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig2.png')
plt.show()
#----------------------------------------
# zadanie 5
# trzy obraz (białe kwadraty na czarnym tle?) tak żeby się pokrywały częściowo
# zadanie 5a
# każdy na inny kanał rgb
# zadanie 5b
# różne permutacje kanałów i zapisać w jednej fig3









