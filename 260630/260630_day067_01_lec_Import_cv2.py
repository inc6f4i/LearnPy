#260630_day067_01_.py
import cv2 
import numpy as np
import pytesseract

class chek:
    def ck(self,a):
        self.c = a
        cv2.imshow('n', self.c)
        cv2.waitKey(0)
        cv2.destroyAllWindows()    

print(pytesseract.__version__)
print(cv2.__version__)
b = chek()
rawImg = cv2.imread(r'E:\code\learnPy\260630\a8.jpg')
b.ck(rawImg)
cropImg = rawImg[333:978, 18:1686]
b.ck(cropImg)
sizeup = cv2.resize(cropImg, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)
b.ck(sizeup)
hsv = cv2.cvtColor(sizeup, cv2.COLOR_BGR2HSV)
b.ck(hsv)
mask = cv2.inRange(hsv, (245, 245, 245), (245, 245, 245))   #(0, 0, 175), (179 , 80, 255)
b.ck(mask)
###########################
num, labels, stats, _ = cv2.connectedComponentsWithStats(mask, 8)
clean = np.zeros_like(mask)
h, w = mask.shape
b.ck(clean)
#for i in range(1, num):
#    x, y, bw, bh, area = stats[i]
#
#    # 글자라고 보기엔 너무 큰 영역 제거
#    if area > w * h * 0.015:
#        continue
#
#    # 너무 작은 노이즈 제거
#    if area < 20:
#        continue
#
#    clean[labels == i] = 255

## 4. 글자 획 보정
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
clean = cv2.morphologyEx(hsv, cv2.MORPH_CLOSE, kernel, iterations=1)
clean = cv2.dilate(clean, kernel, iterations=1)
b.ck(clean)
ocr_img1 = cv2.bitwise_not(clean)
b.ck(ocr_img1)

padding = 20
ocr_img = cv2.copyMakeBorder(
    ocr_img1, 
    padding, padding, padding, padding, 
    cv2.BORDER_CONSTANT, 
    value=[0, 0, 0]
)
b.ck(ocr_img)
##
#kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
#mask1 = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)
#cv2.imshow('n', mask1)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
#ocr_img = cv2.bitwise_not(mask1)



cv2.imwrite(r'E:\code\learnPy\260630\a7_orc_img.jpg', ocr_img)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
custom_config = r'--psm 6'

text = pytesseract.image_to_string(ocr_img, lang='kor+eng', config=custom_config)

print(text)
#cv2.imshow()
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite(r'E:\code\learnPy\260630\output_260630a7_cropped.jpg',cropImg)

