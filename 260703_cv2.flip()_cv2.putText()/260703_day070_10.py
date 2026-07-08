import cv2

img = cv2.imread(r'C:\Users\user\Desktop\imaging\a13.jpg')
shiftx = -45

# ball = img[409:454, 817:884] # ROI 설정 (야구공 영역)
# img[470:515, 817:884] = ball # ROI 영역을 다른 영역에 복사

img[409:454, 826:871] = img[409:454, 826+shiftx:871+shiftx]

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()