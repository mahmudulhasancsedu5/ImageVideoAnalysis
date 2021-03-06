import cv2
import numpy as np


image_folder="F://openCV//Resources//"


#load 2 image
img1=cv2.imread(image_folder+"2.jpg",cv2.IMREAD_COLOR)
img2=cv2.imread(image_folder+"paris.jpg",cv2.IMREAD_COLOR)


rows,cols,channels=img2.shape
print(rows,cols,channels)

roi=img1[0:rows, 0:cols]

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img2gray)


ret,mask=cv2.threshold(img2gray,180,255,cv2.THRESH_BINARY)

mask_inv=cv2.bitwise_not(mask)

#now black grout the area of logo in ROI
img1_bg=cv2.bitwise_and(roi,roi,mask = mask)


img2_fg=cv2.bitwise_and(img2,img2,mask=mask_inv)

dst=cv2.add(img1_bg,img2_fg);



img1[0:rows,0:cols]=dst

#img2_bg=cv2.birwise_and(img2,ing2,mask =)

cv2.imshow("res",img1)
cv2.imshow("mask",mask)
cv2.imshow("ret",ret)
cv2.imshow("mask_inv",mask_inv)



cv2.imshow("image1",img1)
cv2.imshow("image2",img2)


cv2.waitKey(0)

cv2.destroyAllWindows()
