import numpy as np
import cv2
import os

path = os.path.dirname(os.path.realpath(__file__)) + '/'

# img = cv2.imread(path+'faces.jpeg', 1)
img = cv2.imread(path+'photo.jpg', 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar = path+'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(40,40))
print(len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()