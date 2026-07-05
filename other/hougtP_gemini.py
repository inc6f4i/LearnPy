import cv2
import numpy as np

# 웹캠 열기
cap = cv2.VideoCapture(0)

while(True):
    ret, src = cap.read()

    if (ret):
        # 각각의 결과를 따로 그리기 위해 원본 복사본 2개 생성
        src_hough = src.copy()
        src_hough_p = src.copy()
        
        # 1. 전처리 (그레이스케일 변환 및 Canny 에지 검출)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        dst_canny = cv2.Canny(gray, threshold1=50, threshold2=150)

        # ----------------------------------------------------
        # 방법 A: 표준 허프 변환 (cv2.HoughLines)
        # ----------------------------------------------------
        # 모든 점을 계산하므로 연산량이 많고, 화면 끝에서 끝까지 이어지는 '무한한 직선'을 반환합니다.
        lines = cv2.HoughLines(dst_canny, rho=1, theta=np.pi/180, threshold=150)

        if lines is not None:
            for i in range(len(lines)):
                rho, theta = lines[i][0]
                a, b = np.cos(theta), np.sin(theta)
                x0, y0 = a * rho, b * rho
                # 무한한 직선을 시뮬레이션하기 위해 임의의 큰 값(1000)을 곱해 시작점과 끝점 계산
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * (a))
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * (a))
                # 빨간색(Red) 선으로 그리기
                cv2.line(src_hough, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # ----------------------------------------------------
        # 방법 B: 확률적 허프 변환 (cv2.HoughLinesP)
        # ----------------------------------------------------
        # 무작위로 샘플링하여 연산이 빠르고, 선의 시작점과 끝점 좌표 [x1, y1, x2, y2]를 직접 반환하므로 '선분'을 그립니다.
        # minLineLength: 선으로 인정할 최소 길이 (픽셀)
        # maxLineGap: 같은 선 위에 있는 점들 사이의 최대 허용 간격
        lines_p = cv2.HoughLinesP(dst_canny, rho=1, theta=np.pi/180, threshold=50, 
                                  minLineLength=50, maxLineGap=10)

        if lines_p is not None:
            for i in range(len(lines_p)):
                # 시작점(x1, y1)과 끝점(x2, y2)을 곧바로 활용 가능
                x1, y1, x2, y2 = lines_p[i][0]
                # 초록색(Green) 선으로 그리기
                cv2.line(src_hough_p, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # 2. 두 가지만 출력해서 명확하게 비교
        cv2.imshow('1. Standard HoughLines (Red)', src_hough)
        cv2.imshow('2. Probabilistic HoughLinesP (Green)', src_hough_p)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()