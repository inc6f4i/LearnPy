import cv2

img = cv2.imread(r'C:\Users\user\Desktop\imaging\a2.gif')

rows, cols = img.shape[:2] # 이미지 높이, 너비

# Rotation 변환 행렬 생성 (이미지 중심 기준, 90도 회전, 0.5배 Scale)
#M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 0.5)
#M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1.5)
#M = cv2.getRotationMatrix2D((0,10), 45, 0.5)
dst = cv2.warpAffine(img, M, (cols, rows)) # Affine 변환 적용

cv2.imshow('Original', img)
cv2.imshow('Rotation', dst)

cv2.waitKey(0)
cv2.destroyAllWindows()



