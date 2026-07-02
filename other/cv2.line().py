import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (50, 50), (200, 50), (255, 0, 0), 5)
cv2.line(img, (50, 60), (150, 160), (0, 255, 0))
cv2.arrowedLine(img, (150, 100), (250, 300), (0, 0, 255),3,1,0, 0.1)
cv2.drawMarker(img, (256, 256), (255, 255, 0), cv2.MARKER_STAR, 20, 2)
cv2.rectangle(img, (300, 300), (400, 400), (255, 0, 255), 1)
cv2.rectangle(img, (200, 300), (350, 350), (255, 0, 255), 1)
cv2.circle(img, (400, 400), 50, (255, 255, 0), 2, cv2.LINE_AA, 2)
cv2.ellipse(img, (230, 230), (60, 30), 45, 0, 180, (255, 255, 255), 2)
cv2.polylines(img, [np.array([[100, 300], [200, 400], [300, 300],[100, 200], [140, 240], [200, 200]], np.int32)], True, (0, 255, 255), 2)
cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 2, cv2.LINE_AA)



cv2.imshow('Lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
