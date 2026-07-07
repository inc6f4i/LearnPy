"""
cv2.threshold
"""
#260706_day071_07_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\user\Desktop\imaging\a12.png', 0) # GrayScale 이미지 로드

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY) # BINARY Thresholding
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) # BINARY_INV Thresholding
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC) # TRUNC Thresholding
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO) # TOZERO Thresholding
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV) # TOZERO_INV Thresholding 
"""
메서드 마지막 상수에 의해서 각각 조금씩 다른 결과물이 출력
경계선 인식
"""

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in range(6):
    plt.subplot(1, 6, i + 1), plt.imshow(images[i], 'gray') # 결과 이미지 Plot
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([]) # X, Y 축 눈금 제거

plt.show()
"""
여러개의 이미지를 한 화면에 표시하기 위해 subplot() 함수 사용
matplotlib 안에 있음

"""