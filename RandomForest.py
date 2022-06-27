from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from PrepareData import PrepareData
from sklearn import tree
import matplotlib.pyplot as plt

class RandomForest():


    '''def RandomForestApplicationToValidation(self):
       

        prepare_training = PrepareData()
        prepare_training.ScaleDataToValidation("data.csv")

        Bosque = RandomForestClassifier(n_estimators=6, max_depth=4)
        Bosque.fit(prepare_training.training_data, prepare_training.classes)

        print("Accurracy: ", accuracy_score(prepare_training.classes, Bosque.predict(prepare_training.validation_data)))
        print("\n")   
        print("Classification Report: \n",classification_report(prepare_training.classes, 
        Bosque.predict(prepare_training.validation_data)),"\n") 

        #Predice si Mbappe 
        #print(Bosque.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))

        for arbol in Bosque.estimators_:
            tree.plot_tree(arbol, feature_names=prepare_training.getDatos().columns[:-1])
            plt.show()
    '''
    
    def RandomForestApplicationToPlayer(self):
       

        prepare_training = PrepareData()
        prepare_training.ScaleDataToPlayer("data.csv")

        Bosque = RandomForestClassifier(n_estimators=6, max_depth=4)
        Bosque.fit(prepare_training.training_data, prepare_training.classes)
 
        print("Classification Report: \n",classification_report(prepare_training.classes, 
        Bosque.predict(prepare_training.player_data)),"\n") 

        

        #Predice si Mbappe 
        #print(Bosque.predict([[1,1,0.89552239,0.17741935,0.70731707,0.83333333]]))

        '''for arbol in Bosque.estimators_:
            tree.plot_tree(arbol, feature_names=prepare_training.getDatos().columns[:-1])
            plt.show()'''
        
        return Bosque.predict(prepare_training.player_data)
        
