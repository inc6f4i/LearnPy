import cv2, sys
import numpy as np
cap = cv2.VideoCapture(0, cv2.IMREAD_GRAYSCALE)

print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))



while(True):
    ret, frame = cap.read() 

    if (ret):
        fast = cv2.FastFeatureDetector_create(60) #VS Code의 Pylance 같은 도구는 cv2 모듈 내부의 구조를 완벽하게 분석하지 못할 때가 잦습니다.
        keypoints = fast.detect(frame)
        dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dst1 = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)
        for kp in keypoints:
            pt = (int(kp.pt[0]),int(kp.pt[1]))
            cv2.circle(dst1, pt, 5, (0, 0, 255),2)
        cv2.imshow('FAST', dst1)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    else:
        break

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기