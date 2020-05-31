#code that will print content to word file
#We need to install some libraries(word related addons) for achieving the objective
#Extra libraries need to be installed in addition to opencv are python-docx,pytessaract,pdf2image,PIL

import docx
import cv2
import pytesseract
import argparse
from PyPDF2 import PdfFileReader
import pdf2image
import os
import imutils

#To avoid path conflicts with tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config=r'C:\Program Files\Tesseract-OCR\tessdata'  

#create argument parser with pdf file as input
ap=argparse.ArgumentParser()
ap.add_argument("-p","--pdf",required=True,help="path to pdf file")
args=vars(ap.parse_args())

#use the path from argumment parser for pdf file
#read pdf and find the number of pages
cur_pdf_path=args["pdf"]
cur_pdf = PdfFileReader(open(cur_pdf_path,'rb'))
num_pages=cur_pdf.getNumPages()
print(num_pages)

#store each page of pdf as array
#Save each page of pdf as image
pages=pdf2image.convert_from_path(cur_pdf_path,num_pages)
#pages=pages[:10]
#print(len(pages))
image_index=1 #required for saving each pdf page to image



for page in pages:
    filename='page'+str(image_index)+'.jpg'
    page.save(filename,'JPEG')
    image_index=image_index+1


cur_doc=docx.Document() #Create a document object
#parse through each image
for i in range(1,num_pages+1):
    page_img_name='page'+str(i)+'.jpg'
    img=cv2.imread(page_img_name)
    #img=imutils.resize(img,width=640,height=640)
    cv2.imshow('test image',img)
    cv2.waitKey(0)

    #Extract text from images
    text=pytesseract.image_to_string(img)
    #print(text)

    #Save the text in word document
    cur_doc.add_paragraph(text)
    cur_doc.save('my_written_file.docx')

    #Remove the image files
    os.remove(page_img_name)


