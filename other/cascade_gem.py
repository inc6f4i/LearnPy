import cv2
import numpy as np
import os

# 1. 가중치 파일(XML) 로드 및 분류기 초기화
# OpenCV에 내장된 정면 얼굴 검출 모델 파일의 절대 경로를 가져옵니다.
xml_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(xml_path)

# 분류기가 정상적으로 로드되었는지 확인
if face_cascade.empty():
    print("⚠️ 오류: Cascade 분류기 파일을 로드할 수 없습니다.")
    exit()

# 웹캠 열기
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 2. 검출 속도와 정확도를 위해 그레이스케일 변환
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
        # 3. 멀티스케일 객체 검출 실행
        # scaleFactor: 이미지 피라미드에서 이미지를 얼마나 줄여가며 검출할지 (1.1은 10%씩 줄임)
        # minNeighbors: 검출 영역이 최종 후보로 인정받기 위해 겹쳐야 하는 최소 사각형 개수 (노이즈 방지)
        # minSize: 검출할 최소 객체 크기 (예: 너무 작은 얼굴 영역은 무시)
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        # 4. 검출된 얼굴 영역에 사각형 그리기
        # faces는 [[x, y, w, h], [x, y, w, h], ...] 구조의 넘파이 배열을 반환합니다.
        for (x, y, w, h) in faces:
            # 얼굴 위치에 붉은색(BGR: 0, 0, 255) 사각형 그리기
            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
            # 사각형 상단에 텍스트 표기
            cv2.putText(src, "Face", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        # 5. 결과 영상 출력
        cv2.imshow('Haar Cascade Face Detection', src)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()