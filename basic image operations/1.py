
import cv2
import os
# get script's path
img = cv2.imread(os.path.dirname(os.path.realpath(__file__)) + '/opencv-logo.png')
cv2.namedWindow("imageblbl",cv2.WINDOW_NORMAL)
cv2.imshow('imageblbl', img)

cv2.waitKey(0)
cv2.imwrite(os.path.dirname(os.path.realpath(__file__))+ "/output.jpg",img)

cv2.destroyAllWindows()