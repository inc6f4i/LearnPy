#이진화 진행전 적절한 경계, 임계값을 찾기 위해선 히스토 그램 분석이 필수!
import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

pos = 150
    
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)
print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))
while(True):
    ret, src = cap.read() 

    if (ret):
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        rgb = cv2.cvtColor(gray , cv2.COLOR_GRAY2RGB)
        

        _, bin = cv2.threshold(gray, pos, 255, cv2.THRESH_BINARY)
        cv2.imshow('binary', bin)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기