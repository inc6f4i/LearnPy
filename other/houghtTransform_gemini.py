import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 시각화를 위해 원본 복사본 생성 (직선 선그리기용)
        src_hough = src.copy()
        
        # 1. 컬러 영상을 그레이스케일로 변환
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
        # 2. Sobel + Magnitude 에지 검출
        sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        dst_magnitude = cv2.magnitude(sobel_x, sobel_y)
        dst_sobel = cv2.convertScaleAbs(dst_magnitude)

        # 3. Canny 에지 검출 (허프 변환은 가늘고 명확한 에지 이미지가 입력되어야 잘 작동합니다)
        dst_canny = cv2.Canny(gray, threshold1=50, threshold2=150)

        # 4. cv2.HoughLines 알고리즘 적용
        # rho=1 (1픽셀 해상도), theta=np.pi/180 (1도 해상도), threshold=150 (직선으로 인정할 투표 수)
        lines = cv2.HoughLines(dst_canny, rho=1, theta=np.pi/180, threshold=150)

        # 5. 검출된 직선들을 원본 복사본(src_hough) 위에 그리기
        if lines is not None:
            for i in range(len(lines)):
                rho, theta = lines[i][0]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * rho
                y0 = b * rho
                
                # 계산된 라디안 값을 이용해 화면 끝까지 이어지는 직선의 시작점과 끝점 계산
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                
                # 원본 카피 영상 위에 빨간색(BGR: 0, 0, 255), 두께 2로 직선 그리기
                cv2.line(src_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # 6. 결과 영상들을 각각 다른 창에 출력하여 비교
        cv2.imshow('1. Original', src)
        cv2.imshow('2. Sobel Magnitude', dst_sobel)
        cv2.imshow('3. Canny Edge', dst_canny)
        cv2.imshow('4. Hough Lines (Result)', src_hough)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()