#260702_day069_06_.py

import cv2
import os


path = os.getcwd()
file_path = os.path.abspath(__file__)
print('path-->', path)
print('file_path-->', file_path)
dir_path = os.path.dirname(os.path.abspath(__file__)) ##이라인이 중요
print('dir_path-->', dir_path)

img0 = cv2.imread(dir_path + r'\lena.png', 1) #이 프로그램의 위치
img1 = cv2.imread(dir_path + r'\lena.png', 0)
img2 = cv2.imread(dir_path + r'\lena.png', -1)

cv2.imshow('color', img0)
cv2.imshow('gray', img1)    
cv2.imshow('unchanged', img2)
cv2.waitKey(3000) #3000ms 3초 동안만 보여주고 자동으로 닫힘
cv2.destroyAllWindows()

print(type(img0), img0.shape)
print(type(img1), img1.shape,'그레이')
print(type(img2), img2.shape)

#보안사고가 많아서 풀 path를 적어야함
