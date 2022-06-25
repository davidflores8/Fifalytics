from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from asyncio.windows_events import NULL
from sklearn import preprocessing
from sklearn.metrics import classification_report
import pandas as pd


class KNN():

    datos = NULL
    clases = NULL

    datos_validados = NULL
    clases_validadas = NULL
    
    def ScaleData(self):
        jugadores = pd.read_csv("./Jugadores.csv")
        le_clase = LabelEncoder()
        jugadores["clase"] = le_clase.fit_transform(jugadores["Position"])
        jugadores_n = jugadores.drop(['Position', 'Name'], axis="columns")
        clases = jugadores_n["clase"]
        data = jugadores_n.drop('clase', axis = 'columns')
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


    def KNNApplication(self):
        self.ScaleData()   
        self.ScaleValidationData()

        Bosque = KNeighborsClassifier(n_neighbors=3)
        Bosque.fit(self.datos, self.clases)
        print("Accurracy: ", accuracy_score(self.clases_validadas, Bosque.predict(self.datos_validados)))
        print("\n")   
        print("Classification Report: \n",classification_report(self.clases_validadas,
        Bosque.predict(self.datos_validados)),"\n") 

        #Predice si Mbappe 
        #print(Bosque.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))


        

k= KNN()
k.KNNApplication()