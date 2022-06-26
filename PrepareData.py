from asyncio.windows_events import NULL
from random import random
import numpy
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import pandas as pd  


class PrepareData():

    datos = NULL
    training_data = NULL
    validation_data = NULL
    player_data = NULL
    classes = NULL


    def getDatos(self):
        return self.datos
    
    def ScaleDataToValidation(self, ruta):
        #Preparando los datos de los jugadores que queremos predecir.
        jugadores = pd.read_csv("./"+ruta)
        
        self.datos=jugadores
        #Instanciamos la clase LabelEnconder para clasificar las posiciones de los jugadores.
        le_clase = LabelEncoder()
        
        #Dentro del dataset creamos la columna clase donde guardamos las clases debidamente codificadas.
        jugadores["clase"] = le_clase.fit_transform(jugadores["Position"])
        
        #Debido a que ya creamos la clase, eliminamos la posición y el nombre del jugador, ya que es irrelevante al
        #estudio que se realizará. 
        jugadores_n = jugadores.drop(['Position', 'Name'], axis="columns")
        
        #Separamos en una variable las clases de los jugadores para entrenar nuestro modelo.
        clases = jugadores_n["clase"]
        
        #Una vez obtenida la clase, eliminamos esa columna del dataet, para dejar separamos los datos de los
        #atributos de nuestros jugadores.
        data = jugadores_n.drop('clase', axis = 'columns')
        
        #Escalamos los datos en base al máximo y al mínimo, para fácil procesamiento por nuestro modelo. 
        datos = preprocessing.MinMaxScaler().fit_transform(data)
        #Datos listos para procesar

        self.player_data = datos[0]
        datos = numpy.delete(datos,0,0)
        
        validacion = datos
        datos_finales = datos

        for i in range (304,-1,-1):
            if(i>98):
                validacion = numpy.delete(validacion,i,0)
            elif(i<=98):
                datos_finales = numpy.delete(datos_finales,i,0)
        print("El dato a predecir: ",self.player_data)
        print("Size de validacion: ",validacion.shape)
        print("Size de final: ",datos_finales.shape)
        numpy.savetxt('validation.csv', validacion, delimiter=',')
        numpy.savetxt('training.csv', datos_finales, delimiter=',')

        self.datos = datos
        self.validation_data = validacion
        self.training_data = datos_finales
        self.classes = clases

        
    def ScaleDataToPlayer(self, ruta):
        #Preparando los datos de los jugadores que queremos predecir.
        jugadores = pd.read_csv("./"+ruta)
        
        self.datos=jugadores

        #Codigo para insertar jugadores en el df
        '''jugadores.loc[-1] = ['DAVIDE',99, 99, 99, 99, 99, 99,'Delantero']  # adding a row
        jugadores.index = jugadores.index + 1  # shifting index
        jugadores= jugadores.sort_index()''' 

        print(jugadores)
        #Instanciamos la clase LabelEnconder para clasificar las posiciones de los jugadores.
        le_clase = LabelEncoder()
        
        #Dentro del dataset creamos la columna clase donde guardamos las clases debidamente codificadas.
        jugadores["clase"] = le_clase.fit_transform(jugadores["Position"])
        
        #Debido a que ya creamos la clase, eliminamos la posición y el nombre del jugador, ya que es irrelevante al
        #estudio que se realizará. 
        jugadores_n = jugadores.drop(['Position', 'Name'], axis="columns")
        
        #Separamos en una variable las clases de los jugadores para entrenar nuestro modelo.
        clases = jugadores_n["clase"]
        
        #Una vez obtenida la clase, eliminamos esa columna del dataet, para dejar separamos los datos de los
        #atributos de nuestros jugadores.
        data = jugadores_n.drop('clase', axis = 'columns')
        
        #Escalamos los datos en base al máximo y al mínimo, para fácil procesamiento por nuestro modelo. 
        datos = preprocessing.MinMaxScaler().fit_transform(data)
        #Datos listos para procesar

        self.player_data = datos[0]
        datos = numpy.delete(datos,0,0)
        self.datos = datos
        self.classes = clases

        #Guardar el training set en el archivo Training.csv
        #numpy.savetxt('Training.csv', datos, delimiter=',')
        
p = PrepareData()
p.ScaleDataToPlayer("data.csv")