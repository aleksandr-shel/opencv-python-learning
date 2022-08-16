import numpy as np
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/'

bw = cv2.imread(path+'detect_blob.png',0)
height, width = bw.shape[0:2]
cv2.imshow('Original BW',bw)

binary = np.zeros([height,width,1], 'uint8')

thresh = 85

# slow binary segmentation
for row in range(0,height):
    for col in range(0, width):
        if (bw[row][col] >thresh):
            binary[row][col]=255
        else:
            binary[row][col]=0

cv2.imshow('Slow binary',binary)

# built in binary segmentation (faster)
ret, thresh = cv2.threshold(bw, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow('CV Threshold', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()