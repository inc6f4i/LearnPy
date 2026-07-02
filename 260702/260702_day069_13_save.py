import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 카메라 장치 0번

# 코덱 설정 (DIVX)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

# VideoWriter 객체 생성 (output.avi 파일, DIVX 코덱, 25 FPS, 640x480 사이즈)
out = cv2.VideoWriter(r'C:\Users\user\Desktop\imaging\output.avi', fourcc, 25.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        frame = cv2.flip(frame, 0) # 이미지 상하 반전 (0: 상하, 1: 좌우)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray, (5, 5), 0)
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened_image = cv2.filter2D(blurred_image, -1, kernel)
        edges = cv2.Canny(sharpened_image, 100, 200)
        edges = cv2.circle(edges,(320,240),100,255,-1)
        edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        out.write(edges) # 프레임 저장

        cv2.imshow('frame', edges) #

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
out.release() # VideoWriter 객체 해제
cv2.destroyAllWindows()


#익스펙티드 3채널 벗 1채널, 이거 그레이스케일이라 채널없는상태에서 BGR로 바꿔주면 3채널이라 됨