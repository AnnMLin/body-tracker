# src: https://docs.opencv.org/3.4/dd/d43/tutorial_py_video_display.html
# Access pixel values and modify them
# Access image properties
# Setting Region of Interest (ROI)
# Splitting and Merging images
import numpy as np
import cv2 as cv

# print(cv.__version__)
# print(np.__version__)

cap = cv.VideoCapture(0) #connect to first camera with 0(or -1), connect to second camera using 1, so on...

#check if cap is initialized of not
if not cap.isOpened(): #returns True(opened) or False
  print('Camera not opened')
  # cap.open()
  exit()

while True:
  #Capture frame-by-frame
  #https://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=read#cv2.VideoCapture.read
  #https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a473055e77dd7faa4d26d686226b292c1
  #Python: cv2.VideoCapture.read([image]) → retval, image
  ret, frame = cap.read() #if frame is read correctly ret is True

  if not ret:
    print("Can't receive frame (stream end?). Exiting ...")
    break

  cookie = frame[280:340, 330:390]
  frame[273:333, 100:160] = cookie
  
  #Operations on the frame
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  #Display the resulting frame
  cv.imshow('frame', gray)
  if cv.waitKey(1) == ord('q'): #wait 1 millisec for 'q' key to be pressed
    break #break while loop

#when everything done, release the capture
cap.release()
cv.destroyAllWindows()