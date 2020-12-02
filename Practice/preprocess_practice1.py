import cv2
import imutils
import numpy as np

im=cv2.imread('Images/snow_sample2.jpg')
b_im=im[:,:,0]

gray_im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
gray_im=imutils.resize(gray_im,height=400)
a,b=gray_im.shape
print(a,b)
hist_eq_im=cv2.equalizeHist(gray_im)

norm_im=np.zeros((a,b))
norm_im = cv2.normalize(gray_im, norm_im, 0, 255, cv2.NORM_MINMAX)
stacked_im=np.hstack((gray_im,hist_eq_im,norm_im)) 

cv2.imshow('Image',stacked_im)
cv2.waitKey(0)
cv2.destroyAllWindows()
#print('Dimensions:'+str(im.shape))
#print('Num of pixels:'+str(im.size))
#print('Datatype:'+str(im.dtype))

b_mean=np.mean(b_im)
print(b_mean)

if b_mean>123:
    print('Alert threshold breached')


