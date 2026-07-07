import cv2

img = cv2.imread(r'C:\Users\user\Desktop\imaging\lena.png')

GAD = cv2.pyrDown(img) # Gaussian Pyramid Downsampling
GAU = cv2.pyrUp(GAD) # Gaussian Pyramid Upsampling

temp = cv2.resize(GAU, (img.shape[1], img.shape[0])) # Upsampled 이미지 크기를 원본 이미지 크기로 Resize
res = cv2.subtract(img, temp) # 원본 이미지 - Upsampled 이미지 (Laplacian Pyramid Level)

cv2.imshow('Laplacian Pyramid', res) # Laplacian Pyramid Level 이미지 표시
cv2.waitKey(0)
cv2.destroyAllWindows()