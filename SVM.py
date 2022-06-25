from asyncio.windows_events import NULL
from sklearn import svm
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pandas as pd

class SVC():

    datos = NULL
    clases = NULL

    datos_validados = NULL
    clases_validadas = NULL


    def ScaleData(self):
        #Preparando los datos de los jugadores que queremos predecir.
        jugadores = pd.read_csv("./Jugadores.csv")
        
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
        self.datos = datos
        self.clases = clases

    def ScaleValidationData(self):
        jugadores = pd.read_csv("./validation_set.csv")
        le_clase = LabelEncoder()
        jugadores["clase"] = le_clase.fit_transform(jugadores["Position"])
        jugadores_n = jugadores.drop(['Position', 'Name'], axis="columns")
        clases = jugadores_n["clase"]
        data = jugadores_n.drop('clase', axis = 'columns')
        datos = preprocessing.MinMaxScaler().fit_transform(data)
        #Datos listos para procesar
        self.datos_validados = datos
        self.clases_validadas = clases

    def SVCApplication(self):
        self.ScaleData()   
        self.ScaleValidationData()

        m = svm.SVC()
        m.fit(self.datos, self.clases)
        print("Accurracy: ", accuracy_score(self.clases_validadas, m.predict(self.datos_validados)))
        print("\n")   
        print("Classification Report: \n",classification_report(self.clases_validadas,
        m.predict(self.datos_validados)),"\n") 

        #Predice la clase a la que pertenece Mbappe 
        #print(m.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))
  

s = SVC()
s.SVCApplication()