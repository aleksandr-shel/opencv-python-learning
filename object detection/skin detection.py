import numpy as np
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/'

img = cv2.imread(path+'faces.jpeg',1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h = hsv[:, :, 0]
s = hsv[:, :, 1]
v = hsv[:, :, 2]

hsv_split = np.concatenate((h,s,v), axis = 1)
hsv_split_scaled = cv2.resize(hsv_split,(0,0),fx=0.2, fy=0.2)
cv2.imshow('Split hsv scaled', hsv_split_scaled)


ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow('Sat filter', cv2.resize(min_sat,(0,0),fx=0.2, fy=0.2))

# important THRESH_BINARY_INV 0-15 white, 15-255 black
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('Hue filter', cv2.resize(max_hue,(0,0),fx=0.2, fy=0.2))

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow('Final',cv2.resize(final,(0,0),fx=0.2, fy=0.2))
cv2.imshow('Original',cv2.resize(img,(0,0),fx=0.2, fy=0.2))

cv2.waitKey(0)
cv2.destroyAllWindows()