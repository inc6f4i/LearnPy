import cv2

# 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\imaging\a7.jpg')

if image is not None:
    # 이미지 표시
    cv2.imshow('windownamein', image)
    cv2.waitKey(0) # 키 입력 대기 (0은 무한 대기)
    cv2.destroyAllWindows() # 모든 창 닫기
else:
    print("Error: Could not load image.")