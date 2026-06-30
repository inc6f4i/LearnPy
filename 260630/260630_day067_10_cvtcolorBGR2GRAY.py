import cv2

# 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\imaging\a11.jpg')
if image is not None:
    # BGR -> Gray
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Gray -> BGR
    rgb_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR)

    # 결과 저장
    cv2.imwrite(r'C:\Users\user\Desktop\imaging\a11_g.jpg', gray_image)
    cv2.imwrite(r'C:\Users\user\Desktop\imaging\a11_g2r.jpg', rgb_image)
    print("Images converted successfully")
else:
    print("Error: Could not load image.")