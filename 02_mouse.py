# src: https://docs.opencv.org/3.4/db/d5b/tutorial_py_mouse_handling.html
import cv2 as cv
import numpy as np

# events = [i for i in dir(cv) if 'EVENT' in i] #The Python dir() method tries to return a list of valid attributes of the object.
# print(events)

# mouse callback function
def draw_circle(event, x, y, flags, param):
  if event == cv.EVENT_LBUTTONDBLCLK:
    cv.circle(img, (x,y), 50, (255,0,0), -1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle) # bind callback to window

while True:
  cv.imshow('image', img)
  if cv.waitKey(20) & 0xFF == 27: #press Esc key to stop
    break

cv.destroyAllWindows()