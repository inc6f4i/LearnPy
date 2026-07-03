import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)
print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))
while(True):
    ret, frame = cap.read() 
    if (ret):
        cp = (frame.shape[1] / 2, frame.shape[0] / 2)
        rot = cv2.getRotationMatrix2D(cp, 20, 1)
        dst = cv2.warpAffine(frame, rot, (0,0))
        cv2.imshow('rotate', dst)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break
cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기