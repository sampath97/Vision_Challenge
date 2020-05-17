
import cv2
import numpy as np
import imutils

#function for return keypoints and features of an image    
def detectkps_describefeatures(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    sift_descriptor=cv2.xfeatures2d.SIFT_create()
    (kps,features)=sift_descriptor.detectAndCompute(img,None)
    kps = np.float32([kp.pt for kp in kps])
    return (kps,features)

#function for matching descriptors between two image
def match_descriptors(featuresA,featuresB,reprojThresh,ratio,kpsA,kpsB):
    sift_matcher=cv2.DescriptorMatcher_create("BruteForce")
    rawMatches=sift_matcher.knnMatch(featuresA,featuresB,2)
    matches=[]

    for m in rawMatches:
        if len(m) == 2 and m[0].distance < m[1].distance * ratio:
            matches.append((m[0].trainIdx, m[0].queryIdx))

    if len(matches) > 4:
        ptsA = np.float32([kpsA[i] for (_, i) in matches])
        ptsB = np.float32([kpsB[i] for (i ,_) in matches])

        (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,reprojThresh)

        return (matches, H, status)

    return None
	

	





    
im1=cv2.imread('D:\Vision Challenge\Image stiching\sample_school_1.jpg')
im2=cv2.imread('D:\Vision Challenge\Image stiching\sample_school_2.jpg')

#detect keypoints for first image
(kpsA,featuresA)=detectkps_describefeatures(im1)
(kpsB,featuresB)=detectkps_describefeatures(im2)

#calculate matches
(matches,H,status)=match_descriptors(featuresA,featuresB,4,0.75,kpsA,kpsB)

#perform warp transform
result=cv2.warpPerspective(im1,H,(im1.shape[1]+im2.shape[1],im1.shape[0]))
result[0:im2.shape[0], 0:im2.shape[1]] = im2

# Draw first 10 matches.
#img3 = cv2.drawMatches(im1,kpsA,im2,kpsB,matches[:10],flags=2)

cv2.imshow('Stiched Image',result)
cv2.waitKey(0)
cv2.destroyAllWindows






#cv2.imshow('First image',im1)
#cv2.waitKey(0)
#cv2.destroyAllWindows