import cv2
import numpy as np

video_directory="..//resources//video//"


cap=cv2.VideoCapture(0)

#cap=cv2.VideoCapture(0) #for web cam

fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter(video_directory+'output.MP4',fourcc,20.0,(640,480))
id=1;
while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    out.write(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    #cv2.imwrite("..//resources//img//img_"+str(id)+".png",frame)
    id=id+1
    
    
    if cv2.waitKey(1) & 0xFF== ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()

