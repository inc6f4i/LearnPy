import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, frame = cap.read() 

    if (ret):
        blur = cv2.GaussianBlur(frame, (5, 5), 0)
        sharp = cv2.addWeighted(frame, 1.5, blur, -0.5, 0)
        filter = cv2.bilateralFilter(sharp, -1 ,10, 5)
        mid = cv2.medianBlur(frame, 5) 
        cv2.imshow('mi',mid)
        cv2.imshow('fil', filter) 
        cv2.imshow('sh', sharp)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기


#털같은게 많이 지워짐