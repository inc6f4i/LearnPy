import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\user\Desktop\imaging\chess.png') # Chessboard 이미지 로드
rows, cols, ch = img.shape # 이미지 Shape

# 원본 이미지 좌표 (3개의 점)
pts1 = np.float32([[200, 100], [400, 100], [200, 200]])

# 이동할 이미지 좌표 (3개의 점). pts1 좌표에 대응되는 pts2 좌표를 지정
pts2 = np.float32([[200, 300], [400, 200], [200, 400]])

# pts1 좌표에 원 표시 (Affine 변환 후 이동 점 확인)
cv2.circle(img, (200, 100), 10, (255, 0, 0), -1) # Blue
cv2.circle(img, (400, 100), 10, (0, 255, 0), -1) # Green
cv2.circle(img, (200, 200), 10, (0, 0, 255), -1) # Red

M = cv2.getAffineTransform(pts1, pts2) # Affine 변환 행렬 생성

dst = cv2.warpAffine(img, M, (cols, rows)) # Affine 변환 적용

cv2.imshow('src', img)
cv2.imshow('aff', dst)

cv2.waitKey(0)
cv2.destroyAllWindows

#plt.subplot(121), plt.imshow(img), plt.title('image') # 원본 이미지 Plot
#plt.subplot(122), plt.imshow(dst), plt.title('Affine') # Affine 변환 이미지 Plot
#plt.show()