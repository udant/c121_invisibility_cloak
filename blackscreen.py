import cv2
import time
import numpy as np
from google.colab import files
fourcc=cv2.VideoWriter_fourcc(*"XVID")
outputfile=cv2.VideoWriter("output.avi",fourcc,30.0,(640,480))
cap=cv2.VideoCapture(0)
time.sleep(2)
frame=files.upload()
for i in range(60):
    ret,frame=cap.read()
frame=np.flip(frame,axis=1)
while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=cv2.resize(frame,(640,480))
    frame=cv2.resize(frame,(640,480))
    lower_black = np.array([30,30,0])
    upper_black = np.array([104,153,70])
    mask1=cv2.inRange(frame,lower_black,upper_black)
    lower_black = np.array([170,120,70])
    upper_black = np.array([180,255,255])
    res=cv2.bitwise_and(frame,frame,mask=mask1)
    finaloutput=frame - res
    finaloutput=np.where(finaloutput == 0,img,finaloutput)
    outputfile.write(finaloutput)
    cv2.imshow(finaloutput)
    cv2.waiKey(1)
cap.release()
out.release()
cv2.destroyAllWindows()    