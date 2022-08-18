import os
import cv2

path = os.path.dirname(os.path.realpath(__file__)) + '/'
img = cv2.imread(path+'faces.jpeg',1)
# img = cv2.imread(path+'photo.jpg',1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar = path+'haarcascade_eye.xml'

eye_cascade = cv2.CascadeClassifier(haar)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.02, minNeighbors=20, minSize=(10,10))
print(len(eyes))

for (x, y, w, h) in eyes:
    # cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
    xc = (x+x+w)/2
    yc = (y+y+h)/2
    rad = w/2
    cv2.circle(img,(int(xc),int(yc)), int(rad), (0,255,0),2)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()