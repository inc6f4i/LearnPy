import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (100, 100), (400, 400), (0, 0, 255), 1) #img = 대상 x,y 좌표, 색상, 두께
cv2.circle(img, (1512, 1512), 500, (255, 0, 0), 2, cv2.LINE_AA, 2)
cv2.circle(img, (256*4, 256*4), 50, (0,255,255), 2, cv2.LINE_AA, 2)
cv2.ellipse(img, (256, 230), (60, 30), 45, 0, 180, (255, 255, 255), 2)
cv2.polylines(img, [np.array([[85, 175], [281, 180], [100, 190],[277, 200], [90, 210], [290, 220]], np.int32)], True, (0, 255, 255), 2)
cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2)

cv2.imshow('Lines', img)
cv2.waitKey(0)  
cv2.destroyAllWindows()