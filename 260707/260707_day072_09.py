#260707_day072_09_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

# 1단계: 이미지 로드
A = cv2.imread(r'C:\Users\user\Desktop\imaging\lena.png')# Image A (사과)
B = cv2.imread(r'C:\Users\user\Desktop\imaging\lena.png') # Image B (오렌지)

# 2단계: Gaussian Pyramid 생성 (Image A)
G = A.copy()
gpA = [G]
for i in range(6): # 6 Levels Gaussian Pyramid
    G = cv2.pyrDown(G)
    gpA.append(G)

# 2단계: Gaussian Pyramid 생성 (Image B)
G = B.copy()
gpB = [G]
for i in range(6): # 6 Levels Gaussian Pyramid
    G = cv2.pyrDown(G)
    gpB.append(G)

# 3단계: Laplacian Pyramid 생성 (Image A)
lpA = [gpA[5]] # Base Level Laplacian Pyramid = Gaussian Pyramid Level 6
for i in range(5, 0, -1): # Level 5 부터 Level 1 까지 Laplacian Pyramid 생성
    GE = cv2.pyrUp(gpA[i]) # Gaussian Pyramid Level i Upsampling
    temp = cv2.resize(gpA[i - 1], (GE.shape[1], GE.shape[0])) # Upsampling 이미지 크기를 Gaussian Pyramid Level i-1 크기로 Resize
    L = cv2.subtract(temp, GE) # Laplacian Pyramid Level i = Gaussian Pyramid Level i-1 - Upsampled Gaussian Pyramid Level i
    lpA.append(L)

# 3단계: Laplacian Pyramid 생성 (Image B)
lpB = [gpB[5]] # Base Level Laplacian Pyramid = Gaussian Pyramid Level 6
for i in range(5, 0, -1): # Level 5 부터 Level 1 까지 Laplacian Pyramid 생성
    GE = cv2.pyrUp(gpB[i]) # Gaussian Pyramid Level i Upsampling
    temp = cv2.resize(gpB[i - 1], (GE.shape[1], GE.shape[0])) # Upsampling 이미지 크기를 Gaussian Pyramid Level i-1 크기로 Resize
    L = cv2.subtract(temp, GE) # Laplacian Pyramid Level i = Gaussian Pyramid Level i-1 - Upsampled Gaussian Pyramid Level i
    lpB.append(L)

# 4단계: Laplacian Pyramid Level 별 좌우 영역 결합 (Blend)
LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:, 0:cols // 2], lb[:, cols // 2:])) # 좌측 (Image A) 영역과 우측 (Image B) 영역 결합
    LS.append(ls)

# 5단계: Laplacian Pyramid Blending 결과 재구성
ls_ = LS[0] # Base Level Blending 이미지
for i in range(1, 6): # Level 1 부터 Level 5 까지 Upsampling 및 Add 연산
    ls_ = cv2.pyrUp(ls_) # Upsampling
    temp = cv2.resize(LS[i], (ls_.shape[1], ls_.shape[0])) # Upsampling 이미지 크기를 Laplacian Pyramid Level i 크기로 Resize
    ls_ = cv2.add(ls_, temp) # Upsampling 이미지 + Laplacian Pyramid Level i (외곽선 정보)

# 원본 이미지 단순 결합 (비교용)
real = np.hstack((A[:, :cols // 2], B[:, cols // 2:]))

cv2.imshow('Real Blending', real) # 단순 결합 이미지 표시
cv2.imshow('Pyramid Blending', ls_) # Pyramid Blending 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()