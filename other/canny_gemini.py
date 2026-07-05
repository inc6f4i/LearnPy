import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 1. 컬러 영상을 그레이스케일로 변환
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
        # ----------------------------------------------------
        # 방법 A: Sobel + Magnitude (직접 에지 크기 계산)
        # ----------------------------------------------------
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        dst_magnitude = cv2.magnitude(sobel_x, sobel_y)
        dst_sobel = cv2.convertScaleAbs(dst_magnitude) # 최종 Sobel 결과물

        # ----------------------------------------------------
        # 방법 B: Canny Edge Detection (기본 파라미터 적용)
        # ----------------------------------------------------
        # threshold1 (하한 임계값): 50, threshold2 (상한 임계값): 150으로 설정
        # apertureSize(소벨 커널 크기)는 기본값 3, L2gradient는 False가 기본입니다.
        dst_canny = cv2.Canny(gray, threshold1=50, threshold2=150)

        # 2. 결과 영상들을 각각 다른 창에 출력
        cv2.imshow('Original', src)
        cv2.imshow('Sobel Magnitude', dst_sobel)
        cv2.imshow('Canny Edge', dst_canny)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()