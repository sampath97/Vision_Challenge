#practice to output after filtering with different kernels like mean,gaussian,sharpening etc
# The kernels are also being altered to see the output effect
 
import cv2
import imutils
import numpy as np

im=cv2.imread('Images/fam_sample5.jpg')
gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
gray_im=imutils.resize(gray_im,height=300)

k1=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
k2=np.array([[1,2,1],[2,4,2],[1,2,1]])/16

filt_im=cv2.filter2D(gray_im,-1,k2)
filt_im2=cv2.filter2D(filt_im,-1,k1)
stacked_im=np.hstack((filt_im,filt_im2))

cv2.imshow('Filtered Image',stacked_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

