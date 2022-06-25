from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
import pandas as pd    


class PrepareData():

    
    def ScaleData(self, ruta):
        #Preparando los datos de los jugadores que queremos predecir.
        jugadores = pd.read_csv("./"+ruta)
        
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
        return datos
    
    def getClasses(self, ruta):
        #Preparando los datos de los jugadores que queremos predecir.
        jugadores = pd.read_csv("./"+ruta)
        
        #Instanciamos la clase LabelEnconder para clasificar las posiciones de los jugadores.
        le_clase = LabelEncoder()
        
        #Dentro del dataset creamos la columna clase donde guardamos las clases debidamente codificadas.
        jugadores["clase"] = le_clase.fit_transform(jugadores["Position"])
        
        #Debido a que ya creamos la clase, eliminamos la posición y el nombre del jugador, ya que es irrelevante al
        #estudio que se realizará. 
        jugadores_n = jugadores.drop(['Position', 'Name'], axis="columns")
        
        #Separamos en una variable las clases de los jugadores para entrenar nuestro modelo.
        clases = jugadores_n["clase"]

        return clases