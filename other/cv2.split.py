import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 카메라 장치 0번, 보통 숫자로

# 카메라 속성 확인 (width, height)
print('width: {0}, height: {1}'.format(cap.get(3), cap.get(4)))

# 카메라 속성 변경 (width, height 설정)
cap.set(3, 320) # width
cap.set(4, 240) # height

while(True):
    ret, frame = cap.read() # 프레임 읽기

    if (ret):
        b, g, r = cv2.split(frame) # BGR 채널 분리
        m_b = cv2.merge([b, b, b])
        m_g = cv2.merge([g, g, g])
        m_r = cv2.merge([r, r, r])
        cv2.imshow('frame1', m_b) # Red 채널 표시
        cv2.imshow('frame2', m_g) # Green 채널 표시
        cv2.imshow('frame3bluelightlenz', m_r) # Blue 채널 표시

        if cv2.waitKey(1) & 0xFF == ord('q'): # 'q' 키 입력 시 종료
            break
    else:
        break#카메라가 없으니 ret에서 0을 안줘서 True가 계속되나?

cap.release() # VideoCapture 객체 해제
cv2.destroyAllWindows() # 윈도우 창 닫기



#