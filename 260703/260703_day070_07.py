#260703_day070_07_.py
import cv2
import numpy as np

drawing = False # Mouse 클릭 상태 (False: 떼어진 상태, True: 눌린 상태)
mode = True # 도형 모드 (True: 사각형, False: 원)
ix, iy = -1, -1 # 시작점 좌표 초기화

# Mouse Callback 함수
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN: # Left Button Down Event
        drawing = True # 클릭 상태로 변경
        ix, iy = x, y # 시작점 좌표 저장

    elif event == cv2.EVENT_MOUSEMOVE: # Mouse Move Event
        if drawing == True: # 클릭 상태인 경우
            if mode == True: # 사각형 모드
                cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1) # 사각형 그리기
            else: # 원 모드
                cv2.circle(img, (ix, iy), 25, (0, 255, 0), -1) # 원 그리기

    elif event == cv2.EVENT_LBUTTONUP: # Left Button Up Event
        drawing = False # 떼어진 상태로 변경
        if mode == True: # 사각형 모드
            cv2.rectangle(img, (ix, iy), (x, y), (255, 0, 0), -1) # 최종 사각형 그리기
        else: # 원 모드
            cv2.circle(img, (ix, iy), 25, (0, 255, 0), -1) # 최종 원 그리기

img = np.zeros((512, 512, 3), np.uint8) # 검정색 배경 이미지 생성
cv2.namedWindow('image') # 윈도우 창 생성
cv2.setMouseCallback('image', draw_circle) # Mouse Callback 함수 등록

while True:
    cv2.imshow('image', img) # 이미지 표시
    k = cv2.waitKey(1) & 0xFF # 키 입력 대기

    if k == ord('m'): # 'm' 키 입력 시 도형 모드 변경 (사각형 <-> 원)
        mode = not mode
    elif k == 27: # ESC 키 입력 시 종료
        break

cv2.destroyAllWindows()