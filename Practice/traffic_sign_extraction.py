import cv2
import imutils
import numpy as np

img=cv2.imread('Images/traffic_sign1.jpg')
img=imutils.resize(img,height=400)
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

def nothing(x):
    return 0

#created a named window for the trackbar
cv2.namedWindow("Trackbars")

#create trackbars for lower,upper HSV values
cv2.createTrackbar("L-H",'Trackbars',0,180,nothing)
cv2.createTrackbar("L-S",'Trackbars',0,255,nothing)
cv2.createTrackbar("L-V",'Trackbars',0,255,nothing)
cv2.createTrackbar("U-H",'Trackbars',0,180,nothing)
cv2.createTrackbar("U-S",'Trackbars',0,255,nothing)
cv2.createTrackbar("U-V",'Trackbars',0,255,nothing)

while(1):
    #get trackbar positions
    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S","Trackbars")
    l_v=cv2.getTrackbarPos("L-V","Trackbars")
    u_h=cv2.getTrackbarPos("U-H","Trackbars")
    u_s=cv2.getTrackbarPos("U-S","Trackbars")
    u_v=cv2.getTrackbarPos("U-V","Trackbars")

    lower_hsv=np.array([l_h,l_s,l_v])
    upper_hsv=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv_img,lower_hsv,upper_hsv)
    out_img=cv2.bitwise_and(img,img,mask=mask)
    stacked_img=np.hstack((img,out_img))

    cv2.imshow('Binary output',stacked_img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break


cv2.destroyAllWindows()