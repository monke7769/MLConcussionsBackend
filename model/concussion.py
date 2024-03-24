import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd

class ConcussionRegression:
    def __init__(self):
        self.dt = None
        self.lr = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.td = None
        
    def initConcussion(self):
        # load in the csv data
        concussion_data = pd.read_csv('concussion_recovery_data.csv')
        self.td = concussion_data
        categories = ['age', 'ht', 'wt', 'sleephrs', 'exercisehrs', 'hitbox', 'healtime']
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
    
    def runLinearRegression(self, X, y):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        global lr
        lr = LinearRegression()
        lr.fit(self.X_train, self.y_train)

    def testModel(self):
        # Test the linear regression model
        y_pred = self.lr.predict(self.X_test)
        mse = mean_squared_error(self.y_test, y_pred)
        print('Mean Squared Error (MSE): {:.2f}'.format(mse)) 
        
def predict(data):
    new_case = data.copy()
    '''
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
    '''
    new_case['sex'] = new_case['sex'].apply(lambda x: 1 if x == 'male' else 0)
    new_case.drop(['name'], axis=1, inplace=True)
    # predict time to heal
    # healtime = lr.predict(np.array([list(new_case.values())]))
    healtime = np.squeeze(lr.predict(new_case))
    # print(healtime)
    return healtime

def initConcussion():
    global concussion_regression
    concussion_regression = ConcussionRegression()
    concussion_regression.initConcussion()
    X = concussion_regression.td.drop('healtime', axis=1)
    y = concussion_regression.td['healtime']
    concussion_regression.runLinearRegression(X, y)
    
# test the model
if __name__ == "__main__":
    initConcussion()
    patient_data = pd.DataFrame({
        'name': ['Andrew Kim'],
        'sex': ['male'],
        'age': [16],
        'ht': [180],
        'wt': [60],
        'smoke': [0],
        'alcohol': [1],
        'sleephrs': [8.5],
        'exercisehrs': [5.5],
        'hitbox': [0.28],
    })
    print(predict(patient_data))