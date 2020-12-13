#practice to output after filtering with different kernels like mean,gaussian,sharpening etc
# The kernels are also being altered to see the output effect
 
import cv2
import imutils
import numpy as np

im=cv2.imread('Images/success_kid.png')
k=np.array([[0,-5,0],[-5,21,-5],[0,-5,0]])

gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
filt_im=cv2.filter2D(gray_im,-1,k)
stacked_im=np.hstack((gray_im,filt_im))
cv2.imshow('Filtered Image',stacked_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

