import cv2
import numpy as np


img_path="F://openCV//Resources//messi.jpg"

img=cv2.imread(img_path,cv2.IMREAD_COLOR)


img[55,55]=[255,255,255]
px =img[55,55]

print(px)


#img[100:250, 100:350] =[0,0,0] #region of image

messi=img[50:400, 200:500]

img[0:350, 0:300]=messi

#print (roi)

#moving region of image






cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

