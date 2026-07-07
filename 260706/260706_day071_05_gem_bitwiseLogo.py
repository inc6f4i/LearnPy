"""
_, 요소를 대입연산자를 통해 나눠 넣을때 필요없는값은 _,에 대입

로고를 잘 넣어보기, 그냥 bitwise 해서 넣으면 지저분함
"""
import cv2
# 1. 이미지 읽기
img_bg = cv2.imread(r'C:\Users\user\Desktop\imaging\a7.jpg')  # 배경
img_logo = cv2.imread(r'C:\Users\user\Desktop\imaging\a2.png')      # 로고 (예: 흰 배경에 검은 로고)

# 2. ROI 설정 (좌측 상단에 배치)
rows, cols, channels = img_logo.shape
roi = img_bg[0:rows, 0:cols]

# 3. 로고 마스크 만들기
img_gray = cv2.cvtColor(img_logo, cv2.COLOR_BGR2GRAY)

# threshold를 이용해 깔끔한 이진 이미지 생성
_, mask = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask', mask)
cv2.imshow('maskinv',mask_inv)

# 4. 비트 연산을 이용한 프로세스
# 배경에서 로고 부분 구멍 뚫기
img_bg_masked = cv2.bitwise_and(roi, roi, mask=mask_inv)
cv2.imshow('drillimage',img_bg_masked)

# 로고 이미지에서 로고만 추출하기
img_logo_extracted = cv2.bitwise_and(img_logo, img_logo, mask=mask)

# 5. 두 이미지를 더해서 완전한 합성 만들기
dst = cv2.add(img_bg_masked, img_logo_extracted)
dst = cv2.addWeighted(img_bg_masked, 1.0, img_logo_extracted, 1.2, 0)

#mask = 255 * np.ones(img_logo.shape, img_logo.dtype)
#dst = cv2.seamlessClone(img_logo, img_bg, mask, center, cv2.MIXED_CLONE)
# 6. 원본 배경에 합성 완료된 ROI 덮어쓰기
#img_bg[0:rows, 0:cols] = dst

cv2.imshow('Clean Synthesis', img_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()