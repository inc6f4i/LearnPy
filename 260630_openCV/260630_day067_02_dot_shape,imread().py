#260630_day067_02_.py
import cv2
import numpy as np

print(cv2.__version__)

image_path = r'E:\code\learnPy\260630\a7.jpg'

image = cv2.imread(image_path)

if image is None:
    print('이미지를 읽지 못했습니다.')
else:
    print('이미지 읽기 성공')
    print(image.shape)