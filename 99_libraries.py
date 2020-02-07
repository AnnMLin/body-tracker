## Video
cv.VideoCapture(0) #connect to first camera with 0(or -1), connect to second camera using 1, so on...
cv.VideoCapture.isOpened() # returns True(opened) of False
cv.VideoCapture.read() #Python: cv2.VideoCapture.read([image]) → retval, image
cv.VideoCapture.release()

## Image
cv.imread(str) # str: path to img file; second arg ImreadModes:https://docs.opencv.org/3.1.0/d4/da8/group__imgcodecs.html
img = np.zeros((512,512,3), np.uint8)# create a black image
cv.addWeighted(str, float, str, float, num) #(img1, α, img2, β, γ)
cv.imread.shape # returns [rows, cols, channels]

## Window
cv.namedWindow(str) # str: name for window #create a window

## mouse callback
cv.setMouseCallback(window, callback) # window: str->window name

## Trackbar
cv.createTrackbar('R', 'image', 0, 255, nothing) #(trackbar name, window name, value, count, onChange callback)
cv.getTrackbarPos('R', 'image') # get's trackbar value

## Display
cv.imgshow(str, input) # str: name, input: img or vid to show
cv.waitKey(num) # num = 0 default
cv.destroyAllWindows()

## Drawing
cv.line(img, (0,0), (511,511), (255,0,0), 5) #(img, start, end, color, line-weight)
cv.rectangle(img, (150,300), (510,128), (0,255,0), 3) #(img, top-left, bottom-right, color, line-weight)
cv.circle(img, (447,63), 63, (0,0,225), -1) #(img, center, radius, color, -1 = fill)
cv.ellipse(img, (256,256), (100,50), 0, 0, 120, (255,255,255), -1) 
#(img, center, (long axis, short axis), rotation, start angle, end angle, color, fill)

## Image Processing
cv.cvtColor()
  cv.COLOR_BGR2GRAY
  cv.COLOR_BGR2HSV # Hue range is [0,179], Saturation range is [0,255] and Value range is [0,255]
cv.threshold() # first arg is source img, should be grayscale
  cv.THRESH_BINARY #0
  cv.THRESH_BINARY+cv.THRESH_OTSU #8
  cv.THRESH_BINARY_INV #1
  cv.THRESH_TRUNC #2
  cv.THRESH_TOZERO #3
  cv.THRESH_TOZERO_INV #4
cv.adaptiveThreshold()
  cv.ADAPTIVE_THRESH_MEAN_C
  cv.ADAPTIVE_THRESH_GAUSSIAN_C
cv.bitwise_not()
cv.bitwise_and()
cv.add()
cv.inRange(inputArray, lowerArray, upperArray) # Checks if array elements lie between the elements of two other arrays.
cv.resize() # img scaling
cv.warpAffine() # img translation
cv.getRotationMatrix2D() # img rotation
cv.getAffineTransform() # img affine transformation (perspective)
cv.getPerspectiveTransform() #img perspective
cv.warpPerspective() # img perspective

## Mask
cv.findNonZero(mask)
cv.minMaxLoc(	src[, mask]	) # returns minVal, maxVal, minLoc, maxLoc
cv.mean(src, mask) #returns mean value

## Contours
cv.findContours(input_img, mode, method) # returns (contours, hierarchy) https://docs.opencv.org/2.4/modules/imgproc/doc/structural_analysis_and_shape_descriptors.html
  # mode:
  cv.RETR_EXTERNAL #0 retrieves only the extreme outer contours
  cv.RETR_LIST #1 retrieves all of the contours without establishing any hierarchical relationships.
  cv.RETR_CCOMP #2 retrieves all of the contours and organizes them into a two-level hierarchy. At the top level, there are external boundaries of the components. At the second level, there are boundaries of the holes. If there is another contour inside a hole of a connected component, it is still put at the top level.
  cv.RETR_TREE #3 retrieves all of the contours and reconstructs a full hierarchy of nested contours.

  #method:
  cv.CHAIN_APPROX_NONE #1
  cv.CHAIN_APPROX_SIMPLE #2
  cv.CHAIN_APPROX_TC89_L1 #3
  cv.CHAIN_APPROX_TC89_KCOS #4

cv.drawContours(background_img, contours, contourIdx(-1 for all), color, thickness)
cv.moments(cnt) #cnt = contours[0]
cv.contourArea(cnt)
cv.arcLength(cnt, True) # Second argument specify whether shape is a closed contour (if passed True), or just a curve.
cv.approxPolyDP(cnt, epsilon, True) #epsilon:maximum distance from contour to approximated contour
cv.convexHull(cnt)
cv.convexityDefects(cnt,hull)
cv.isContourConvex(cnt)
cv.boundingRect(cnt) #return x, y, w, h => (x, y): top left coord, w:width, h:height
cv.minAreaRect(cnt) # returns ( center (x,y), (width, height), angle of rotation )
cv.boxPoints()
cv.fitLine()
cv.pointPolygonTest(cnt(contour),point,True) # finds point to contour shortest dist (True) || whether point inside of contour or not (False)
cv.matchShapes(cnt1,cnt2,mode,0.0)