#260706_day071_09_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\user\Desktop\imaging\xas1.png', 0) # 노이즈 이미지 로드

# Global Thresholding (임계값: 127)
ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Otsu's Thresholding
ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Gaussian Blur + Otsu's Thresholding (노이즈 제거 후 Otsu 적용)
blur = cv2.GaussianBlur(img, (5, 5), 0) # Gaussian Blur
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Otsu's Thresholding

# Plot images and histograms
images = [img, 0, th1, img, 0, th2, blur, 0, th3]
titles = ['Original Noisy Image', 'Histogram', 'Global Thresholding (v=127)',
          'Original Noisy Image', 'Histogram', "Otsu's Thresholding",
          'Gaussian filtered Image', 'Histogram', "Otsu's Thresholding"]

for i in range(3):
    plt.subplot(3, 3, i * 3 + 1), plt.imshow(images[i * 3], 'gray') # 원본 이미지 Plot
    plt.title(titles[i * 3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 2), plt.hist(images[i * 3].ravel(), 256) # 히스토그램 Plot
    plt.title(titles[i * 3 + 1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3, 3, i * 3 + 3), plt.imshow(images[i * 3 + 2], 'gray') # 임계처리 결과 이미지 Plot
    plt.title(titles[i * 3 + 2]), plt.xticks([]), plt.yticks([])

plt.show()