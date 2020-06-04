#code that will detect basic characters present in image

import cv2
import imutils
import argparse
import numpy as np
import pytesseract

#create an argument parser for input image
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to pdf file")

#retrive variables from argument parser
args=vars(ap.parse_args())

#Store the image and convert to grayscale
img=cv2.imread(args["image"])
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#perform gaussian blur and do thresholding
gray_blur=cv2.GaussianBlur(gray,(3,3),1)
_,gray_bin=cv2.threshold(gray_blur,80,255,cv2.THRESH_BINARY_INV)

cv2.imshow('binary image',gray_bin)
cv2.waitKey(0)

'''
#detect contours in image
cnts=cv2.findContours(gray_bin,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
num_cnts=len(cnts)
for contour in cnts:
    x,y,w,h=cv2.boundingRect(contour)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0))

cv2.putText(img,'Num contours detected:'+str(num_cnts),(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.35,(0,0,255))

'''
text=pytesseract.image_to_string(gray_blur)
print(text)
#Resize the image
#gray=imutils.resize(gray,width=400,height=400)