import cv2
import numpy as np
import math
x = 45
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

rad = x * math.pi /180
aff = np.array([[math.cos(rad),math.sin(rad), 0],[-math.sin(rad), math.cos(rad), 0]], dtype=np.float32)


while(True):
    ret, frame = cap.read() 

    if (ret):
        dst = cv2.warpAffine(frame, aff, (0,0))

        cv2.imshow('rotate', dst)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기