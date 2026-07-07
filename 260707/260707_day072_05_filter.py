#11.6 샘플 코드 Bilateral Filtering(양방향필터) \
import cv2
import numpy as np
#img1 = cv2.imread('D:/GoogleDrv/99_LectureData/00_incheon/code/day072/images/logo.png') # OpenCV 로고 이미지
from matplotlib import pyplot as plt
#
dotImage = cv2.imread('D:/GoogleDrv/99_LectureData/00_incheon/code/day260707/images/dot_image.png', cv2.IMREAD_GRAYSCALE) # 점 노이즈 이미지 (GrayScale)
holeImage = cv2.imread('D:/GoogleDrv/99_LectureData/00_incheon/code/day260707/images/hole_image.png', cv2.IMREAD_GRAYSCALE) # 구멍 노이즈 이미지 (GrayScale)
orig = cv2.imread('D:/GoogleDrv/99_LectureData/00_incheon/code/day260707/images/morph_origin.png', cv2.IMREAD_GRAYSCALE) # 원본 이미지 (GrayScale)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # 5x5 사각형 Kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) # 5x5 타원형 Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) # 5x5 십자형 Kernel

# Erosion 연산 (점 노이즈 제거)
erosion = cv2.erode(dotImage, kernel, iterations=1)

# Dilation 연산 (구멍 노이즈 채우기)
dilation = cv2.dilate(holeImage, kernel, iterations=1)

# Opening 연산 (점 노이즈 제거)
opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)

# Closing 연산 (구멍 노이즈 채우기)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient (경계선 추출)
gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel)

# Top Hat (원본 - Opening, 작은 객체/돌기 추출)
tophat = cv2.morphologyEx(orig, cv2.MORPH_TOPHAT, kernel)

# Black Hat (Closing - 원본, 작은 구멍 추출)
blackhat = cv2.morphologyEx(orig, cv2.MORPH_BLACKHAT, kernel)

images = [dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat]
titles = ['Dot Image', 'Erosion', 'Opening', 'Hole Image', 'Dilation', 'Closing', 'Gradient', 'Tophat', 'Blackhot']

for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()