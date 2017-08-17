import cv2
import numpy as np

imageFolder="F://openCV//Resources//"
imageName='bookpage.jpg'

img = cv2.imread(imageFolder+imageName)
retval1,threshold1=cv2.threshold(img,8,255,cv2.THRESH_BINARY)

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2,threshold2=cv2.threshold(imgGray,8,255,cv2.THRESH_BINARY)

gaus=cv2.adaptiveThreshold(imgGray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,111,1)


cv2.imshow("image1",img)
cv2.imshow("threshold1",threshold1)

cv2.imshow("imageGray",imgGray)
cv2.imshow("threshold2",threshold2)

cv2.imshow("gaus",gaus)


cv2.waitKey(0)
cv2.destroyAllWindows()



