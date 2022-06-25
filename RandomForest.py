from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from PrepareData import PrepareData
from sklearn import tree
import matplotlib.pyplot as plt

class RandomForest():


    def RandomForestApplication(self):
       

        prepare_training = PrepareData()
        training_data = prepare_training.ScaleData("Jugadores.csv")
        training_classes = prepare_training.getClasses("Jugadores.csv")

        prepare_validation= PrepareData()
        validation_data = prepare_validation.ScaleData("validation_set.csv")
        validation_classes = prepare_validation.getClasses("validation_set.csv")

        Bosque = RandomForestClassifier(n_estimators=6, max_depth=4)
        Bosque.fit(training_data, training_classes)
        print("Accurracy: ", accuracy_score(validation_classes, Bosque.predict(validation_data)))
        print("\n")   
        print("Classification Report: \n",classification_report(validation_classes, 
        Bosque.predict(validation_data)),"\n") 

        #Predice si Mbappe 
        #print(Bosque.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))

        for arbol in Bosque.estimators_:
            tree.plot_tree(arbol, feature_names=prepare_validation.getDatos().columns[:-1])
            plt.show()
    

        

r = RandomForest()
r.RandomForestApplication()