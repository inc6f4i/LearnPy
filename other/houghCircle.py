import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 1. 전처리: 그레이스케일 변환 및 노이즈 제거(블러링)
        # 노이즈를 줄여야 원치 않는 가짜 원들이 검출되는 것을 막을 수 있습니다.
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (9, 9), 2)

        # 2. cv2.HoughCircles 알고리즘 적용
        # dp=1 (입력 영상과 동일한 해상도), minDist=50 (검출된 원 중심 간의 최소 거리)
        # param1=50 (Canny 에지 상한 임계값), param2=30 (원 중심 투표 빈도 임계값 - 낮을수록 원이 많이 검출됨)
        # minRadius=10, maxRadius=200 (검출할 원의 최소/최대 반지름 픽셀 크기)
        circles = cv2.HoughCircles(
            blurred, 
            cv2.HOUGH_GRADIENT, 
            dp=1, 
            minDist=50, 
            param1=50, 
            param2=30, 
            minRadius=10, 
            maxRadius=200
        )

        # 3. 검출된 원이 있다면 화면에 그리기
        if circles is not None:
            # 정수형태로 좌표 및 반지름 변환
            circles = np.uint16(np.around(circles))
            
            for i in circles[0, :]:
                center = (i[0], i[1]) # 원의 중심 좌표 (x, y)
                radius = i[2]         # 원의 반지름 (r)
                
                # 원의 외곽선 그리기 (초록색, 두께 3)
                cv2.circle(src, center, radius, (0, 255, 0), 3)
                # 원의 중심점 찍기 (빨간색 점)
                cv2.circle(src, center, 2, (0, 0, 255), 5)

        # 4. 결과 영상 출력
        cv2.imshow('Hough Circles Detection', src)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()