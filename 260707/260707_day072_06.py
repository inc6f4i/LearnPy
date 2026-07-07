import cv2
import numpy as np
from matplotlib import pyplot as plt
path = 'C:/Users/user/Desktop/imaging/260707/'
img = cv2.imread(path +'/dave.png')

# Canny Edge Detection
canny = cv2.Canny(img, 30, 70) # threshold1=30, threshold2=70

# Laplacian Filter
laplacian = cv2.Laplacian(img, cv2.CV_8U)

# Sobel Filter (X축, Y축 Edge 검출)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3) # X축 미분
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3) # Y축 미분

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

for i in range(5):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], cmap='gray') # GrayScale 이미지 출력
    plt.title([titles[i]])
    plt.xticks([]), plt.yticks([])

plt.show()