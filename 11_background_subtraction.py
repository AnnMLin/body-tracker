
from __future__ import print_function
import cv2 as cv


## [create]
#create Background Subtractor objects
backSub = cv.createBackgroundSubtractorKNN()
print(backSub)
## [create]

## [capture]
capture = cv.VideoCapture(0)
if not capture.isOpened:
    print('Unable to open camera')
    exit()
## [capture]

while True:
    ret, frame = capture.read()
    if frame is None:
        break

    ## [apply]
    #update the background model
    fgMask = backSub.apply(frame, learningRate = -1)
    ## [apply]

    ## [show]
    #show the current frame and the fg masks
    cv.imshow('FG Mask', fgMask)
    ## [show]

    keyboard = cv.waitKey(30)
    if keyboard == 'q' or keyboard == 27:
        break