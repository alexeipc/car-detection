import numpy as np
import cv2

cap = cv2.VideoCapture('video1.avi')
car_cascade = cv2.CascadeClassifier('cars.xml')
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

# Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 1) 
      
    # To draw a rectangle in each cars 
    for (x,y,w,h) in cars: 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),1) 
        #cv2.PutText(cv2.cv.fromarray(frame),'car', (x,y+h),font, 255)
        cv2.rectangle(frame,(x,y),(x+w,y-10),(255,255,255),-1)
        cv2.putText(frame,'Car',(x,y), font, 0.5,(0,0,0),1,cv2.LINE_AA)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capre
cap.release()
cv2.destroyAllWindows()