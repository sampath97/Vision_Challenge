import cv2
import imutils
import numpy as np
import os

img_name='circle3.jpg'
img_path=os.path.join('Images',img_name)
out_img_name=os.path.join('Images',img_name.rsplit('.', 1)[0]+'_result'+'.jpg')
print(out_img_name)

img=cv2.imread(img_path)
img=imutils.resize(img,width=400)
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Apply gaussian blur
gray_img=cv2.GaussianBlur(gray_img,(9,9),0)

#create sharpening filter kernel
k=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])/1
out_img=cv2.filter2D(gray_img,-1,k)

#find the edges
edges = cv2.Canny(out_img, threshold1=40, threshold2=100)


#Detect circles in image
circles =cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1.2, minDist=1,minRadius=30, maxRadius=120)
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for x,y,r in circles:
        cv2.circle(img,(x,y),r,(0,255,0),2)
        cv2.putText(img,'Radius:'+str(r),(x+r,y+r),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),1, cv2.LINE_AA)
        cv2.imwrite(out_img_name,img)



stacked_img=np.hstack((out_img,gray_img))
cv2.imshow('Output img',img)
cv2.imshow('edges',edges)
#cv2.imshow('Onion image',stacked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
