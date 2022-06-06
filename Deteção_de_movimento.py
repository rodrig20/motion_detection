import cv2
 
cap = cv2.VideoCapture(0)
del_bg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
t = 0
while True:
    _,frame = cap.read()
    frame = cv2.blur(frame, (15,15))
    mask_bg = del_bg.apply(frame)
    
    cv2.imshow('fgmask', mask_bg)
    #cv2.imshow('frame',frame )
 
     
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()