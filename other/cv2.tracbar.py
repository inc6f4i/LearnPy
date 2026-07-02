import cv2
import numpy as np
blurred_image = None
def change_brightness(pos):
    global blurred_image
    factor = pos / 100
    adjusted = cv2.convertScaleAbs(blurred_image, alpha=factor, beta=0)
    cv2.imshow('frame2', adjusted)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap.set(3, 320) # width
cap.set(4, 240) # height

cv2.namedWindow('frame2')
cv2.createTrackbar('Brightness', 'frame2', 100, 200, change_brightness)
while(True):
    ret, frame = cap.read() # 프레임 읽기

    if (ret):
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray, (5, 5), 0) 
        cv2.imshow('frame2', blurred_image)
        current_pos = cv2.getTrackbarPos('Brightness', 'frame2')
        change_brightness(current_pos)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' 키 입력 시 종료
            break
    else:
        break#카메라가 없으니 ret에서 0을 안줘서 True가 계속되나?

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기




cv2.waitKey(0)
cv2.destroyAllWindows()
