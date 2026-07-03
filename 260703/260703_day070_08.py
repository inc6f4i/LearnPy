import cv2
import numpy as np

def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

img = np.zeros((300, 512, 3), np.uint8) # 검정색 배경 이미지 생성
cv2.namedWindow('image') # 윈도우 창 생성

# Trackbar 생성 및 윈도우 창에 등록
cv2.createTrackbar('R', 'image', 0, 255, nothing) # R 값 Trackbar
cv2.createTrackbar('G', 'image', 0, 255, nothing) # G 값 Trackbar
cv2.createTrackbar('B', 'image', 0, 255, nothing) # B 값 Trackbar

switch = '0:OFF\n1:On' # Switch Trackbar 이름
cv2.createTrackbar(switch, 'image', 1, 1, nothing) # Switch Trackbar (0 또는 1 값)

while(1):
    cv2.imshow('image', img) # 이미지 표시

    if cv2.waitKey(1) & 0xFF == 27: # ESC 키 입력 시 종료
        break

    # Trackbar 현재 Position 값 얻기
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image') # Switch Trackbar 값

    if s == 0: # Switch Off (초기화)
        img[:] = 0 # 검정색 배경으로 변경
    else: # Switch On
        img[:] = [b, g, r] # RGB 값으로 배경색 변경

cv2.destroyAllWindows()