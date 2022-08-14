import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/'

color = cv2.imread(path +'butterfly.jpg',1)


gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
cv2.imwrite(path + 'gray.jpg', gray)

# more efficient than cv2.split
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]

rgba = cv2.merge((b,g,r,g))
cv2.imwrite(path+'rgb.png',rgba)
