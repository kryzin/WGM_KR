from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt

# zadanie 1
im = Image.open('image.jpg')
im = im.convert('L')
print("tryb obrazu", im.mode)
# im.show()

print("-----------------------------------------")
# zadanie 2
def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)
    print("count ", s.count)
    print("mean ", s.mean)
    print("median ", s.median)
    print("stddev ", s.stddev)

statystyki(im)
hist = im.histogram()
# plt.title("histogram")
# plt.bar(range(256), hist[:256])
# plt.show()
print("-----------------------------------------")
# zadanie 3
def histogram_norm(im):
    hist = im.histogram()
    for i in range(256):
        hist[i] = int(hist[i] / 256)
    return hist

hist_norm = histogram_norm(im)
# plt.title("histogram znormalizowany")
# plt.bar(range(256), hist_norm[:256])
# plt.show()
print("-----------------------------------------")
# zadanie 4
def histogram_cumul(im):
    hist = histogram_norm(im)
    sum = 0
    for i in range(256):
        sum += hist[i]
        hist[i] = sum
    return hist

hist_kumul = histogram_cumul(im)
# plt.title("histogram skumulowany")
# plt.bar(range(256), hist_kumul[:256])
# plt.show()
print("-----------------------------------------")
# zadanie 5
def histogram_equalization(im):
    im_eq = im.point(lambda p: int(255 * p))
    return im_eq

im_equalized = histogram_equalization(im)
im_equalized.show()

print("-----------------------------------------")
# zadanie 6
im_equalized1 = ImageOps.equalize(im)
im_equalized1.show()

plt.figure(figsize=(10,10))
plt.subplot(1,2,1)
plt.imshow(im_equalized)
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(im_equalized1)
plt.axis('off')
# plt.savefig('fig1.png')
plt.show()

diff=ImageChops.difference(im_equalized1, im_equalized)
print("statystyki róznicy: ")
statystyki(diff)


