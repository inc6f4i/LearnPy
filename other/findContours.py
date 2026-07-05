import cv2
import numpy as np
import sys

# 카메라 열기
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    sys.exit()

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while True:
    ret, src = cap.read() 

    if ret:
        # 1. 그레이스케일 변환 및 이진화 (외곽선 검출을 위한 필수 전처리)
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # 2. findContours 적용
        # - mode=cv2.RETR_EXTERNAL: 가장 바깥쪽 외곽선만 검출 (내부 구멍 무시)
        # - method=cv2.RETR_TREE 등을 쓰면 계층 구조(hierarchy)까지 완벽히 검출 가능
        # - method=cv2.CHAIN_APPROX_NONE: 외곽선의 모든 점 좌표를 저장
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # 결과를 그릴 복사본 이미지
        dst = src.copy()

        # 3. 검출된 외곽선 순회하며 그리기
        count = 0
        for pts in contours:
            # 노이즈 제거: 외곽선이 감싸는 면적이 너무 작으면 무시 (예: 100 픽셀 이하)
            if cv2.contourArea(pts) < 100:
                continue
                
            count += 1

            # 각 외곽선(pts)을 dst 이미지에 초록색(0, 255, 0) 선으로 그리기 (두께 2)
            # -1은 contours 리스트 안의 특정 인덱스가 아니라 단일 외곽선 자체를 그린다는 의미입니다.
            cv2.drawContours(dst, [pts], -1, (0, 255, 0), 2)

            # (선택) 외곽선을 감싸는 사각형 좌표를 구해 텍스트를 쓸 위치 지정
            x, y, w, h = cv2.boundingRect(pts)
            cv2.putText(dst, f"Obj {count}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

        # 발견된 총 객체 수를 화면 좌측 상단에 표시
        cv2.putText(dst, f"Total Objects: {count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # 4. 결과 출력
        cv2.imshow('Binary', binary)
        cv2.imshow('Result (Contours)', dst)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv2.destroyAllWindows()