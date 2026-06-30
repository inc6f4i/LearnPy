#260630_day067_03_.py
import cv2
image = cv2.imread(r'C:\Users\user\Desktop\a9.jpg')

if image is None:
    print('null image')
    exit(1)
else :
    cv2.imwrite(r'C:\Users\user\Desktop\o_a9.jpg', image)
    print("image saved as o_a9.jpg")

    

