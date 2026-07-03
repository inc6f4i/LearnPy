import cv2, sys
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

feature = cv2.KAZE_create()


while(True):
    ret, frame = cap.read() 

    if (ret):
            
        dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kp1 = feature.detect(frame)
        
        dst2 = cv2.drawKeypoints(dst, kp1, None, flags = cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('FAST', dst2)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기