import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, frame = cap.read() 

    if (ret):
        kernel = np.ones((3,3), dtype=np.float64)/9.
        frame1 = cv2.filter2D(frame, -1, kernel)
        cv2.imshow('frame', frame1) 

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기