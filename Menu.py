from cgi import print_arguments
from cgitb import text
from turtle import bgcolor
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Prestamo\AppData\Local\Programs\Tesseract-OCR\tesseract"
#ruta="./Fotos Proyecto Inteligentes/"
clahe=cv2.createCLAHE(clipLimit=0.5,tileGridSize=(20,20))

f = open("./imagenes.txt", "r")
for i in f:
    ruta=""
    cadena=str(i)
    cadena=cadena.replace("\n","")
    ruta="./Fotos Proyecto Inteligentes/"+cadena
    print(ruta)
    image= cv2.imread(ruta)
    imageC=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    imageE=cv2.equalizeHist(imageC)
    imageD=clahe.apply(imageE)
    texto=pytesseract.image_to_string(imageD)
    print (texto)    
    cv2.imshow("image: ", imageD)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    
f.close



#cv2.imshow("image: ", imageD)
#cv2.waitKey(0)
#cv2.destroyAllWindows()