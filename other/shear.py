import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, frame = cap.read() 

    if (ret):
        aff=np.array([[1,0.5,0],[0,1,0]], dtype=np.float32)
        h,w = frame.shape[:2]
        dst = cv2.warpAffine(frame,aff,(w+int(h*0.5),h))

        cv2.imshow('SHEAR', dst)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기