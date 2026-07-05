import cv2
import numpy as np

# 1. HOG 기술자 설정 및 사전 학습된 보행자 검출기 로드
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# 웹캠 열기
cap = cv2.VideoCapture(0)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read()

    if (ret):
        # 2. HOG 검출 속도 향상을 위해 이미지 크기를 약간 줄이는 것이 좋습니다 (선택사항)
        # 웹캠 해상도가 너무 높으면 실시간 연산이 밀릴 수 있습니다.
        # h, w = src.shape[:2]
        # src_resized = cv2.resize(src, (640, int(h * (640 / w))))
        
        # 3. 멀티스케일 보행자 검출 실행
        # winStride: 윈도우가 이미지를 훑으며 이동하는 보폭 (x, y)입니다. 작을수록 정밀하지만 느려집니다.
        # padding: 이미지 경계면 주변의 패딩 크기입니다.
        # scale: 이미지 피라미드 축소 비율입니다. (값이 작을수록 촘촘하게 검출하여 정확도가 높아지나 느려짐)
        # finalThreshold: 겹치는 검출 사각형들을 합치기 위한 임계값입니다.
        found, weights = hog.detectMultiScale(src, winStride=(8, 8), padding=(32, 32), scale=1.05)# finalThreshold=2.0
        
        # 4. 검출된 보행자 영역에 사각형 그리기
        # found에는 [[x, y, w, h], ...] 형태로 사각형 좌표들이 들어있습니다.
        for (x, y, w, h) in found:
            # 보행자 위치에 주황색(BGR: 0, 128, 255) 사각형 그리기
            cv2.rectangle(src, (x, y), (x + w, y + h), (0, 128, 255), 2)
            
            # 사각형 상단에 텍스트 표기
            cv2.putText(src, "Person", (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 128, 255), 2)

        # 5. 결과 영상 출력
        cv2.imshow('HOG Pedestrian Detection', src)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()