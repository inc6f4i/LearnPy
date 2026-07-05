import cv2
import numpy as np
import sys

# 카메라 열기 (두 번째 인자 플래그 제거)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    sys.exit()

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while True:
    ret, src = cap.read() 

    if ret:
        # 1. 그레이스케일 변환 및 이진화 (레이블링을 위한 필수 전처리)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        # 오츠(Otsu) 알고리즘으로 최적의 임계값을 자동으로 찾아 이진화합니다.
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # 2. connectedComponentsWithStats 적용
        # retval: 객체 개수 (배경 포함)
        # labels: 객체마다 번호(0, 1, 2...)가 매겨진 맵
        # stats: 객체의 위치(x, y), 가로(w), 세로(h), 면적(area) 정보
        # centroids: 객체의 중심점(x, y) 좌표
        retval, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

        # 원본 영상(src) 위에 결과를 그리기 위해 복사본 생성
        dst = src.copy()

        # 3. 발견된 객체들을 순회하며 시각화 (0번은 배경이므로 1번부터 시작)
        for i in range(1, retval):
            # stats에서 정보 추출
            x = stats[i, cv2.CC_STAT_LEFT]
            y = stats[i, cv2.CC_STAT_TOP]
            w = stats[i, cv2.CC_STAT_WIDTH]
            h = stats[i, cv2.CC_STAT_HEIGHT]
            area = stats[i, cv2.CC_STAT_AREA]

            # 너무 작은 노이즈(예: 면적 100 픽셀 이하)는 무시하기
            if area < 100:
                continue

            # centroids에서 중심점 추출
            cx, cy = centroids[i]

            # 객체 테두리에 노란색 사각형 그리기 (두께 2)
            cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 255), 2)
            
            # 객체 중심에 빨간색 점 그리기 (반지름 3, 채우기)
            cv2.circle(dst, (int(cx), int(cy)), 3, (0, 0, 255), -1)

        # 4. 결과 출력
        cv2.imshow('Binary Image', binary) # 이진화된 모습 확인용
        cv2.imshow('Result (dst)', dst)    # 사각형과 점이 그려진 최종 화면

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv2.destroyAllWindows()