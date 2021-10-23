import numpy as np
import matplotlib.pyplot as plt

img=plt.imread('myimg.png')
print(img.dtype,img.ndim,img.size,img.shape)
# print(img)
blur_img=img.copy()

def blur_img_func(img):
    blur_img=(img[:-2,1:-1]       # top
                + img[2:,1:-1]      # bottom
                + img[1:-1,1:-1]    # center
                + img[1:-1,:-2]     # left
                + img[1:-1,2:] )/5    # right
    return blur_img

for i in range(10):
    blur_img=blur_img_func(blur_img)

print(blur_img.dtype,blur_img.ndim,blur_img.size,blur_img.shape)

plt.imshow(img,cmap=plt.cm.hot)
plt.figure()
plt.imshow(blur_img,cmap=plt.cm.hot)
plt.show()