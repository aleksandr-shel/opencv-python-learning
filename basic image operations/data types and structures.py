import numpy as np
import cv2

# create black image
black = np.zeros([150,400,1], 'uint8')
cv2.imshow('Black',black)
print(black[0][0])

# create image of ones (still black)
ones = np.ones([150,400,3],'uint8')
cv2.imshow('Ones', ones)
print(ones[0,0,:])

#create white image
white = np.ones([150,400,3],'uint16')
white *= (2**16 - 1)
cv2.imshow('white', white)
print(white[0,0,:])

#create colored image
color = ones.copy()
color[:,:] = (255,0,0)
cv2.imshow('Colored', color)
print(color[0,0,:])

cv2.waitKey(0)
cv2.destroyAllWindows()