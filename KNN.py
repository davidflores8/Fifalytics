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

    def KNNApplicationToPlayer(self, Jugador):
        
        prepare_training = PrepareData()
        prepare_training.ScaleDataToPlayer("data.csv", Jugador)

        knn = KNeighborsClassifier(n_neighbors=3)
        knn.fit(prepare_training.training_data, prepare_training.classes)

        print("Classification Report: \n",classification_report(prepare_training.classes, 
        knn.predict(prepare_training.player_data)),"\n") 


        return knn.predict(prepare_training.player)
    
    
