from PIL import Image, ImageFilter
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

# statystyki(im)
# hist = im.histogram()
# plt.title("histogram")
# plt.bar(range(256), hist[:256])
# plt.show()
print("-----------------------------------------")
# zadanie 3
def histogram_norm(im):
    h, w = im.size
    hist = im.histogram()
    hist_norm = hist.copy()
    zakres = h * w
    for i in range(0,len(hist),1):
        hist_norm[i] = hist[i] / zakres
    return hist_norm

# hist_norm = histogram_norm(im)
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

# hist_kumul = histogram_cumul(im)
# plt.title("histogram skumulowany")
# plt.bar(range(256), hist_kumul[:256])
# plt.show()
print("-----------------------------------------")
# zadanie 5
def histogram_equalization(im):
    return im.point(lambda p: int(255 * histogram_cumul(im)[p]))

equalized = histogram_equalization(im)
# equalized.show()
# equalized.save('equalized.png')
print("-----------------------------------------")
# zadanie 6
equalized1 = ImageOps.equalize(im)
# equalized1.show()
# equalized1.save('equalized1.png')

# diff=ImageChops.difference(equalized1, equalized)
# plt.figure(figsize=(10,10))
# plt.subplot(1,1,1)
# plt.imshow(diff,'gray')
# plt.axis('off')
# plt.show()
#
# plt.figure(figsize=(10,4))
# plt.subplot(1,2,1)
# plt.title("histogram equalized")
# plt.bar(range(256), equalized.histogram()[:256])
# plt.subplot(1,2,2)
# plt.title("histogram equalized1")
# plt.bar(range(256), equalized1.histogram()[:256])
# plt.show()
#
# statystyki(equalized)
# print("**************************")
# statystyki(equalized1)
#
# print("statystyki róznicy: ")
# statystyki(diff)
print("-----------------------------------------")
# zadanie 7
equalized1 = equalized1.convert("RGB")
eq_detail = equalized1.filter(ImageFilter.DETAIL).convert("RGB")
eq_sharpen = equalized1.filter(ImageFilter.SHARPEN).convert("RGB")
eq_contour = equalized1.filter(ImageFilter.CONTOUR).convert("RGB")
fig = plt.figure(figsize=(8,8))
fig.add_subplot(2, 2, 1)
plt.title("obraz początkowy")
plt.imshow(equalized1)
plt.axis('off')
fig.add_subplot(2, 2, 2)
plt.title("DETAIL")
plt.imshow(eq_detail)
plt.axis('off')
fig.add_subplot(2, 2, 3)
plt.title("SHARPEN")
plt.imshow(eq_sharpen)
plt.axis('off')
fig.add_subplot(2, 2, 4)
plt.title("CONTOUR")
plt.imshow(eq_contour)
plt.axis('off')
plt.savefig("filtry.png")
plt.show()


