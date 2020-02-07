# src: https://docs.opencv.org/3.4/d3/df2/tutorial_py_basic_ops.html
import numpy as np
import cv2 as cv

img = cv.imread('messi5.jpg')

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

while True:
  cv.imshow('image', img)
  if cv.waitKey(20) & 0xFF == 27: #press Esc key to stop
    break

cv.destroyAllWindows()

print(img[:,0,:])
# other notes
# b,g,r = cv.split(img)
# img = cv.merge((b,g,r))

# b = img[:,:,0] # gets all blue pixels
# img[:,:,2] = 0 # sets all red pixels to 0