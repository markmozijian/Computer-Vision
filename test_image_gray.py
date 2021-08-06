# -*- coding: utf-8 -*-
"""
@author: Mark

image gray level processing and binaryzation
"""
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

plt.subplot(221)
img = plt.imread("lenna.png") 
img.shape
plt.imshow(img)
print("\nimage lenna:\n")
print(img)
 
# gray level processin
img_gray = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gray, cmap='gray')
print("\nimage gray:\n")
print(img_gray)

img_gray.shape

# gray level binaryzation
img_binary = np.where(img_gray >= 0.5, 1, 0) 
print("\nimage_binary:\n")
print(img_binary)
print(img_binary.shape)
plt.subplot(223) 
plt.imshow(img_binary, cmap='gray')
plt.show()
