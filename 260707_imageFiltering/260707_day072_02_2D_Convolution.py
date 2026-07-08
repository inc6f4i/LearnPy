#260707_day072_02_.py
import cv2
import numpy as np

def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

img = cv2.imread(r'C:\Users\user\Desktop\imaging\lena.png')

cv2.namedWindow('image')
cv2.createTrackbar('K', 'image', 1, 1024, nothing) # K Trackbar (Kernel Size 조절)

while(1):
    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 입력 시 종료
        break

    k = cv2.getTrackbarPos('K', 'image') # Trackbar 값 얻기

    if k == 0: # Kernel Size 가 0 이면 에러 발생 방지 (최소 1로 설정)
        k = 1

    # Kernel 생성 (k x k Averaging Filter)
    kernel = np.ones((k, k), np.float32) / (k * k)
    dst = cv2.filter2D(img, -1, kernel) # 2D Convolution 필터링 적용

    cv2.imshow('image', dst) # 필터링 결과 이미지 표시

cv2.destroyAllWindows()