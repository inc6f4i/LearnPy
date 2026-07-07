#260706_day071_01_.py
import cv2
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

while(True):
    ret, src = cap.read() 

    if (ret):
        
        #b, g, r = cv2.split(src)
        #dst = cv2.merge((b,g,r))
        b = src[:, :, 0] # Blue 채널 접근 ndarray start,ndarray end, channel
        g = src[:, :, 1] # Green 채널 접근
        r = src[:, :, 2] # Red 채널 접근

        cv2.imshow('1', b)
        cv2.imshow('2', g)
        cv2.imshow('3', r)
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() 
cv2.destroyAllWindows()