from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from PrepareData import PrepareData

class SVC():

    def SVCApplication(self):
        prepare_training = PrepareData()
        training_data = prepare_training.ScaleData("Jugadores.csv")
        training_classes = prepare_training.getClasses("Jugadores.csv")

        prepare_validation= PrepareData()
        validation_data = prepare_validation.ScaleData("validation_set.csv")
        validation_classes = prepare_validation.getClasses("validation_set.csv")

        m = svm.SVC()
        m.fit(training_data, training_classes)

        print("Accurracy: ", accuracy_score(validation_classes, m.predict(validation_data)))
        print("\n")   
        print("Classification Report: \n",classification_report(validation_classes, 
            m.predict(validation_data)),"\n") 

        #Predice la clase a la que pertenece Mbappe 
        #print(m.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))
  

s = SVC()
s.SVCApplication()