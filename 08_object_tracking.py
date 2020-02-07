# src: https://docs.opencv.org/3.4/df/d9d/tutorial_py_colorspaces.html
# Goal: track a blue object
# Method:
# Take each frame of the video
# Convert from BGR to HSV color-space
# We threshold the HSV image for a range of blue color
# Now extract the blue object alone, we can do whatever on that image we want.
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:

  # Take each frame
  _, frame = cap.read()

  # Convert BGR to HSV
  hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

  # define range of blue color in HSV
  lower_blue = np.array([110,50,50])
  upper_blue = np.array([130,255,255])

  # Threshold the HSV image to get only blue colors
  mask = cv.inRange(hsv, lower_blue, upper_blue)

  res = cv.bitwise_and(frame, frame, mask = mask)

  cv.imshow('frame', frame)
  cv.imshow('mask', mask)
  cv.imshow('res', res)
  if cv.waitKey(5) & 0xFF == 27:
    break

cap.release()
cv.destroyAllWindows()

# How to find HSV values to track?
# >>> green = np.uint8([[[0,255,0 ]]])
# >>> hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
# >>> print( hsv_green )
# [[[ 60 255 255]]]
# take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively