#먼저 콘솔에서 pip install Pillow opencv-python 설치 필요
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


# 빈 이미지 생성 (OpenCV)
img = np.zeros((300, 500, 3), dtype=np.uint8)
img.fill(255) # 흰 배경


# OpenCV 이미지를 Pillow 이미지로 변환
pil_img = Image.fromarray(img) #대문자이니 클래스 부르니 객체생성됨


# 폰트 설정 (예: 나눔고딕, 경로에 맞게 수정)
font_path = "NanumGothic.ttf" # 또는 "malgun.ttf" 등
font_size = 30

font = ImageFont.truetype(font_path, font_size) # 폰트라는 객체로 다시 만듦


# Pillow로 텍스트 그리기
draw = ImageDraw.Draw(pil_img) #드로우 메서드로 객체를 또 만듦
text = "한글 텍스트 표시"

draw.text((50, 150), text, font=font, fill=(0, 0, 255)) # 빨간색


# Pillow 이미지를 OpenCV 이미지로 변환
img = np.array(pil_img)


# 결과 출력
cv2.imshow("Korean Text Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows() 