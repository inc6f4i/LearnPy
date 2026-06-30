import cv2

# 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\a10.png')

if image is not None:
    # 크기 변경
    resized_image = cv2.resize(image, (1000, 1000),interpolation=cv2.INTER_CUBIC)
    # 자르기
    cropped_image = resized_image[10:500, 10:500]
    # 회전
    rotated_image = cv2.rotate(cropped_image, cv2.ROTATE_90_CLOCKWISE)



    # 결과 저장
    cv2.imwrite(r'C:\Users\user\Desktop\a10_resized_image.jpg', resized_image)
    cv2.imwrite(r'C:\Users\user\Desktop\a10_rotated_image.jpg', rotated_image)
    cv2.imwrite(r'C:\Users\user\Desktop\a10_cropped_image.jpg', cropped_image)
    print("Images resized, rotated, and cropped successfully")
else:
    print("Error: Could not load image.")