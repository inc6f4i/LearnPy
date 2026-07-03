import cv2
import numpy as np
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, frame = cap.read() 

    if (ret):
      
    
        k = 5
        #frame1 = cv2.blur(frame, (k,k))
        frame1 = cv2.GaussianBlur(frame, (k,k), 1)
        desc = 'k = {}'.format(k)
        cv2.putText(frame1, desc, (10,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, 0, 1, cv2.LINE_AA)
        cv2.imshow('frame', frame1) 

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기