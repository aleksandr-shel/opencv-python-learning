import cv2
import os
import numpy as np

path = os.path.dirname(os.path.realpath(__file__)) + '/'

# Gaussian Blur filter
image = cv2.imread(path+'thresh.jpg')
cv2.imshow('Original', image)

# (x,y),sigma
blur = cv2.GaussianBlur(image, (5,55),0)
cv2.imshow('Blur', blur)

# Dilation and Erosion
kernel = np.ones((5,5),'uint8')

# remove black noise?
dilate = cv2.dilate(image,kernel,iterations=1)

# remove light noise?
erode = cv2.erode(image,kernel,iterations=1)

cv2.imshow('Dilate', dilate)
cv2.imshow('Erode',erode)

cv2.waitKey(0)
cv2.destroyAllWindows()