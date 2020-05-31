#code that will print content to word file
#We need to install some libraries(word related addons) for achieving the objective

import docx
import cv2
import PIL 
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  #To avoid path conflicts

img=cv2.imread('license.jpg')
cv2.imshow('test image',img)
cv2.waitKey(0)

#get text from the image
text=pytesseract.image_to_string(img)
print(text)

cur_doc=docx.Document() #Create a document object
cur_doc.add_paragraph(text)
cur_doc.save('my_written_file.docx')

