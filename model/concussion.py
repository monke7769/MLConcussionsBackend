import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
import pandas as pd

# Define the Concussion Regression global variable
concussion_regression = None

# define the concussionregression class
class ConcussionRegression:
    def __init__(self): # initialize variables
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
        global cd
        # now cd has all the data
        cd = concussion_data
        categories = ['age', 'ht', 'wt', 'sleephrs', 'exercisehrs', 'hitbox', 'healtime']
        # clean up the data
        # for non-boolean categories, drop all negative values
        for cat in categories:
            cd.drop(cd[cd[cat] < 0].index, inplace=True)
    
    def runLinearRegression(self):
        # making a linear regression model :exploding_face:
        X = cd.drop('healtime', axis=1)
        y = cd['healtime']
        # split up data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        global lr
        # train model
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        
def predict(data):
    new_case = data.copy() # copy in the data from frontend
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
    # convert frontend data to usable format
    # sex is boolean, name doesn't matter
    new_case['sex'] = new_case['sex'].apply(lambda x: 1 if x == 'male' else 0)
    new_case.drop(['name'], axis=1, inplace=True)
    # predict time to heal
    # need to convert to list since "numpy arrays are not directly serializable"
    healtime = np.squeeze(lr.predict(new_case)).tolist()
    print(healtime)
    return healtime

def initConcussion():
    # initiate the concussion regression model
    global concussion_regression
    concussion_regression = ConcussionRegression()
    concussion_regression.initConcussion()
    concussion_regression.runLinearRegression()
    
# test the model
if __name__ == "__main__":
    # initialize concussion model
    initConcussion()
    # test data on partner
    patient_data = pd.DataFrame({
        'name': ['Andrew Kim'],
        'sex': ['male'],
        'age': [16],
        'ht': [180],
        'wt': [73],
        'smoke': [0],
        'alcohol': [1],
        'sleephrs': [8.5],
        'exercisehrs': [5.5],
        'hitbox': [0.28],
    })
    print(predict(patient_data))