import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def putKor(img, text, position, font_size, color):
    font_path = r'C:\Users\user\Desktop\imaging\MaruBuri-Regular.ttf'
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))#필로우용 클래스로 재탄생한 이미지
    draw = ImageDraw.Draw(img_pil)#드로우 메서드로 객체를 또 만듦
    font = ImageFont.truetype(font_path, font_size)
    
    # PIL은 RGB 순서이므로 color를 (B, G, R)에서 (R, G, B)로 뒤집어줍니다.
    draw.text(position, text, font=font, fill=(color[2], color[1], color[0]))

    
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)


img = cv2.imread(r'C:\Users\user\Desktop\imaging\contest_02.jpg', cv2.IMREAD_COLOR)

img = putKor(img, '김동진 참가완료', (30, 0), 30, (0, 255, 0))

cv2.imshow('result', img)
cv2.waitKey(0)  
cv2.destroyAllWindows()


#두개의 다른클래스가 동작해서 
"""
1. cv.2imread()로 이미지를 읽어오면 OpenCV의 이미지 객체가 생성됩니다.
2. putKor() 함수호출
3. 폰트 경로 정의
4. Image 클랫의 fromarray() 메서드에 BGR 배열을 RGB 배열로 객체생성
5. Image 클래스의 안의 Draw 클래스로 그릴 배열 객체 생성
6. 폰트클래스 객체 생성
7. 

"""