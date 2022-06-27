from asyncio import windows_events
from re import MULTILINE
import PySimpleGUI as sg
from matplotlib.pyplot import Text
import os.path
import cv2
import pytesseract
import numpy as np
from Parseos import Parser  as psr
import PrepareData as PrepareData
import KNN as KNN
import RandomForest as RandomForest
import SVM as SVM
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Prestamo\AppData\Local\Programs\Tesseract-OCR\tesseract"

def agarradatos(cadena):
    image= cv2.imread(cadena)
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
    Atributos=psr.atributos(cadena2)
    salida=""
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
    
    salida="Pace: ",Ritmo, "Dribbling: ",regate,"Shooting: ",tiro,"Defending: ",defensa,"Passing: ",pase," Physicality: ",fisico
    print(salida)
    Jugador = ["-",Ritmo, regate, tiro, defensa, pase, fisico,"Delantero"]
    print("pl",Jugador)
    #knn
    knn_classificator = KNN()
    print("hola2  ")
    knn_result = knn_classificator.KNNAplicationToPlayer(Jugador)
    print("holaknn")
    '''#svm
    svm_classificator = SVM()
    svm_result = svm_classificator.SVMApplicationToPlayer()
    print("hola svm")
    #random
    random_forest_classificator = RandomForest()
    random_forest_result = random_forest_classificator.RandomForestApplicationToPlayer()
    print("hola rf")
    '''
    return salida

file_list_column=[
    [
        sg.Text("Image Folder"),
        sg.In(size=(25,1),enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[],enable_events=True,size=(40,20),
            key="-FILE LIST-"
        )
    ],
]
image_viewer_column =[

    [sg.Text("Elige una foto de las de la izquierda:")],
    [sg.Text(size=(40,1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]
STATS_viewer_column =[

    [sg.Text("lAS ESTADISTICAS DEL JUGADOR SON: ")],
    [sg.Text(size=(25,20), key="-TEXTO-")],
]
layout =[
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),
        sg.VSeperator(),
        sg.Column(STATS_viewer_column)
    ]
]
window = sg.Window("Image Viewe", layout)

while True:
    event, values = window.read()
    if event=="Exit" or event==sg.WIN_CLOSED:
        break
    if event== "-FOLDER-":
        folder=values["-FOLDER-"]
        try:
            file_list=os.listdir(folder)
        except:
            file_list=[]
        fnames=[
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder,f))
            and f.lower().endswith((".png"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event =="-FILE LIST-":
        try:
            filename = os.path.join(
                values["-FOLDER-"], values ["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename=filename)
            window['-TEXTO-'].update(agarradatos(filename))            
            #
        except:
            pass
window.close()
