from PIL import Image, ImageOps
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# zadanie 1
im1 = Image.open('obraz.jpg')
# print("tryb", im1.mode)
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
# im2.show()
# diff.show()

# zadanie 2c
t_im1 = np.asarray(im1)
t_im2 = np.asarray(im2)
porownanie = t_im1 == t_im2
czy_rowne = porownanie.all()
print("porównanie tablic im1 i im2: ",czy_rowne)

#-------------------------------
# zadanie 3a
r, g, b = im1.split()
im3 = Image.merge('RGB',(g, r, b)) # zamiana r i g
im3.save('im3.jpg')
im3.save('im3.png')
# zadanie 3b
im3j = Image.open('im3.jpg')
im3p = Image.open('im3.png')
sprawdzenie = im3j == im3p
print("porównanie obraz 3 format jpg i format png, czy są równe?: ", sprawdzenie)

o1j = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_1.jpg')
o1p = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_1.png')
on1j = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_1N.jpg')
on1p = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_1N.png')
o2j = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_2.jpg')
o2p = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_2.png')
on2j = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_2N.jpg')
on2p = Image.open('c:/Users/Karolina/PycharmProjects/WGM_KR/lab3/obraz1_2N.png')

plt.figure(figsize=(25, 16))
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
def rysuj_ramke(h, w, dzielnik):# ramki w coraz jaśniejszym odcieniu szarości
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
im4.save('im4.jpg')
# im4.show()
# zadanie 4a
im4_1 = Image.merge('RGB',(r, g, im4))
im4_2 = Image.merge('RGB',(r, im4, b))
im4_3 = Image.merge('RGB',(im4, g, b))
# im4_1.show()
# im4_2.show()
# im4_3.show()

# zadanie 4b
plt.figure(figsize=(20, 20))
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
o1 = Image.open('a.bmp')
o2 = Image.open('b.bmp')
o3 = Image.open('c.bmp')

o1 = o1.convert("L")
o2 = o2.convert("L")
o3 = o3.convert("L")

# zadanie 5a
image = Image.merge('RGB', (o1, o2, o3))
image.save('image.jpg')
# image.show()

# zadanie 5b
t = (300,400)
A = np.zeros(t, dtype=np.uint8)
A_im = Image.fromarray(A)
image1 = Image.merge('RGB',(o2, o3, o1)) # zamiana wszystkie
image2 = Image.merge('RGB',(A_im, o2, o3)) # tablica A z R
image3 = Image.merge('RGB',(o3, o2, o1)) # zamiana R i B
image4 = Image.merge('RGB',(o2, o1, o3)) # zamiana R i G

plt.figure(figsize=(100, 100))
plt.subplot(2, 2, 1)
plt.imshow(image1)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(image2)
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(image3)
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(image4)
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('fig3.png')
plt.show()









