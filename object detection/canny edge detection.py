import numpy as np
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/'

img = cv2.imread(path+'tomatoes.jpg')

# simple threshold
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# hue 0-25 - red
res, thresh = cv2.threshold(hsv[:,:,0], 25, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Thresh', thresh)

# 
edges = cv2.Canny(img, 100, 70)
cv2.imshow('Canny', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
