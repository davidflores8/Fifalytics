from asyncio import windows_events
import PySimpleGUI as sg
from matplotlib.pyplot import Text
import os.path
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
layout =[
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(image_viewer_column),

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
        except:
            pass
window.close()