#Code to run all image files ,classify them and save them
import cv2
import os
import sys
import subprocess
import sam_caffe
def load_images_from_folder(folder):
    images = []
    image_names=[]
    for filename in os.listdir(folder):
        #img = cv2.imread(os.path.join(folder,filename))
        #if img is not None:
            #images.append(img)
        absolute_file_name=os.path.join(folder,filename)
        image_names.append(absolute_file_name)
    return image_names

Folder_path='D:\Vision_Challenge\Deep_learning\Image_Classification\images'
image_names=load_images_from_folder(Folder_path)

#print(image_names)

for name in image_names:
    img=sam_caffe.main(name)
    if img is None:
        print('Not getting output')
    else:
        cv2.imshow('current_image',img)
        cv2.waitKey(0)

