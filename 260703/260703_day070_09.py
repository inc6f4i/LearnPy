import cv2
import numpy as np

img = cv2.imread(r'C:\Users\user\Desktop\imaging\lena.png')

px = img[100, 200] # (100, 200) 좌표 Pixel 값 (BGR)
print(px) # 출력 예: [157 100 190] (BGR 값)
blue = img[100, 200, 0] # (100, 200) 좌표 Blue 채널 값
print(blue) # 출력 예: 157

img[10, 100] = [255,255,255]
img.item(10,10,)
cv2.imshow('d',img)

cv2.waitKey(3000)
cv2.destroyAllWindows