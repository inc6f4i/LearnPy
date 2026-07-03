#실습-4-해답
#
import cv2
import numpy as np
import os
#
path = os.path.dirname(os.path.abspath(__file__))
#img = cv2.imread(path+r'\lena.jpg', cv2.IMREAD_GRAYSCALE)

img = cv2.imread(path+r'\baseball-player00.jpg')

# ball = img[409:454, 817:884] # ROI 설정 (야구공 영역)
# img[470:515, 817:884] = ball # ROI 영역을 다른 영역에 복사

grass = img[470:515, 817:884] # ROI 설정 (야구공 아래의 잔디 영역)
img[409:454, 817:884] = grass # ROI 영역을 다른 영역에 복사

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



