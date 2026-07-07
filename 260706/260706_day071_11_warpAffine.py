#260706_day071_11_.py
import cv2
import numpy as np

img = cv2.imread(r'C:\Users\user\Desktop\imaging\output.png')

rows, cols = img.shape[:2] # 이미지 높이, 너비

# Translation 변환 행렬 생성 (X축으로 10, Y축으로 20 이동)
M = np.float32([[1, 0, 10], [0, 1, 20]])

dst = cv2.warpAffine(img, M, (cols, rows)) # Affine 변환 적용

cv2.imshow('Original', img)
cv2.imshow('Translation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()