import cv2
import time
import numpy as np
c = cv2.VideoCapture(0)
def desp():
    _ , f = c.read()
    res = cv2.matchTemplate(f,tem,cv2.TM_CCOEFF_NORMED)
    pnt = np.unravel_index(res.argmax(),res.shape)  
    cv2.rectangle(f,(pnt[0]+50,pnt[1]+50),pnt,255)
    cv2.imshow('example',f)
    cv2.waitKey(1)

tem = cv2.imread(r"C:\Users\<my user>\Pictures\findMe.jpg")
otm = time.time()
while otm + 40 > time.time():
    desp()
