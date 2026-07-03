import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, frame = cap.read() 

    if (ret):
        dst1 = cv2.resize(frame, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
        dst2 = cv2.resize(frame, (3840,2160))
        dst3 = cv2.resize(frame, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        dst4 = cv2.resize(frame, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_LANCZOS4)

        cv2.imshow('NEAREST', dst1)
        cv2.imshow('noInterpol', dst2)
        cv2.imshow('44', dst3)
        cv2.imshow('88', dst4)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기