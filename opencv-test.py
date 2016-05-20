import cv2
import numpy as np
from matplotlib import pyplot as plt

def trackerUpdated(val):
  print val;

#control window
cv2.namedWindow("Control", cv2.WINDOW_AUTOSIZE)

iLowH = 0
iHighH = 179

iLowS = 0
iHighS = 255

iLowV = 0
iHighV = 255

# Create trackbars in "Control" window
cv2.createTrackbar("LowH", "Control", iLowH, 179, trackerUpdated) # //Hue (0 - 179)
cv2.createTrackbar("HighH", "Control", iHighH, 179, trackerUpdated)

cv2.createTrackbar("LowS", "Control", iLowS, 255,trackerUpdated) #Saturation (0 - 255)
cv2.createTrackbar("HighS", "Control", iHighS, 255,trackerUpdated)

cv2.createTrackbar("LowV", "Control", iLowV, 255,trackerUpdated) #Value (0 - 255)
cv2.createTrackbar("HighV", "Control", iHighV, 255,trackerUpdated)
    
cap = cv2.VideoCapture(0)
while (True):
  (ret, frame) = cap.read()


  # Our operations on the frame come here
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  

  # edgesC = cv2.Canny(frame,100,200)
  edgesG = cv2.Canny(gray,100,200)  
  
  edgesImg = cv2.cvtColor( edgesG, cv2.COLOR_GRAY2BGR );
  
  cv2.imshow("test1", frame)
  cv2.imshow("test2", edgesImg)
   
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows() 
