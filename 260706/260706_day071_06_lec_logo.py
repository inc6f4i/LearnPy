"""
주요학습내용
임계값 처리함수 컬러 이미지를 흑백으로 변경할때
임계값보다 낮으면 0 크면 255

2진 연산함수로 로고부분 제거
"""


import cv2
import numpy as np

img1 = cv2.imread('images/logo.png') # OpenCV 로고 이미지
img2 = cv2.imread('images/lena.jpg') # 배경 이미지

rows, cols, _, = img1.shape # 로고 이미지 Shape 세로가로컬러

roi = img2[0:rows, 0:cols] # 배경 이미지에서 로고 이미지 영역 추출 (ROI)

# 로고 이미지를 GrayScale로 변환 후 Binary 이미지로 변환 (Mask 생성)
img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # Thresholding (Binary Mask)
"""
임계값 처리함수 컬러 이미지를 흑백으로 변경할때
임계값보다 낮으면 0 크면 255
"""
mask_inv = cv2.bitwise_not(mask) # Mask 반전 (Inverse Mask)

# Bitwise AND 연산: Mask를 이용하여 로고 이미지에서 전경 (Logo) 추출
img1_fg = cv2.bitwise_and(img1, img1, mask=mask)

# Bitwise AND 연산: 반전된 Mask를 이용하여 ROI 영역에서 배경 추출
img2_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
"""
2진 연산함수
"""
# 전경 (Logo) 와 배경 이미지 합성
dst = cv2.add(img1_fg, img2_bg)

img2[0:rows, 0:cols] = dst # 합성된 이미지를 원본 배경 이미지에 적용

cv2.imshow('res', img2) # 최종 결과 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()