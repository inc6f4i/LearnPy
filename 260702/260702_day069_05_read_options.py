#260702_day069_05_.py
import cv2
lena = r'C:\Users\user\Desktop\imaging\lena.png'

img0 = cv2.imread(lena, 1)
img1 = cv2.imread(lena, 0)
img2 = cv2.imread(lena, -1)

cv2.imshow('color', img0)
cv2.imshow('gray', img1)    
cv2.imshow('unchanged', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(type(img0), img0.shape)
print(type(img1), img1.shape,'그레이')
print(type(img2), img2.shape)