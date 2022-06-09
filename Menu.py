from cgi import print_arguments
from cgitb import text
from tkinter import image_names
from turtle import bgcolor
import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Prestamo\AppData\Local\Programs\Tesseract-OCR\tesseract"
#ruta="./Fotos Proyecto Inteligentes/"
clahe=cv2.createCLAHE(clipLimit=3.5,tileGridSize=(10,10))

f = open("./imagenes.txt", "r")
print(pytesseract.get_languages(config=''))
for i in f:
    ruta=""
    cadena=str(i)
    cadena=cadena.replace("\n","")
    ruta="./Fotos Proyecto Inteligentes/"+cadena
    print(ruta)      
    image= cv2.imread(ruta)
    imageC=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    (thresh,negro)=cv2.threshold(imageC,127,255,cv2.THRESH_BINARY)
    #imageE=cv2.equalizeHist(negro)
    #imageD=clahe.apply(imageE)
    
    texto=pytesseract.image_to_string(image,lang="eng")
    a=open ("./lista.txt","a")
    a.write(str(texto).replace("\n",""))
    a.write("\n")
    a.close()

    #cv2.imshow("image: ", image) 
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()    
f.close
#cv2.imshow("image: ", imageD)
#cv2.waitKey(0)
#cv2.destroyAllWindows()