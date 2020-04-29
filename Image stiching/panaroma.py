import cv2
import numpy as np
import imutils
im1=cv2.imread('sample_school_1.jpg')
im2=cv2.imread('sample_school_2.jpg')

class sticher(self,imgA,imgB):
    def __init__(self):
        print('initialized')
    
    def image_sticher(self,img1,img2):
        imgA=img1
        imgB=img2

        #Detect keypoints and features
        (kpsA,featuresA)=self.detectAnddescribe(imgA)
        (KpsB,featuresB)=self.detectAnddescribe(imgB)

        #Match features obtained
        M=self.MatchKeyPoints(kpsA,kpsB,featuresA,featuresB)

        if M is None:
            print('No key points matched. Try other algorithms')
            return None
        
        #Get the Matches,Homography matrix,status
        (Matches,H,status)=M

        #apply warp transform to stich images together
        result=cv2.warpPerspective(imgA,H,
        (imgA.shape[1] + imgB.shape[1], imgA.shape[0]))
		result[0:imgB.shape[0], 0:imgB.shape[1]] = imgB

        if showMatches:
            vis = self.drawMatches(imgA, imgB, kpsA, kpsB, Matches,
				status)
			# return a tuple of the stitched image and the
			# visualization
			return (result, vis)








#cv2.imshow('First image',im1)
#cv2.waitKey(0)
#cv2.destroyAllWindows