import cv2
import pytesseract
#import numpy as np


image = cv2.imread(r'C:\Users\user\Desktop\Screenshot_20260609_015116_O.jpg')

crop = image[766:800, 300:450]
#kernel = np.array([[0, -1, 0],  [-1, 5, -1], [0, -1, 0]])
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#resized = cv2.resize(gray, None, fx=1.4, fy=1.4, interpolation=cv2.INTER_CUBIC)
#blurred = cv2.GaussianBlur(resized, (3, 3), 0)
#sharpened = cv2.filter2D(blurred, -1, kernel)
#_, thresh = cv2.threshold(image, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--psm 4'

text = pytesseract.image_to_string(crop, lang='kor+eng', config=custom_config)


cv2.imshow('입력된이미지', image)
#cv2.imshow('Binarized Image', thresh)
cv2.imshow('크롭', crop)

print("OCR 결과:")
print(text)


cv2.waitKey(0)
cv2.destroyAllWindows()