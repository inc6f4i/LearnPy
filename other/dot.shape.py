import sys
import cv2

im1 = cv2.imread(r'C:\Users\user\Desktop\imaging\a9.jpg', cv2.IMREAD_GRAYSCALE)
im2 = cv2.imread(r'C:\Users\user\Desktop\imaging\a10.png', cv2.IMREAD_COLOR)

h, w = im2.shape[:2]
print('im1, im2 shapes',im1.shape, im2.shape) 

for y in range(300,h):
    for x in range(300,w):
        im1[y,x] = 255
        im2[y,x] = (0,0,255)

im1[300:640, 300:640] = 0
im2[300:640, 300:640] = (0,0,255) # BGR !

cv2.imshow('im1', im1)
cv2.imshow('im2', im2)

cv2.waitKey(0)
cv2.destroyAllWindows()
