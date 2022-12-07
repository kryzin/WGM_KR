from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops
import matplotlib.pyplot as plt
import math

obraz = Image.open('C:/Users/Karolina/PycharmProjects/WGM_KR/lab4/obraz.jpg')
# print("tryb obrazu", obraz.mode)

def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]

# zadanie 1
def filtruj(obraz, kernel, scale):
    obraz_size = int(math.sqrt(len(kernel))), int(math.sqrt(len(kernel)))
    return obraz.filter(ImageFilter.Kernel(size=obraz_size, kernel= kernel, scale= scale))

# plt.imshow(filtruj(obraz, (-1, -1, -1, -1, 6, -1, -1, -1, -1), 1))
# plt.show()
#------------------------------------------------------------
# zadanie 2
info_blur = list(ImageFilter.BLUR.filterargs)
blur = filtruj(obraz,info_blur[3],info_blur[1])
blurA = obraz.filter(ImageFilter.BLUR)

# plt.figure(figsize=(9,3))
# plt.subplot(1,3,1)
# plt.imshow(blur)
# plt.axis('off')
# plt.subplot(1,3,2)
# plt.imshow(blurA)
# plt.axis('off')
# plt.subplot(1,3,3)
# plt.imshow(ImageChops.difference(blur,blurA))
# plt.axis('off')
# plt.savefig('fig1.png')
# plt.show()

#-------------------------------------------------------------
# zadanie 3
obrazL = obraz.convert('L')
info_emboss = list(ImageFilter.EMBOSS.filterargs)
# print(info_emboss)
t1 = (-1, 0, 1, -2, 0, 2, -1, 0, 1)
t2 =  (-1, -2, -1, 0, 0, 0, 1, 2, 1)
sobel1 = obrazL.filter(ImageFilter.Kernel(size= info_emboss[0], kernel= t1, scale= info_emboss[1], offset= info_emboss[2]))
sobel2 = obrazL.filter(ImageFilter.Kernel(size= info_emboss[0], kernel= t2, scale= info_emboss[1], offset= info_emboss[2]))

# plt.figure(figsize=(9,3))
# plt.subplot(1,3,1)
# plt.imshow(obrazL)
# plt.axis('off')
# plt.subplot(1,3,2)
# plt.imshow(sobel1)
# plt.axis('off')
# plt.subplot(1,3,3)
# plt.imshow(sobel2)
# plt.axis('off')
# plt.savefig('fig2.png')
# plt.show()
#-------------------------------------------------------------
# zadanie 4
obraz_detail = obraz.filter(ImageFilter.DETAIL) # 2
obraz_edgem = obraz.filter(ImageFilter.EDGE_ENHANCE_MORE) # 4
obraz_sharpen = obraz.filter(ImageFilter.SHARPEN) # 6
obraz_smoothm = obraz.filter(ImageFilter.SMOOTH_MORE) # 8

# plt.figure(figsize=(8,10))
# plt.subplot(4, 2, 1)
# plt.imshow(obraz_detail)
# plt.axis('off')
# plt.title("DETAIL")
# plt.subplot(4, 2, 2)
# plt.imshow(ImageChops.difference(obraz_detail,obraz))
# plt.axis('off')
# plt.subplot(4, 2, 3)
# plt.imshow(obraz_edgem)
# plt.axis('off')
# plt.title("EDGE_ENHANCE_MORE")
# plt.subplot(4, 2, 4)
# plt.imshow(ImageChops.difference(obraz_edgem,obraz))
# plt.axis('off')
# plt.subplot(4, 2, 5)
# plt.imshow(obraz_sharpen)
# plt.axis('off')
# plt.title("SHARPEN")
# plt.subplot(4, 2, 6)
# plt.imshow(ImageChops.difference(obraz_sharpen,obraz))
# plt.axis('off')
# plt.subplot(4, 2, 7)
# plt.imshow(obraz_smoothm)
# plt.axis('off')
# plt.title("SMOOTH_MORE")
# plt.subplot(4, 2, 8)
# plt.imshow(ImageChops.difference(obraz_smoothm,obraz))
# plt.axis('off')
# plt.savefig("fig3.png")
# plt.show()

# zadanie 4b
# obraz_gaussian = obraz.filter(ImageFilter.GaussianBlur(radius=5))
# obraz_unsharp = obraz.filter(ImageFilter.UnsharpMask(radius=10, percent=150, threshold=2))
# obraz_median = obraz.filter(ImageFilter.MedianFilter(size=5))
# obraz_min = obraz.filter(ImageFilter.MinFilter(size=5))
# obraz_max = obraz.filter(ImageFilter.MaxFilter(size=5))
# plt.figure(figsize=(10,20))
# plt.subplot(5, 2, 1)
# plt.imshow(obraz_gaussian)
# plt.axis('off')
# plt.title("GaussianBlur, radius=5")
# plt.subplot(5, 2, 2)
# plt.imshow(ImageChops.difference(obraz_gaussian,obraz))
# plt.axis('off')
# plt.subplot(5, 2, 3)
# plt.imshow(obraz_unsharp)
# plt.axis('off')
# plt.title("UnsharpMask, radius=10, percent=150, threshold=2")
# plt.subplot(5, 2, 4)
# plt.imshow(ImageChops.difference(obraz_unsharp,obraz))
# plt.axis('off')
# plt.subplot(5, 2, 5)
# plt.imshow(obraz_median)
# plt.axis('off')
# plt.title("MedianFilter, size=5")
# plt.subplot(5, 2, 6)
# plt.imshow(ImageChops.difference(obraz_median,obraz))
# plt.axis('off')
# plt.subplot(5, 2, 7)
# plt.imshow(obraz_min)
# plt.axis('off')
# plt.title("MinFilter, size=5")
# plt.subplot(5, 2, 8)
# plt.imshow(ImageChops.difference(obraz_min,obraz))
# plt.axis('off')
# plt.subplot(5, 2, 9)
# plt.imshow(obraz_max)
# plt.axis('off')
# plt.title("MaxFilter, size=5")
# plt.subplot(5, 2, 10)
# plt.imshow(ImageChops.difference(obraz_max,obraz))
# plt.axis('off')
# plt.savefig("fig4.png")
# plt.show()