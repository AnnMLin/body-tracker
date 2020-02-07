# src: https://docs.opencv.org/3.4/dc/d71/tutorial_py_optimization.html
import cv2 as cv
import numpy as  np

e1 = cv.getTickCount()
e2 = cv.getTickCount()
time = (e2 - e1)/ cv.getTickFrequency()

# Avoid using loops in Python as far as possible, especially double/triple loops etc. They are inherently slow.
# Vectorize the algorithm/code to the maximum possible extent because Numpy and OpenCV are optimized for vector operations.
# Exploit the cache coherence.
# Never make copies of array unless it is needed. Try to use views instead. Array copying is a costly operation.