import cv2
import numpy as np

# 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\imaging\image.jpg')
if image is not None:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)### 매우중요

    # 가우시안 블러링 
    blurred_image = cv2.GaussianBlur(image, (7, 7), 0) ### 얘는 그냥 이미지

    # 샤프닝
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) ### 얘도 그냥이미지
    sharpened_image = cv2.filter2D(image, -1, kernel)

    # 소벨 필터
    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=2) ### 소벨필터는 그레이스케일 한놈
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=2)

    # 캐니 엣지 검출
    edges = cv2.Canny(gray_image, 300, 350)        ### 엣지검출도 그레이스케일한놈, 컬러는 못잡아냄

    # 결과 저장
    cv2.imwrite('blurred_image.jpg', blurred_image)
    cv2.imwrite('sharpened_image.jpg', sharpened_image)
    cv2.imwrite('sobelx.jpg', sobelx)
    cv2.imwrite('sobely.jpg', sobely)
    cv2.imwrite('edges.jpg', edges)
    print("Images filtered successfully")
else:
    print("Error: Could not load image.")