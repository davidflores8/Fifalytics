from cgi import print_arguments
from cgitb import text
from tkinter import image_names
import pandas as pd
import csv 
from turtle import bgcolor
import cv2
import numpy as np
import pytesseract
from Parseos import Parser  as psr
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Prestamo\AppData\Local\Programs\Tesseract-OCR\tesseract"
clahe=cv2.createCLAHE(clipLimit=3.5,tileGridSize=(10,10))
f = open("./imagenes.txt", "r")
print(pytesseract.get_languages(config=''))
for i in f:
    ruta=""
    cadena=str(i)
    cadena=cadena.replace("\n","")
    ruta="./Fotos Proyecto Inteligentes/"+cadena
    #lee imagen de la ruta, en base a el archivo de imagenes      
    image= cv2.imread(ruta)
    #de color a gris
    imageC=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    #de gris a blanco y negro
    (thresh,negro)=cv2.threshold(imageC,127,255,cv2.THRESH_BINARY)
    #recorta la imagen
    negro=negro [275:390,30:260]
    #de blanco y negro a negro y blanco
    negro =255-negro
    #proceso de dilatar las letras (segun, no note mucho cambio)
    kernel = np.ones((1, 1), 'uint8')
    negro= cv2.dilate(negro,kernel,iterations=1)
    #pasa de la imagen a texto
    texto=pytesseract.image_to_string(negro,lang="eng")
    #quitar espacios
    cadena2= str(texto).replace(" ","")
    cadena2= cadena2.replace("\n\n","")
    #llama al metodo de la clase parseos para poder agarrar los datos de mejor forma
    print(ruta)
    print(texto)
    Atributos=psr.atributos(cadena2)
    #asignacion de los atributos en la primera linea (ritmo y regate)
    Ritmo=Atributos[0]
    regate=Atributos[1]
    
    print("ritmo " , Ritmo)
    print("regate: ", regate)
    #abrir archivo csv para poder escribir

    b= open ("data.csv","a",newline="")    
    tupla=(Ritmo,regate)
    escritor=csv.writer(b)
    escritor.writerow(tupla)
    b.close()
    #para mostrar la imagen lo siguiente
    #cv2.imshow("image: ", negro) 
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()    
f.close
print("termino")
