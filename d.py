import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap2 = cv2.VideoCapture(1, cv2.CAP_DSHOW)
#cap.set(3,320)
#cap.set(4,240)

while(True):
    ret, frame = cap.read()
    ret2, frame2 = cap2.read()
    if (ret):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        g1 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        #dst = cv2.subtract(gray, g1)
        dst = cv2.absdiff(gray, g1)
        cv2.imshow('f', dst)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else :
        break