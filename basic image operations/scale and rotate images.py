import cv2
import os
import numpy as np

path = os.path.dirname(os.path.realpath(__file__)) + '/'
img = cv2.imread(path+'players.jpg')
# Scaling
img_half = cv2.resize(img, (0,0),fx=0.5, fy=0.5)
img_stretch = cv2.resize(img, (600,600))

# no interpolation was done during the scaling process
img_stretch_near = cv2.resize(img, (600,600), interpolation=cv2.INTER_NEAREST)

cv2.imshow('Half', img_half)
cv2.imshow('Stretch',img_stretch)
cv2.imshow('Stretch_near', img_stretch_near)

# Rotation
M = cv2.getRotationMatrix2D((img.shape[1]/2,img.shape[0]/2), -90, 2)
rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow('Rotated', rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()