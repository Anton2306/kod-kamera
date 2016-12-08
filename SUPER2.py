# Code for Matrix Matching Workshop
# Save as a .py file
# Mr. Michaud
# www.nebomusic.net

import cv2 as cv2
import numpy as np
import scipy as sc

# Function to match patch
# Function for matching and drawing Rectangle
# Inputs: frame, patch, color
# Returns - point of match
def matchPatch(frame, patch, color):
    # Fetch grayscale image from camera and find normalized correlation with patch
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f = cv2.matchTemplate(gray, patch, cv2.TM_SQDIFF)
    point = np.where(f == f.max())
    # Coordinates for drawing rectangle
    w = len(patch[0]) # width
    l = len(patch)    # length
    x = point[1][0]
    y = point[0][0]
    #Plot rectangle on match
    cv2.rectangle(frame, (x,y), (x+w, y+l), color, thickness=2, lineType=8, shift=0)
    #Update patch with current best match - adaptive
    patch = gray[y:y+l, x:x+w]
    #return f normalized
    # return (f - f.min()) / (f.max() - f.min())
    return point



###########  Set Paths for patch #############

# Paths for patch - uncomment to use
path = "/home/pi/kod-kamera/BEST_SYMBOL_EVER.png"
patch = cv2.imread(path,0)

##############################################



######  Camera Read and Display Code #########

# Setup Camera Object: 0 is the index of the installed camera
cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()

    # Show Video
    if ret==True:
        # Find Match, uncomment to use
        matchPatch(frame, patch, (0, 0, 255))
        cv2.imshow('Camera', frame)

    # Exit Sequence
    # Exits on 'q' key pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break

##############################################

# Release cap object from memory and turn off camera
cap.release()
