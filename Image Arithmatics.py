import cv2
import numpy as np


image_path="F://openCV//Resources//"

img1=cv2.imread(image_path+"paris.jpg",cv2.IMREAD_COLOR)

img2=cv2.imread(image_path+"2.jpg",cv2.IMREAD_COLOR)


#add=img1+img2
#add=cv2.add(img1,img2)

weighted=cv2.addWeighted(img1,0.5,img2,0.5,0)



cv2.imshow('image',weighted)
cv2.imwrite(image_path+'messi_parice.jpg',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
