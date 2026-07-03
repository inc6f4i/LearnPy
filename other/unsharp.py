import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, frame = cap.read() 

    if (ret):
        blur = cv2.GaussianBlur(frame, (5, 5), 0)
        sharp = cv2.addWeighted(frame, 1.5, blur, -0.5, 0)
        cv2.imshow('frame', sharp) 

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기