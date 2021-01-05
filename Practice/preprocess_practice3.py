#code to analyze the color object tracking with RGB and HSV color space
import cv2
import imutils
import numpy as np

cam=cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

# Define the codec and create VideoWriter object 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480)) 


def nothing(x): 
    return 0

#create a named window
cv2.namedWindow("Trackbars")

#create trackbars
#trackbar inout arguments are name of trackbar,window name,min value,max value,callback
'''
cv2.createTrackbar("L-R","Trackbars",0,255,nothing)
cv2.createTrackbar("L-G","Trackbars",0,255,nothing)
cv2.createTrackbar("L-B","Trackbars",0,255,nothing)
cv2.createTrackbar("H-R","Trackbars",0,255,nothing)
cv2.createTrackbar("H-G","Trackbars",0,255,nothing)
cv2.createTrackbar("H-B","Trackbars",0,255,nothing)
'''
cv2.createTrackbar("L-H","Trackbars",0,180,nothing)
cv2.createTrackbar("L-S","Trackbars",0,255,nothing)
cv2.createTrackbar("L-V","Trackbars",0,255,nothing)
cv2.createTrackbar("H-H","Trackbars",0,180,nothing)
cv2.createTrackbar("H-S","Trackbars",0,255,nothing)
cv2.createTrackbar("H-V","Trackbars",0,255,nothing)

while True:
    ret,img=cam.read()
    img=cv2.flip(img,1)
    img2=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    ''' 
    #get the values from the trackbars
    l_r=cv2.getTrackbarPos("L-R","Trackbars")
    l_g=cv2.getTrackbarPos("L-G","Trackbars")
    l_b=cv2.getTrackbarPos("L-B","Trackbars")
    h_r=cv2.getTrackbarPos("H-R","Trackbars")
    h_g=cv2.getTrackbarPos("H-G","Trackbars")
    h_b=cv2.getTrackbarPos("H-B","Trackbars")
   '''
    l_h=cv2.getTrackbarPos("L-H","Trackbars")
    l_s=cv2.getTrackbarPos("L-S","Trackbars")
    l_v=cv2.getTrackbarPos("L-V","Trackbars")
    h_h=cv2.getTrackbarPos("H-H","Trackbars")
    h_s=cv2.getTrackbarPos("H-S","Trackbars")
    h_v=cv2.getTrackbarPos("H-V","Trackbars")
    '''
    lower_range_rgb=np.array([l_b,l_g,l_r])
    higher_range_rgb=np.array([h_b,h_g,h_r])
    '''
    lower_range_hsv=np.array([l_h,l_s,l_v])
    higher_range_hsv=np.array([h_h,h_s,h_v])


    #get the mask for the corresponding color
    #mask_rgb=cv2.inRange(img,lower_range_rgb,higher_range_rgb)
    mask_hsv=cv2.inRange(img2,lower_range_hsv,higher_range_hsv)
    
    #comnine mask and img 
    #res_rgb=cv2.bitwise_and(img,img,mask=mask_rgb)
    res_hsv=cv2.bitwise_and(img,img,mask=mask_hsv)

    #stacked image
    stack_img=np.hstack((img,res_hsv))
    out.write(np.uint8(stack_img))
    
    cv2.imshow("Trackbars",cv2.resize(stack_img,None,fx=0.4,fy=0.4))
    key=cv2.waitKey(1)
    if key==27:
        break
    

cam.release()
out.release()
cv2.destroyAllWindows()