#260706_day071_08_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\user\Desktop\imaging/dave.png', 0) # GrayScale 이미지 로드
img = cv2.medianBlur(img, 5) # Median Filter (노이즈 제거, Optional)

ret, th1 = cv2.threshold(img, 66, 255, cv2.THRESH_BINARY) # Global Thresholding (기본 임계처리)
"""
평범한 이진화
"""
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,

                            cv2.THRESH_BINARY, 15, 2) # Mean Adaptive Thresholding
"""
민
"""

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, 33, 2) # Gaussian Adaptive Thresholding
"""
가우시안
"""
titles = ['Original', 'Global', 'Mean', 'Gaussian']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()