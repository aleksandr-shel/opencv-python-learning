import numpy as np
import os
import cv2
img = cv2.imread(os.path.dirname(os.path.realpath(__file__)) + '/opencv-logo.png', 1)



print(img)
print(len(img))
print(len(img[0]))
print(len(img[0][0]))
print(img.shape)
print(img.size)
print(type(img))
print(img.dtype)

print(img[10,5])

# all pixels in one channel

print(img[:,:,0])