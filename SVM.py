from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from PrepareData import PrepareData

class SVM():

    '''def SVCApplicationToValidation(self):
        #Instancia de clase para preparar cada uno de los datos
        prepare_training = PrepareData()
        prepare_training.ScaleDataToValidation("data.csv")


        #Creación de Instancia de SVM se scikit learn.
        modelo = svm.SVM()

        #Creación de modelo instanciado. 
        modelo.fit(prepare_training.training_data, prepare_training.classes)

        #Impresión de algunas características del model obtenido.
        print("Accurracy: ", accuracy_score(prepare_training.classes, modelo.predict(prepare_training.data)))
        print("\n")   
        print("Classification Report: \n",classification_report(prepare_training.classes, 
        modelo.predict(prepare_training.validation_data)),"\n") 

    '''

    def SVMApplicationToPlayer(self):
        #Instancia de clase para preparar cada uno de los datos
        prepare_training = PrepareData()
        prepare_training.ScaleDataToPlayer("data.csv")

        #Creación de Instancia de SVM se scikit learn.
        modelo = svm.SVM()

        #Creación de modelo instanciado. 
        modelo.fit(prepare_training.training_data, prepare_training.classes)

        #Impresión de algunas características del model obtenido.
        print("Classification Report: \n",classification_report(prepare_training.classes, 
            modelo.predict(prepare_training.player_data)),"\n") 

        return modelo.predict(prepare_training.player_data)
  
