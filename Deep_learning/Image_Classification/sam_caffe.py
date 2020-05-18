# example
# python deep_learning_with_opencv.py --image images/jemma.png --prototxt bvlc_googlenet.prototxt --model bvlc_googlenet.caffemodel --labels synset_words.txt

#Reference
#https://www.pyimagesearch.com/2017/08/21/deep-learning-with-opencv/

#Assumptions doing this exercise with Imagenet bundle set
#B G R Mean subtaction values for Imagenet database are (104, 117, 123)
'''
#import necessary modules
import argparse

#Create argument parser object
ap=argparse.ArgumentParser()

#add optional input arguments
ap.add_argument("-i", "--image", required=True,
    help="path to input image")    
args=vars(ap.parse_args())

img=main(args)
cv2.imshow('output image',img)
'''

def main(input_image):
    import cv2
    import numpy as np
    import time
    import imutils

    #Load model architecture path
    model_architecture_path='bvlc_googlenet.prototxt'

    #Load weights of layers path for caffe model
    weight_layers= 'bvlc_googlenet.caffemodel'

    #Load labels
    lables_path= 'synset_words.txt'

    #Start algorithm
    img=cv2.imread(input_image)
    if img is None:
        return None
    else:
    #img=imutils.resize(img,width=224,height=224)

        classes=[] #declare classes containing trained object names 
        img_lables=open(lables_path).read().strip().split("\n") #Read each label into array and split thebased on new line charcter
        #Extract lables into array
        for idx,obj_label in enumerate(img_lables):
            temp=obj_label[obj_label.find(" ")+1:]  #find spaces and split them after spaces
            classes.append(temp.split(",")[0])
            

        #Create dnn object
        net=cv2.dnn.readNetFromCaffe(model_architecture_path,weight_layers)
        blobs=cv2.dnn.blobFromImage(img,1,(244,244),(104, 117, 123)) #Do mean subraction and detect blobs

        #Give this blobs as input
        start_time=time.time()
        net.setInput(blobs)  #set blob as input
        predictions=net.forward()  #forward the input to neural network and get prediction
        end_time=time.time()
        print('execution time')
        print(end_time-start_time)

        #display top 3 predictions
        idxs=np.argsort(predictions[0])[::-1][:3] #sort in descending highest as first

        for i,idx in enumerate(idxs):
            if i==0:
                text="Label:{}, p:{}".format(classes[idx],predictions[0][idx] * 100)
                cv2.putText(img,text,(5, 25),  cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, (0, 0, 255), 2)

        # display the output image

        #cv2.imshow("Image", img)
        #cv2.waitKey(0)
        return img
