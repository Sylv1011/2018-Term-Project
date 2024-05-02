import cv2
import numpy as np
import matplotlib.pyplot as plt


##Sources: 
#https://www.youtube.com/watch?v=sARklx6sgDk

cap = cv2.VideoCapture(0)

while True:
 # Capture frame-by-frame
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_skin = np.array([0,30,60])
    upper_skin = np.array([12,150,255])
    
    #0，30，60，20，150，255
    
    mask = cv2.inRange(hsv, lower_skin, upper_skin)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    kernel = np.ones((15,15), np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    
    blur = cv2.GaussianBlur(res,(35,35),0)
    bilateral = cv2.bilateralFilter(res,35,75,75)
    
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    print(contours)
    
    cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('frame',1200,800)
    cv2.imshow('frame',frame)
    
    # cv2.imshow("mask",mask)
    
    cv2.namedWindow('res',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('res',1200,800)
    cv2.imshow('res', res)

    #cv2.imshow("smoothed", smoothed)
    
    cv2.namedWindow('blur',cv2.WINDOW_NORMAL)
    cv2.resizeWindow('blur',1200,800)
    cv2.imshow('blur', blur)
    
    # cv2.namedWindow('bilateral',cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('bilateral',1200,800)
    # cv2.imshow('bilateral', bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cv2.destroyAllWindows()
cap.release()
