# src: https://docs.opencv.org/3.4/d0/d86/tutorial_py_image_arithmetics.html
# add 2 images:
#   using opencv function: cv.add() #saturated operation
#   using numpy operation: res = img1 + img2 #modulo operation

import numpy as np
import cv2 as cv

space = cv.imread('space.jpg')
cat = cv.imread('cat.jpg')

# g(x)=(1−α)f0(x)+αf1(x)
# dst=α⋅img1+β⋅img2+γ
dst = cv.addWeighted(space, 0.5, cat, 0.5, 0) #(img1, α, img2, β, γ)

cv.imshow('dst', dst)
cv.waitKey(0)
cv.destroyAllWindows()