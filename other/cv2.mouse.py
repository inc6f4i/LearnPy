import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x, y
        print(f"Left button clicked at ({x}, {y})")
    elif event == cv2.EVENT_LBUTTONUP:
        print(f"Left button released at ({x}, {y})")
    elif event == cv2.EVENT_MOUSEMOVE:
        if flags & cv2.EVENT_FLAG_LBUTTON:
            cv2.line(img, (oldx, oldy), (x, y), (255, 0, 0), 5)
            cv2.imshow('Mouse Drawing', img)
            oldx, oldy = x, y
        
img = np.full((512, 512, 3), 255, np.uint8)
cv2.namedWindow('Mouse Drawing')
cv2.imshow('Mouse Drawing', img)
cv2.setMouseCallback('Mouse Drawing', on_mouse, img)

cv2.waitKey(0)
cv2.destroyAllWindows()
