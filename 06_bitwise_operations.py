# src: https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html
import cv2 as cv
import numpy as np

#Load two images
img1 = cv.imread('messi5.jpg')
img2 = cv.imread('opencv-logo-white.png')

# ROI Region of Interest
# create a ROI
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# https://docs.opencv.org/3.4/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY) # retval, dst	=	cv.threshold(	src, thresh, maxval, type[, dst]	)

# Inverts every bit of an array
mask_inv = cv.bitwise_not(mask) # dst	=	cv.bitwise_not(	src[, dst[, mask]]	)

# black out the area of img2 in img1 ROI
img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv) # dst	=	cv.bitwise_and(	src1, src2[, dst[, mask]]	)

# Take only region of logo from logo image
img2_fg = cv.bitwise_and(img2, img2, mask = mask)

#put logo in ROI and modify the main image
dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('img2', img2)
cv.imshow('img2gray', img2gray)
cv.imshow('mask', mask)
cv.imshow('mask_inv', mask_inv)
cv.imshow('img1_bg', img1_bg)
cv.imshow('img2_fg', img2_fg)
cv.imshow('dst', dst)
cv.imshow('img1', img1)
cv.waitKey(0)
cv.destroyAllWindows()