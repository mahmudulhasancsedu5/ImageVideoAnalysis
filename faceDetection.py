import cv2
import numpy as mp
import matplotlib.pyplot as plt


print('Mahmud')

#loading image feed
image_name='messi.jpg'


def loadImageCV2(image_name):
    img=cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
    #IMREAD_COLOR = 1
    #IMREAD_UNCHANGED = -1

    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def loadImagePlt(image_name):
    img=cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
    plt.imshow(img,cmap='gray',interpolation='bicubic')
    plt.plot([0,500],[700,50],'c',linewidth=1)
    plt.show()
    
    
      
    



#loadImageCV2(image_name)

loadImagePlt(image_name)


    
