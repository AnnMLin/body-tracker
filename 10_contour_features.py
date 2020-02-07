# src: https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
import numpy as np
import cv2 as cv

link = 'ellipse.png'
img = cv.imread(link, 0)
img2 = cv.imread(link)
ret, thresh = cv.threshold(img, 127, 255, 0) # cv.THRESH_BINARY
contours, hierarchy = cv.findContours(thresh, 1, 2)
#print(contours)

# IMAGE MOMENTS : center of mass of obj, area of obj
cnt = contours[0]
print(cnt[:,:,1])
#cv.drawContours(img2, [cnt], 0, (0,255,0), 1)
#cv.imshow('cnt0', img2)
M = cv.moments(cnt)
#print(M)
# centroid:
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
#print(cx, cy)
cv.circle(img2, (cx,cy), 10, (0,0,255), 2)
cv.imshow('image', img2)

# CONTOUR AREA: the return value of cv.contourArea() or M['m00']
area = cv.contourArea(cnt)
#print(area)

# CONTOUR PERIMETER
perimeter = cv.arcLength(cnt, True)
#print(perimeter)

# CONTOUR APPROXIMATION
epsilon = 0.001*perimeter
approx = cv.approxPolyDP(cnt, epsilon, True) #epsilon:maximum distance from contour to approximated contour
#print(approx)
cv.drawContours(img2, [approx], -1, (0,0,255), 2)
cv.imshow('approx', img2)

# CONVEX HULL
hull = cv.convexHull(cnt)
#print(hull)
cv.drawContours(img2, [hull], -1, (255,0,255), 2)
cv.imshow('hull', img2)

# CHECKING CONVEXITY
k = cv.isContourConvex(cnt)
#print(k)

# BOUNDING RECTANGLE
x, y, w, h = cv.boundingRect(cnt) #(x, y): top left coord, w:width, h:height
cv.rectangle(img2,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('straigh rect', img2)

rect = cv.minAreaRect(cnt) # returns ( center (x,y), (width, height), angle of rotation )
#print(rect)
box = cv.boxPoints(rect)
#print(box)
box = np.int0(box)
#print(box)
cv.drawContours(img2, [box], 0, (255,255,0), 2)
cv.imshow('rotated rect', img2)

# MIN ENCLOSING CIRCLE
(x,y), radius = cv.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
cv.circle(img2, center, radius, (0,255,0), 2)
cv.imshow('min cir', img2)

# FITTING LINE
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv.fitLine(cnt, cv.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv.line(img2,(cols-1,righty),(0,lefty),(0,255,0),2)
cv.imshow('line', img2)


if cv.waitKey(0) == ord('q'): #wait 1 millisec for 'q' key to be pressed
  cv.destroyAllWindows()