#260706_day071_14_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\user\Desktop\paper0.png') # 원근 효과 이미지 로드
#img = cv2.resize(img, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_CUBIC)

#rows, cols = img.shape[:2]
#img = cv2.getRotationMatrix2D((cols / 2, rows / 2), 180, 1)


# 원본 이미지 좌표 (4개의 점). 좌상 -> 좌하 -> 우상 -> 우하 순서
pts1 = np.float32([[92, 33], [21, 629], [456, 77], [521, 620]])

# 이동할 이미지 좌표 (4개의 점). pts1 좌표에 대응되는 pts2 좌표를 지정
pts2 = np.float32([[0, 0], [0, 670], [530, 0], [530, 670]])

# pts1 좌표에 원 표시 (Perspective 변환 후 이동 점 확인)
cv2.circle(img, (92, 33), 20, (255, 0, 0), -1) # Blue
cv2.circle(img, (21, 629), 20, (0, 255, 0), -1) # Green
cv2.circle(img, (456, 77), 20, (0, 0, 255), -1) # Red
cv2.circle(img, (521, 620), 20, (0, 0, 0), -1) # Black

M = cv2.getPerspectiveTransform(pts1, pts2) # Perspective 변환 행렬 생성

dst = cv2.warpPerspective(img, M, (530, 670)) # Perspective 변환 적용

plt.subplot(121), plt.imshow(img), plt.title('image') # 원본 이미지 Plot
plt.subplot(122), plt.imshow(dst), plt.title('Perspective') # Perspective 변환 이미지 Plot
plt.show()