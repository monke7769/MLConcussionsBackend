# import all necessary packages for machine learning
# numpy to handle the returned result and convert into usable list format
import numpy as np
# need to be able to split up data into training and testing sets
from sklearn.model_selection import train_test_split
# training with linear regression model as data is continuous, not discrete
from sklearn.linear_model import LinearRegression
# python pandas package
# need pandas for dataframe and easy data manipulation
import pandas as pd

# Define the concussion_regression global variable
concussion_regression = None

# define the ConcussionRegression class
# we are using OOP here
class ConcussionRegression:
    # below are the separate functions to handle various events in the prediction
    # initConcussion will take the generated sample data from the CSV file
    # then it will clean data by removing all negative values
    def initConcussion(self):
        # load in the csv data
        concussion_data = pd.read_csv('concussion_recovery_data.csv')
        '''
        Categories in the CSV file: sex,age,ht,wt,smoke,alcohol,sleephrs,exercisehrs,hitbox,healtime
        sex is boolean, 1=male 0=female
        ht = height (cm)
        wt = weight (kg)
        smoke/alcohol are boolean, 1=yes 0=no
        sleephrs are per night
        exercisehrs are per week
        hitbox = size of object hit, in kg
        healtime is in days
        '''
        global cd
        # now variable cd has all the data
        cd = concussion_data
        categories = ['age', 'ht', 'wt', 'sleephrs', 'exercisehrs', 'hitbox', 'healtime']
        # clean up the data
        # for non-boolean categories, drop all negative values
        for cat in categories:
            cd.drop(cd[cd[cat] < 0].index, inplace=True)
    
    # runLinearRegression trains the model according to linear regression
    # the model will be trained to predict healtime based on the other categories
    def runLinearRegression(self):
        # making a linear regression model
        X = cd.drop('healtime', axis=1) # all categories except healtime (result)
        y = cd['healtime'] # healtime (the result)
        # split up data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        global lr
        # train the model
        lr = LinearRegression()
        lr.fit(X_train, y_train)
        
def predict(data):
    new_case = data.copy() # copy in the data from frontend
    '''
    format of the input:
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
    # sex converted to boolean and name doesn't matter
    new_case['sex'] = new_case['sex'].apply(lambda x: 1 if x == 'male' else 0)
    new_case.drop(['name'], axis=1, inplace=True)
    # predict time to heal
    # need to convert to list since numpy arrays are not directly serializable to JSON
    healtime = np.squeeze(lr.predict(new_case)).tolist() # use numpy and .tolist()
    # print(healtime)
    return healtime

def initConcussion():
    # initiate the concussion regression model
    # then run linear regression
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