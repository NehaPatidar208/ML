
import cv2
import numpy as np


"""
# show original image

img=cv2.imread('img2.png')
print(img.shape)
cv2.imshow('image',img)
cv2.waitKey(0)
"""

"""#grayed image
gray_img=cv2.imread('img2.png',0)
cv2.imshow('image',gray_img)
cv2.waitKey(0)
"""
# r,g,b image
img=cv2.imread('img2.png')
#b,g,r=cv2.split(img)
#new_img=cv2.merge([b,g,r])
# new_img=cv2.merge([b+40,g+20,r+40])
# cv2.imshow('new_image',new_img)
#cv2.waitKey(0)

#cropped image
print(img.shape)
cr_img=img[100:500,250:600]
cv2.imshow("Cropped image",cr_img)
cv2.waitKey(0)