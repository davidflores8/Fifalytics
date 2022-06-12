from cgi import print_arguments
from cgitb import text
import re
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
    #llama al metodo de la clase parseos para poder agarrar los datos de mejor forma
    print(ruta)
    print(texto)
    Atributos=psr.atributos(cadena2)
    #asignacion de los atributos en la primera linea (ritmo y regate)
    Ritmo=Atributos[0]
    regate=Atributos[1]
    regate=regate.replace("0R1","")
    tiro=Atributos[2]
    defensa=Atributos[3]
    defensa=defensa.replace("0F","")
    defensa=defensa.replace("0EF","") 
    pase=Atributos[4]
    fisico=Atributos[5]
    pase =int(pase)
    if int(pase) >100:
        pase=pase/10
    fisico =int(fisico)
    if int(fisico) >100:
        fisico=fisico/10
    Ritmo =int(Ritmo)
    if int(Ritmo) >100:
        Ritmo=Ritmo/10
    tiro =int(tiro)
    if int(tiro) >100:
        tiro=tiro/10
    regate =int(regate)
    if int(regate) >100:
        regate=regate/10
    defensa =int(defensa)
    if int(defensa) >100:
        defensa=defensa/10
    Ritmo=Ritmo.__round__()
    tiro=tiro.__round__()
    defensa=defensa.__round__()
    regate=regate.__round__()
    pase=pase.__round__()
    fisico=fisico.__round__()
    print("ritmo " , Ritmo)
    print("regate: ", regate)
    print("tiro " , tiro)
    print("defensa: ", defensa)
    print("pase " , pase)
    print("fisico ", fisico)
    #abrir archivo csv para poder escribir
    nombre=cadena.replace(".PNG","")
    b= open ("data.csv","a",newline="")    
    tupla=(nombre,Ritmo,regate,tiro,defensa,pase,fisico)
    escritor=csv.writer(b)
    escritor.writerow(tupla)
    b.close()
    #para mostrar la imagen lo siguiente
    #cv2.imshow("image: ", negro) 
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()    
f.close
print("lectura de datos terminada")
