import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
color = (255,0,0)
line_width=3
radius=3
point = (0,0)
pressed = False

# click callback
def click(event, x, y, flags, param):
    global canvas, color, point, pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # canvas[point[0] - radius: point[0] + radius,point[1] - radius: point[1] + radius,:]=color
        pressed = True
        cv2.circle(canvas,point,radius,color,line_width)
    elif event == cv2.EVENT_MOUSEMOVE:
        if pressed == True:
            cv2.circle(canvas,point,radius,color,line_width)
        point = (x,y)
    elif event == cv2.EVENT_LBUTTONUP:
        pressed = False
        color = (255,0,0) if color == (0,255,0) else (0,255,0)

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# cv2.imshow("canvas",canvas)
# Forever draw loop
while True:
    cv2.imshow("canvas",canvas)
	# key capture every 1ms
    ch = cv2.waitKey(1)
    if ch & 0xFF == ord('q'):
        break
	

cv2.destroyAllWindows()