@author: chandrakanta chaudhury
"""

import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True :
    ret , frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_white = np.array([150,150,150])
    upper_white = np.array([255,255,255])
    mask =cv2.InRange(hsv,lower_white,upper_white)
    res = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)  & 0xFF
    
    if k==25:
        break
    
cv2.destroyAllWindows()
cap.release()
