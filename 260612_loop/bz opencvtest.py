import cv2
import numpy as np
import pytesseract

def imread_korean(path):
    img_array = np.fromfile(path, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
    return img

img_path = r'C:\Users\user\Desktop\2026-06-04 140417.png'
img = imread_korean(img_path)
cropped_img = img[100:500, 200:600]
gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
_, binary_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
# 3. 화면에 띄우기 세트
cv2.imshow('Hangul Path Test', img)
cv2.imshow('Binarized Image', binary_img)

text = pytesseract.binary_img_to_string(binary_img, lang='kor+eng')


print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()