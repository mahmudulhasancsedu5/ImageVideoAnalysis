import cv2
import numpy as np

image_path="F://openCV//Resources//messi.jpg"
video_path="F://openCV//Resources//video//Lionel Messi.MP4"



img=cv2.imread(image_path,cv2.IMREAD_COLOR)



#draw line

cv2.line(img,(0,0),(200,200),(0,0,255),1) #line
cv2.rectangle(img,(20,20),(100,100),(255,0,0),5) #rectangle
cv2.circle(img,(200,300),100,(0,255,0),-1) #draw circle

pts=np.array([[10,10],[50,50],[100,200],[250,400]],np.int32) # draw polygon

cv2.polylines(img,[pts],True,(0,255,255),3)



font=cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img,"open cv",(100,200),font,3,(255,255,0),1,cv2.LINE_AA)



cv2.imshow('image',img)





cv2.waitKey(0)
cv2.destroyAllWindows()










