import cv2
import numpy as np

# 1. 비디오 캡처 객체 생성
#cap = cv2.VideoCapture(0)  # VideoCapture에 IMREAD_GRAYSCALE은 올바른 인자가 아닙니다.
cap = cv2.VideoCapture(r'C:\Users\user\Desktop\imaging\260707\highway.mp4')
# 트래커 초기화 (원하는 트래커 주석을 해제하여 사용하세요)
tracker = cv2.TrackerKCF_create()
#tracker = cv2.TrackerCSRT_create()  # 정확도가 높아 보통 추천됩니다
#tracker = cv2.TrackerMIL_create() # 이중하나쓰거나 둘다쓰거나

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

# 첫 프레임을 읽어와 ROI(관심영역) 설정 및 트래커 초기화 진행
ret, frame = cap.read()
if ret:
    # 윈도우 창 이름, 이미지, 격자 표시 여부, 시작점 중심 여부
    bbox = cv2.selectROI('Select ROI', frame, False, False)
    cv2.destroyWindow('Select ROI')
    
    # 트래커에 첫 프레임과 설정한 bbox(상자)를 입력하여 초기화 중요함
    tracker.init(frame, bbox) # 초기화하기

while True:
    ret, src = cap.read() 

    if ret:
        # 2. 트래커 업데이트 (새로운 프레임에서 객체 위치 추적)
        success, bbox = tracker.update(src)
        
        # dst 변수를 사용하기 위해 복사본 생성 (또는 src에 직접 그려도 됨)
        dst = src.copy()

        if success:
            # 추적 성공 시 객체 위치 추출 (x, y, w, h)
            x, y, w, h = map(int, bbox)
            
            # 3. 바운딩 박스 사각형 그리기
            cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # 4. 'test' 텍스트 표시하기
            cv2.putText(dst, 'test', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            # 추적 실패 시 표시
            cv2.putText(dst, "Tracking Failure", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            #여기다가 재탐색 로직같은거 넣으면
        # 결과 화면 출력
        cv2.imshow('Tracking', dst)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # 캡처 객체를 반환한다는 뜻임
cv2.destroyAllWindows()