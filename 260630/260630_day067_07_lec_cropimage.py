import cv2

# 이미지 로드
image = cv2.imread(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\image2.jpg')

if image is None: # 이미지 로드 실패 시
    print("Error: Could not read image.")
else:
    # 이미지 저장
    cv2.imwrite(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\output2.png', image)
    print("Image saved as output.png")

resized_image = cv2.resize(image, (200, 150)) # 변경할 크기 (가로, 세로)
#
if resized_image is None: # 이미지 로드 실패 시
    print("Error: Could not read resized_image.")
else:
    # 이미지 저장
    cv2.imwrite(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\output3.png', resized_image)
    print("Image saved as output.png")

#---------------------------------------------
# 이하 https://robot-python-3.netlify.app/7
#
rotated_image1 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)  # 시계 방향 90도 회전
rotated_image2 = cv2.rotate(image, cv2.ROTATE_180) # 180도 회전
rotated_image3 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE) # 반시계 방향 90도 회전

cv2.imwrite(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\output4_1.png', rotated_image1)
cv2.imwrite(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\output4_2.png', rotated_image2)
cv2.imwrite(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\output4_3.png', rotated_image3)

#---------------------------------------------
# 이하 https://robot-python-3.netlify.app/78
#
cropped_image = image[100:2000, 59:1500]  # y축 시작:끝, x축 시작:끝 
cv2.imwrite(r'D:\GoogleDrv\99_LectureData\00_incheon\code\day260630\output5_cropped.png', cropped_image)

