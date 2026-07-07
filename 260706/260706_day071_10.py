#260706_day071_10_.py
import cv2
import numpy as np

img = cv2.imread(r'C:\Users\user\Desktop\imaging\xas1.png')

height, width = img.shape[:2] # 이미지 높이, 너비

# 이미지 축소 (Shrink)
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# 수동 크기 지정 (Manual Size)
zoom1 = cv2.resize(img, (400, 400), interpolation=cv2.INTER_CUBIC)
"""
x+1 y+1
x*2 y*2 변한가능
"""
# 배수 크기 지정 (Scale Factor)
zoom2 = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
"""
보통 이렇게 함
"""
cv2.imshow('Original', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()