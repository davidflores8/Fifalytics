from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from PrepareData import PrepareData

class SVC():

    def SVCApplicationToValidation(self):
        #Instancia de clase para preparar cada uno de los datos
        prepare_training = PrepareData()
        prepare_training.ScaleDataToValidation()


        #Creación de Instancia de SVM se scikit learn.
        modelo = svm.SVC()

        #Creación de modelo instanciado. 
        modelo.fit(prepare_training.training_data, prepare_training.classes)

        #Impresión de algunas características del model obtenido.
        print("Accurracy: ", accuracy_score(prepare_training.classes, modelo.predict(prepare_training.data)))
        print("\n")   
        print("Classification Report: \n",classification_report(prepare_training.classes, 
        modelo.predict(prepare_training.validation_data)),"\n") 

    def SVCApplicationToPlayer(self):
        #Instancia de clase para preparar cada uno de los datos
        prepare_training = PrepareData()
        prepare_training.ScaleDataToPlayer()

        #Creación de Instancia de SVM se scikit learn.
        modelo = svm.SVC()

        #Creación de modelo instanciado. 
        modelo.fit(prepare_training.training_data, prepare_training.classes)

        #Impresión de algunas características del model obtenido.
        print("Classification Report: \n",classification_report(prepare_training.classes, 
            modelo.predict(prepare_training.player_data)),"\n") 
  

svc_instance = SVC()
svc_instance.SVCApplicationToValidation()