# src: https://docs.opencv.org/3.4/dc/da5/tutorial_py_drawing_functions.html
import numpy as np
import cv2 as cv

# create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5px
cv.line(img, (0,0), (511,511), (255,0,0), 5) #(img, start, end, color, line-weight)

cv.rectangle(img, (150,300), (510,128), (0,255,0), 3) #(img, top-left, bottom-right, color, line-weight)

cv.circle(img, (447,63), 63, (0,0,225), -1) #(img, center, radius, color, -1 = fill)

cv.ellipse(img, (256,256), (100,50), 0, 0, 120, (255,255,255), -1) 
#(img, center, (long axis, short axis), rotation, start angle, end angle, color, fill)

cv.imshow('image', img)
if cv.waitKey(0) == ord('q'): #wait 1 millisec for 'q' key to be pressed
  cv.destroyAllWindows()