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
        df = pd.read_csv('concussion_recovery_data.csv')
        # print(df)
        row = df.loc[0]
        print(row)
concussion_regression = ConcussionRegression()
concussion_regression.initConcussion()