import cv2
import numpy as np

# 1. 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\Screenshot_20260609_015116_O.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 2. 색상별 고유 영역(Mask) 범위 지정 (실제 기기 아이콘 색상 기준)
# 빨간색 (고장)
lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 100, 100])
upper_red2 = np.array([180, 255, 255])

# 노란색 (방전)
lower_yellow = np.array([15, 100, 100])
upper_yellow = np.array([35, 255, 255])

# 하늘색 (정비대상)
lower_sky = np.array([85, 100, 100])
upper_sky = np.array([105, 255, 255])

# 3. 마스크 생성 및 픽셀 수 카운트
mask_red = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_sky = cv2.inRange(hsv, lower_sky, upper_sky)

# 각각의 색상이 차지하는 픽셀 개수 뽑기
red_pixels = cv2.countNonZero(mask_red)
yellow_pixels = cv2.countNonZero(mask_yellow)
sky_pixels = cv2.countNonZero(mask_sky)

total_pixels = image.shape[0] * image.shape[1]
print(f"🔴 고장(빨강): {red_pixels/total_pixels*100:.2f}%")
print(f"🟡 방전(노랑): {yellow_pixels/total_pixels*100:.2f}%")
print(f"🔵 정비(하늘): {sky_pixels/total_pixels*100:.2f}%")