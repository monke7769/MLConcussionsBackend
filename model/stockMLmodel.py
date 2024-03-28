import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
import pandas as pd

sp500 = yf.Ticker("^GSPC") #enables us to download for a single stock. GSPC is the S&P500 index
sp500 = sp500.history(period="max") # Query the historical prices. Passing period = max which querys data even from the beginning when the index was created
sp500.index #Display index; THE DATE COLUMN
sp500.plot.line(y="Close", use_index=True) # creating a chart in which the y-axis is the closing price and the x-axis is the date
del sp500["Dividends"]
del sp500["Stock Splits"] # deleting unnecessary columns in data. Data cleanup
sp500["Tomorrow"]= sp500["Close"].shift(-1) # Setting the new tomorrow column equal to the close column of the next days data. Pandas shift method. 
sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int) # returns a boolean (1 or 0) saying if tomorrow is greater then todays price
sp500 = sp500.loc["1990-01-01":].copy() #pandas LOC method, basically saying only use data where the index is at least 1990-01-01

from sklearn.ensemble import RandomForestClassifier #random forest classifier trains multiple decision trees based of many randomized parameters then taking the average of those decision trees. 
model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1) # n_estimators = # of decision trees we want to train, random_state = if we run the same model twice the random numbers generated will be the same.
train = sp500.iloc[:-100] #iloc stops dataleakage from the future into the model
test = sp500.iloc[-100:]
predictors = ["Close", "Volume", "Open", "High", "Low"] #a list of all the parameters in our dataset we want to use to help predict targer
#cant use target or tomorrow column because then the model knows the future. Not a real world application. INSIDER TRADING?
model.fit(train[predictors], train["Target"]) #train the predictors to attempt to predict the Target column

preds = model.predict(test[predictors])# generating prediction and passing our predictors test set.
#displays as a numpy array so hard to work with

preds = pd.Series(preds, index=test.index)
#formatted that array to align with the test index. 
precision_score(test["Target"], preds)

combined = pd.concat([test["Target"], preds], axis=1) #concatinating the actual and predicted value
combined.plot()

def predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict(test[predictors])
    preds = pd.Series(preds, index=test.index, name="Predictions")
    combined = pd.concat([test["Target"], preds], axis=1)
    return combined

def backtest(data, model, predictors, start=2500, step=250): #start: taking 10 yrs of data. Trading yr is typically 250 days. 
    #take the 1st 12 yrs of data to predict 13th yr and so on
    all_predictions = []

    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i+step)].copy()
        predictions = predict(train, test, predictors, model)
        all_predictions.append(predictions)
    
    return pd.concat(all_predictions)

predictions = backtest(sp500, model, predictors)
predictions["Predictions"].value_counts() #value counts counts how many times each prediction was made
#predicted market would go down at 3522 days
#predicted market would go up at 2602 days

precision_score(predictions["Target"], predictions["Predictions"])

predictions["Target"].value_counts() / predictions.shape[0]
# actual percentage of the market going up or going down
