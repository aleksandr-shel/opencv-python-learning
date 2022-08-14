import cv2
import os
import numpy as np

path = os.path.dirname(os.path.realpath(__file__)) + '/'

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    cv2.imshow('Frame', frame)

    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()