import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

concussion_regression = None

class ConcussionRegression: # using OOP
    def __init__(self):
        self.dt = None
        self.logreg = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.encoder = None
        
    def initConcussion(self):
        # load in the csv data
        concussion_data = pd.read_csv('concussion_recovery_data.csv')
        global td
        self.td = concussion_data
        categories = ['age','ht','wt','sleephrs','exercisehrs','hitbox','healtime']
        # manage the data
        # for non-boolean categories, drop all negative values
        for cat in categories:
            self.td.drop(self.td[self.td[cat] < 0].index, inplace=True)
            
    def runDecisionTree(self):
        # want to train to predict how long it takes to heal
        self.X = self.td.drop('healtime', axis=1)
        self.y = self.td['healtime']
        # split up the dataset to train/test
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=42)
        dt = DecisionTreeClassifier()
        dt.fit(self.X_train, self.y_train)
        self.dt = dt
    
    def runLogisticRegression(self, X, y):
                self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
                self.logreg = LogisticRegression()
                self.logreg.fit(self.X_train, self.y_train)
                
    def testModel(self):
        # test the model
        y_pred = self.logreg.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        print('Logistic Regression Accuracy: {:.2%}'.format(accuracy))  
        
def predict(self,data):
        case = data.get("case")
        new_case = {
            'name': case.get('name'),
            'sex': case.get('sex'),
            'ht': case.get('ht'),
            'wt': case.get('wt'),
            'smoke': case.get('smoke'),
            'alcohol': case.get('alcohol'),
            'sleephrs': case.get('sleephrs'),
            'exercisehrs': case.get('exercisehrs'),
            'hitbox': case.get('hitbox'),
        }
        new_case['sex'] = new_case['sex'].apply(lambda x: 1 if x == 'male' else 0)
        new_case['smoke'] = new_case['smoke'].apply(lambda x: 1 if x == 'yes' else 0)
        new_case['alcohol'] = new_case['alcohol'].apply(lambda x: 1 if x == 'yes' else 0)
        new_case.drop(['name'], axis=1, inplace=True)
        # predict time to heal
        healtime = np.squeeze(self.logreg.predict_proba(new_case))
        return healtime
def initConcussion():
    global concussion_regression
    concussion_regression = ConcussionRegression()
    concussion_regression.initConcussion()
    X = concussion_regression.td.drop('healtime', axis=1)
    y = concussion_regression.td['healtime']
    concussion_regression.runLogisticRegression(X, y)
    
# test the model
if __name__ == "__main__":
    initConcussion()
    patient_data = pd.DataFrame({
        'name': ['Andrew Kim'],
        'sex': ['male'],
        'ht': [180],
        'wt': [60],
        'smoke': [0],
        'alcohol': [0],
        'sleephrs': [8.5],
        'exercisehrs': [5.5],
        'hitbox': [0.28],
    })
    print(concussion_regression.predict(patient_data))