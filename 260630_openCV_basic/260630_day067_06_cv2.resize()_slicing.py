#260630_day067_06_.py
import cv2
r = cv2.imread(r'C:\Users\user\Desktop\a9.jpg')

j = cv2.resize(r, None, fx= 0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

j1 = j[:600,0:]
cv2.imshow("i",j1)
cv2.waitKey(0)
cv2.destroyAllWindows()

j2 = j[0:,800:]
cv2.imshow("i",j2)
cv2.waitKey(0)
cv2.destroyAllWindows()

j3 = j[600:,0:]
cv2.imshow("i",j3)
cv2.waitKey(0)
cv2.destroyAllWindows()

j4 = j[0:,:800]
cv2.imshow("i",j4)
cv2.waitKey(0)
cv2.destroyAllWindows()