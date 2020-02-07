import numpy as np
import cv2 as cv

im = cv.imread('space.jpg')
imCopy = im.copy()
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, img = cv.threshold(imgray, 127, 255, 0)
# cv.imshow('img1', img)
contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# print(x[2])
cv.drawContours(imCopy, contours, -1, (0,255,0), 1)
cv.imshow('img', imCopy)
cv.waitKey(0)
cv.destroyAllWindows()