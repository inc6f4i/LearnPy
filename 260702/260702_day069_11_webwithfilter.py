import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 카메라 장치 0번, 보통 숫자로

# 카메라 속성 확인 (width, height)
print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

# 카메라 속성 변경 (width, height 설정)
cap.set(3, 320) # width
cap.set(4, 240) # height

while(True):
    ret, frame = cap.read() # 프레임 읽기

    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # GrayScale 변환
        blurred_image = cv2.GaussianBlur(gray, (5, 5), 0) ### 얘는 그냥 이미지

    # 샤프닝
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) ### 얘도 그냥이미지
        sharpened_image = cv2.filter2D(blurred_image, -1, kernel)
        
        edges = cv2.Canny(sharpened_image, 100, 200)
        edges = cv2.line(edges,(0,0),(240,240),255,8)
        edges = cv2.circle(edges,(0,0),(240,240),255,8)
        sobelx = cv2.Sobel(sharpened_image, cv2.CV_64F, 1, 0, ksize=5) ### 소벨필터는 그레이스케일 한놈
        sobely = cv2.Sobel(sharpened_image, cv2.CV_64F, 0, 1, ksize=5)
        
        cv2.imshow('frame3', sobelx) # GrayScale 프레임 표시
        cv2.imshow('frame2', edges) # GrayScale 프레임 표시
        cv2.imshow('frame1', sobely) # GrayScale 프레임 표시
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' 키 입력 시 종료
            break
    else:
        break#카메라가 없으니 ret에서 0을 안줘서 True가 계속되나?

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기