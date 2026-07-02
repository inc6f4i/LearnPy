import cv2
import os
from matplotlib import pyplot as plt
import ctypes ##이번 강좌에서 볼거

path = os.getcwd()
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(os.path.abspath(__file__)) ##이라인이 중요



img = cv2.imread( dir_path + r'\lena.png', -1)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#b, g, r = cv2.split(img)
#rgb = cv2.merge([r, g, b])

cv2.imshow('windowName', img)
plt.imshow(rgb)
#plt.xticks([]) # x축 눈금 제거
plt.yticks([])
plt.show()
k = cv2.waitKey(0)

if k == 27: # esc key (ASCII 코드 27) #오 ㅋㅋ
    cv2.destroyAllWindows()
elif k == ord('s'): # 's' key (ASCII 코드 's')
    cv2.imwrite(dir_path + r'\lenagray.png',img)
    ctypes.windll.user32.MessageBoxW(0, "저장되었습니다.", "알림", 0)
    cv2.destroyAllWindows()
