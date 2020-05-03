
import cv2
import numpy as np
import imutils

#function for return keypoints and features of an image    
def detectkps_describefeatures(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift_descriptor=cv2.xfeatures2d.SIFT_create()
    (kps,features)=sift_descriptor.detectAndCompute(img,None)
    return (kps,features)

#function for matching descriptors between two image
def match_descriptors(featuresA,featuresB):
    sift_matcher=cv2.DescriptorMatcher_create("Brute Force")
    matches=sift_matcher.knnMatch(featuresA,featuresB,2)
    return matches

 #function for computing homography matrix
 def compute_homography:
     print('starting homography')   
    

im1=cv2.imread('D:\Vision Challenge\Image stiching\sample_school_1.jpg')
im2=cv2.imread('D:\Vision Challenge\Image stiching\sample_school_2.jpg')

#detect keypoints for first image
(kpsA,featuresA)=detectkps_describefeatures(im1)
(kpsB,featuresB)=detectkps_describefeatures(im2)

#print(kpsB)














#cv2.imshow('First image',im1)
#cv2.waitKey(0)
#cv2.destroyAllWindows