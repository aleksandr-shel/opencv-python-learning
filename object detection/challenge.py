import numpy as np
import cv2
import os
import random
path = os.path.dirname(os.path.realpath(__file__)) + '/'
img = cv2.imread(path + "fuzzy.png",1)
cv2.imshow('Original',img)

kernel = np.ones((5,5), 'uint8')
print(kernel)
dilate = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Dilate', dilate)

# gray = cv2.cvtColor(dilate, cv2.COLOR_RGB2GRAY)
gray = cv2.cvtColor(dilate, cv2.COLOR_RGB2GRAY)


thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)
cv2.imshow('Binary', thresh)


erode = cv2.erode(thresh, kernel, iterations=5)
cv2.imshow('Erode',erode)

thresh2 = cv2.adaptiveThreshold(erode, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 115,1)
cv2.imshow('Binary 2', thresh2)

contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

index = -1
thickness = 4
color = (255,0,255)

objects = np.zeros([img.shape[0],img.shape[1],3],'uint8')
canvas = np.ones([500,500,3],'uint8')*255

for c in contours:
    col = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    cv2.drawContours(objects, [c], -1, col, -1)

    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print(area,perimeter)

cv2.imshow('Contours', objects)

cv2.waitKey(0)
cv2.destroyAllWindows()