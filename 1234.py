import cv2
import numpy as np
from matplotlib import pyplot as plt


#cv2.VideoCapture cap(0)
#    if(!cap.isOpened())
#        return -1

#img = cv2.imread('kryg2.jpg',0)
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#img2 = img.copy()
template = cv2.imread('BEST_SYMBOL_EVER.png',0)
#lol = template.rgba()
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
method = 'cv2.TM_CCORR_NORMED'
#methods = ['cv2.TM_CCORR_NORMED']
for meth in methods:
    #img = img2.copy()
    #img = cap
    method = eval(meth)
      
    res = cv2.matchTemplate(gray,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(gray,top_left, bottom_right, 255, 2)

    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(gray,cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()
    
