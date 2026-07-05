import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 1. 컬러 영상을 그레이스케일(흑백)로 변환 (에지 검출 효율 상승)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
        # 2. X방향 및 Y방향 Sobel 미분 계산 (음수 값 보존을 위해 cv2.CV_64F 사용)
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        
        # 3. X, Y 미분 값을 합쳐서 크기(Magnitude) 계산
        dst_magnitude = cv2.magnitude(sobel_x, sobel_y)
        
        # 4. 화면 출력을 위해 8비트(0~255) unsigned int 형태로 변환
        dst = cv2.convertScaleAbs(dst_magnitude)

        # 5. 결과 영상 출력
        cv2.imshow('Edge Detection (Sobel Magnitude)', dst)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()