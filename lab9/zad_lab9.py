from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# zadanie 1a
obraz1 = Image.open('obraz1.png')
obraz2 = obraz1.copy().convert('RGB')

# zadanie 1b
r,g,b,a = obraz1.split()
# a.show()
obraz3 = Image.new('RGB', obraz1.size, (255,255,255))
obraz3.paste(obraz1, (0, 0), a)

# zadanie 1c
roznica = ImageChops.difference(obraz2,obraz3)
# roznica.show()
#-------------------------------------------------------
# zadanie 2a
tryby = ['CMYK','YCbCr','HSV']
plt.figure(figsize=(10,6))
plt.subplot(1,3,1)
plt.imshow(obraz1.convert('CMYK'))
plt.title("CMYK")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(obraz1.convert('YCbCr'))
plt.title("YCbCr")
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(obraz1.convert('HSV'))
plt.title("HSV")
plt.axis('off')
plt.savefig('fig1.png')
# plt.show()

# zadanie 2b
c,m,y,k = obraz1.convert('CMYK').split()
plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
plt.imshow(c)
plt.title("kanał Cyan")
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(m)
plt.title("Kanał Magenta")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(y)
plt.title("Kanał Yellow")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(k)
plt.title("Kanał Key")
plt.axis('off')
plt.savefig('cmyk.png')
# plt.show()

y, cb, cr = obraz1.convert('YCbCr').split()
plt.figure(figsize=(10,6))
plt.subplot(1,3,1)
plt.imshow(y)
plt.title("kanał Luminance")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(cb)
plt.title("Kanał Chroma Blue")
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(cr)
plt.title("Kanał Chroma Red")
plt.axis('off')
plt.savefig('ycbcr.png')
# plt.show()

h,s,v = obraz1.convert('HSV').split()
plt.figure(figsize=(10,6))
plt.subplot(1,3,1)
plt.imshow(h)
plt.title("kanał Hue")
plt.axis('off')
plt.subplot(1,3,2)
plt.imshow(s)
plt.title("Kanał Saturation")
plt.axis('off')
plt.subplot(1,3,3)
plt.imshow(v)
plt.title("Kanał Value/Intensity")
plt.axis('off')
plt.savefig('hsv.png')
# plt.show()
#-----------------------------------------------
# zadanie 3a
obraz4 = Image.open('obraz4.png')
obraz4 = obraz4.resize(obraz1.size, 1)
obraz4a = obraz4.copy()
obraz4a.paste(obraz1, (0,0), a)
obraz4a.show()

obraz1a = obraz1.copy()
obraz1a.paste(obraz4, (0,0), a)
obraz1a.show()

plt.figure(figsize=(5,3))
plt.subplot(1,2,1)
plt.imshow(obraz4a)
plt.title('obraz1 na obraz4')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(obraz1a)
plt.title('obraz4 na obraz1')
plt.axis('off')
plt.savefig('fig2.png')
# plt.show()



