import cv2
import numpy as np
import matplotlib.pyplot as plt

class chek:
    def ck(self,a):
        self.c = a
        cv2.imshow('n', self.c)
        cv2.waitKey(0)
        cv2.destroyAllWindows()    

b = chek()


# 이미지 로드
image = cv2.imread(r'C:\Users\user\Desktop\imaging\image1.png')
if image is not None:
    
    gray_image1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)### 매우중요

    # 가우시안 블러링 
    blurred_image = cv2.GaussianBlur(gray_image1, (3, 3), 0) ### 얘는 그냥 이미지

    # 샤프닝
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) ### 얘도 그냥이미지
    sharpened_image = cv2.filter2D(blurred_image, -1, kernel)


    
    # 소벨 필터
    sobelx = cv2.Sobel(sharpened_image, cv2.CV_64F, 1, 0, ksize=5) ### 소벨필터는 그레이스케일 한놈
    sobely = cv2.Sobel(sharpened_image, cv2.CV_64F, 0, 1, ksize=5)

    # 캐니 엣지 검출
    edges = cv2.Canny(sharpened_image, 200, 300)        ### 엣지검출도 그레이스케일한놈, 컬러는 못잡아냄

    # 결과 저장


    cv2.imwrite('blurred_image.jpg', blurred_image)
    
    
    cv2.imwrite('sharpened_image.jpg', sharpened_image)

    cv2.imwrite('sobelx.jpg', sobelx)
    cv2.imwrite('sobely.jpg', sobely)
    cv2.imwrite('edges.jpg', edges)
    print("Images filtered successfully")
    b.ck(edges)
    #b.ck(sobelx)
    #b.ck(sobely)
    #b.ck(sharpened_image)
    #b.ck(blurred_image)


    hist = cv2.calcHist([gray_image1], [0], None, [256], [0, 256])
    plt.plot(hist)
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.title("Image Histogram")
    plt.show()




else:
    print("Error: Could not load image.")