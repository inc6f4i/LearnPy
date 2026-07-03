import cv2
from matplotlib import pyplot as plt

img = r'C:\Users\user\Desktop\imaging\contest_02.jpg'
im = cv2.imread(img)

plt.axis('on')
plt.imshow(im)
plt.show()
