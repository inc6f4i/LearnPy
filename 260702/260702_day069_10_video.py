import cv2

cap = cv2.VideoCapture(r'C:\Users\user\Desktop\crosswalk_cctv_02.mp4') # 비디오 파일 경로

while(cap.isOpened()): # 비디오 파일 열기 성공 여부 확인
    ret, frame = cap.read()

    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break # ret == False (파일 끝 or 오류)

cap.release()
cv2.destroyAllWindows()


#코드 자체는 동일한 목적을 수행하지만, 비디오가 끝나면 ret값이 false가 되어 종료
