#260707_day072_04_.py
import cv2
import numpy as np
from matplotlib import pyplot as plt

from skimage.metrics import structural_similarity as ssim



path = 'C:/Users/user/Desktop/imaging/260707/'
dotImage = cv2.imread(path +'/dot_image.png', cv2.IMREAD_GRAYSCALE) # 점 노이즈 이미지 (GrayScale)
holeImage = cv2.imread(path +'hole_image.png', cv2.IMREAD_GRAYSCALE) # 구멍 노이즈 이미지 (GrayScale)
orig = cv2.imread(path + 'morph_origin.png', cv2.IMREAD_GRAYSCALE) # 원본 이미지 (GrayScale)

#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # 5x5 사각형 Kernel
#kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)) # 5x5 타원형 Kernel
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5)) # 5x5 십자형 Kernel




# Erosion 연산 (점 노이즈 제거)
erosion = cv2.erode(dotImage, kernel, iterations=1)

# Dilation 연산 (구멍 노이즈 채우기)
dilation = cv2.dilate(holeImage, kernel, iterations=1)

# Opening 연산 (점 노이즈 제거)
opening = cv2.morphologyEx(dotImage, cv2.MORPH_OPEN, kernel)

# Closing 연산 (구멍 노이즈 채우기)
closing = cv2.morphologyEx(holeImage, cv2.MORPH_CLOSE, kernel)

# Morphological Gradient (경계선 추출)
gradient = cv2.morphologyEx(orig, cv2.MORPH_GRADIENT, kernel)

# Top Hat (원본 - Opening, 작은 객체/돌기 추출)
tophat = cv2.morphologyEx(orig, cv2.MORPH_TOPHAT, kernel)

# Black Hat (Closing - 원본, 작은 구멍 추출)
blackhat = cv2.morphologyEx(orig, cv2.MORPH_BLACKHAT, kernel)

images = [dotImage, erosion, opening, holeImage, dilation, closing, gradient, tophat, blackhat, orig]
titles = ['Dot Image', 'Erosion\ncv2.erode', 'Opening\ncv2.MORPH_OPEN', 'Hole Image', 'Dilation\ncv2.dilate', 'Closing\ncv2.MORPH_CLOSE', 'Gradient\ncv2.MORPH_GRADIENT', 'Tophat\ncv2.MORPH_TOPHAT',
           'Blackhat\ncv2.MORPH_BLACKHAT', 'origin']
######################################################################
a = cv2.matchTemplate(dilation, orig, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(a)

print('min_val, max_val, min_loc, max_loc\n',min_val, max_val, min_loc, max_loc)

#########################################
orig = cv2.resize(orig, (dilation.shape[1], dilation.shape[0]))
score, diff = ssim(orig, dilation, full=True)
print(f"SSIM 유사도 점수: {score}")
print("orig:", orig.shape)
print("dilation:", dilation.shape)

# 두 이미지가 0과 255로 이루어진 이진 이미지일 때
intersection = np.logical_and(orig, dilation).sum()
union = np.logical_or(orig, dilation).sum()
iou = intersection / union
print(f"교집합 비율(IoU): {iou}")




fig, axes = plt.subplots(4, 3, figsize=(12, 9))
axes = axes.flatten()
for i in range(10):
    plt.subplot(4, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

for i in range(10, 12):
    axes[i].axis("off")

plt.tight_layout()
plt.show()