from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from PrepareData import PrepareData
import matplotlib.pyplot as plt
import seaborn as sb

class KNN():


    '''def KNNApplicationToValidation(self):
        
        prepare_training = PrepareData()
        prepare_training.ScaleDataToValidation("data.csv")

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(prepare_training.training_data, prepare_training.classes)
        print("Accurracy: ", accuracy_score(prepare_training.classes, knn.predict(prepare_training.training_data)))
        print("\n")   
        print("Classification Report: \n",classification_report(prepare_training.classes, 
        knn.predict(prepare_training.validation_data)),"\n") 
        
    '''

    def KNNApplicationToPlayer(self, player):
        
        prepare_training = PrepareData()
        prepare_training.ScaleDataToPlayer("data.csv",player)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(prepare_training.datos, prepare_training.classes)

        print("Classification Report: \n",classification_report(prepare_training.classes, 
        knn.predict(prepare_training.datos)),"\n") 

        print(prepare_training.player_data)
        print(knn.predict(prepare_training.player_data))

        #print("Posicion de Mbappe: ",knn.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))
    
#Jugador = ["Mbappe",97,92,88,36,80,77,"Delantero"]    
#knn_classificator = KNN()
#knn_result = knn_classificator.KNNApplicationToPlayer(Jugador)

    
