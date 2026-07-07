import cv2
import numpy as np

img1 = cv2.imread(r'C:\Users\user\Desktop\imaging\a7.jpg')
img2 = cv2.imread(r'C:\Users\user\Desktop\imaging\a2.png')

def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing) # W Trackbar (Blending 비율 조절)

while True:
    w = cv2.getTrackbarPos('W', 'image') # Trackbar 값 얻기

    alpha = float(100 - w) * 0.01 # img1 가중치 (0.01 ~ 1.0)
    beta = float(w) * 0.01 # img2 가중치 (0.01 ~ 1.0)

    dst = cv2.addWeighted(img1, alpha, img2, beta, 0) # 이미지 Blending

    cv2.imshow('dst', dst) # Blending 결과 이미지 표시

    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 입력 시 종료
        break

cv2.destroyAllWindows()