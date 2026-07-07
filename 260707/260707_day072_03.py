#260707_day072_03_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x): # Trackbar Callback 함수 (empty function)
    pass


img = cv2.imread(r'C:\Users\user\Desktop\imaging\lena.png')

# Matplotlib 출력을 위해 BGR -> RGB 변환
b, g, r = cv2.split(img)
img_rgb = cv2.merge([r, g, b])

# Averaging Blur (평균 필터)
dst1 = cv2.blur(img_rgb, (7, 7)) # 7x7 Kernel

# Gaussian Blur (가우시안 필터)
dst2 = cv2.GaussianBlur(img_rgb, (3, 3), 0) # 5x5 Kernel, sigmaX = 0 (자동 계산)

# Median Blur (미디언 필터)
dst3 = cv2.medianBlur(img_rgb, 9) # 9x9 Kernel

# Bilateral Filtering (양방향 필터)
dst4 = cv2.bilateralFilter(img_rgb, 9, 75, 75) # d=9, sigmaColor=75, sigmaSpace=75

images = [img_rgb, dst1, dst2, dst3, dst4]
titles = ['Original', 'Blur(7x7)', 'Gaussian Blur(5x5)', 'Median Blur', 'Bilateral']

for i in range(5):
    plt.subplot(3, 2, i + 1), plt.imshow(images[i]), plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()