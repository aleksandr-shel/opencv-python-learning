import numpy as np
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/'

template = cv2.imread(path+'template2.jpg', 0)
# template = cv2.imread(path+'template.jpg', 0)
frame = cv2.imread(path+'players.jpg',0)

cv2.imshow('Frame', frame)
cv2.imshow('Template', template)

# двумерная матрица 
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
# print(result)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(max_val, max_loc)

cv2.circle(result, max_loc, 15, 255, 2)

cv2.imshow('Matching', result)

cv2.waitKey(0)
cv2.destroyAllWindows()