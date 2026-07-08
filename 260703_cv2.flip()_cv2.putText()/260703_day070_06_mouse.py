#260703_day070_06_.py
import cv2
import numpy as np

img = np.zeros((640, 640, 3), dtype=np.uint8)
img.fill(0) # 흰 배경

def draw_circle(event, x, y, flags, param):
    # event: 발생한 Mouse Event 종류 (예: cv2.EVENT_LBUTTONDOWN)
    # x, y: Mouse Cursor 좌표
    # flags: Mouse Event 발생 시 눌러진 키 (Ctrl, Shift, Alt, 마우스 버튼 등)
    # param: cv2.setMouseCallback() 함수에서 전달된 param 값
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (0, 0, 255), -1) # Double Click 시 원 그리기
cv2.namedWindow("korean")
cv2.setMouseCallback("korean", draw_circle)
while(1):
    cv2.imshow("korean", img)
    if cv2.waitKey(20) & 0xFF == 27: # ESC 키 입력 시 종료
        break
cv2.waitKey(0)
cv2.destroyAllWindows() 
