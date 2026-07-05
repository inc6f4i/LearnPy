import cv2
import sys
import numpy as np

def on_trackbar(x):
    pass

# 카메라 열기
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
    sys.exit()

# 윈도우 생성 및 트랙바 등록
cv2.namedWindow('Binary Image')
cv2.createTrackbar('Threshold', 'Binary Image', 150, 255, on_trackbar)

while True:
    ret, src = cap.read() 
    if not ret:
        break

    # 1. 그레이스케일 변환
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    # 2. 현재 트랙바 임계값 가져오기 및 이진화
    pos = cv2.getTrackbarPos('Threshold', 'Binary Image')
    _, binary = cv2.threshold(gray, pos, 255, cv2.THRESH_BINARY)

    # 3. OpenCV를 이용한 실시간 히스토그램 계산
    # cv2.calcHist([이미지], [채널], 마스크, [빈(Bin)개수], [정규화범위])
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    
    # 4. 히스토그램을 그릴 빈 이미지(스케치북) 생성 (가로 256, 세로 200, 3채널 컬러)
    hist_img = np.zeros((200, 256, 3), dtype=np.uint8)
    
    # 그래프가 창에 꽉 차게 그리도록 정규화 (최대 높이를 190으로 맞춤)
    cv2.normalize(hist, hist, 0, 190, cv2.NORM_MINMAX)

    # 5. 히스토그램 선 그리기 (하얀색 선)
    for i in range(1, 256):
        pt1 = (i - 1, 200 - int(hist[i - 1][0]))
        pt2 = (i, 200 - int(hist[i][0]))
        cv2.line(hist_img, pt1, pt2, (255, 255, 255), 1)
        

    # 6. 현재 트랙바 위치(임계값)를 히스토그램에 빨간 세로선으로 표시
    # 이 선을 기준으로 왼쪽은 검은색(0), 오른쪽은 흰색(255)이 됩니다.
    cv2.line(hist_img, (pos, 0), (pos, 200), (0, 0, 255), 2)
    cv2.putText(hist_img,f'{pos}',(10,30),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0))
    # 7. 화면 출력
    cv2.imshow('Original Gray', gray)
    cv2.imshow('Binary Image', binary)
    cv2.imshow('Real-time Histogram', hist_img)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()