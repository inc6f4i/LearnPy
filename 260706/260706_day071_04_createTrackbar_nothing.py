#260706_day071_04_.py




def nothing(x): # Trackbar Callback 함수 (empty function)
    pass

cv2.namedWindow('image')
cv2.createTrackbar('W', 'image', 0, 100, nothing) # W Trackbar (Blending 비율 조절)


