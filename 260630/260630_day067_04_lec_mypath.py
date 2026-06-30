import cv2

# 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\a9.jpg')

if image is None: # 이미지 로드 실패 시
    print("Error: Could not read image.")
else:
    # 이미지 저장
    cv2.imwrite(r'DC:\Users\user\Desktop\a9.jpg', image)
    print("Image saved as output.png")

resized_image = cv2.resize(image, (200, 150)) # 변경할 크기 (가로, 세로)
#
if resized_image is None: # 이미지 로드 실패 시
    print("Error: Could not read resized_image.")
else:
    # 이미지 저장
    cv2.imwrite(r'C:\Users\user\Desktop\o_a9.jpg', resized_image)
    print("Image saved as output.png")

rotated_img1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
rotated_img2 = cv2.rotate(image, cv2.ROTATE_180)
rotated_img3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
if all(img is None for img in[rotated_img1, rotated_img2, rotated_img3]):
    print("없어")
    exit()
else:
    cv2.imwrite(r'C:\Users\user\Desktop\o_a9_90c.jpg', rotated_img1)
    cv2.imwrite(r'C:\Users\user\Desktop\o_a9_180.jpg', rotated_img2)
    cv2.imwrite(r'C:\Users\user\Desktop\o_a9_90cc.jpg', rotated_img3)
    print('저장됨')