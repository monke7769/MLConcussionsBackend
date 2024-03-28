from flask import Flask, request, jsonify, Blueprint
import yfinance as yf
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from model.stockMLmodel import *

app = Flask(__name__)
stock_api = Blueprint('stock_api', __name__, url_prefix='/api/stock')

# Function to prepare your data and model
def prepare_data_and_model():
    sp500 = yf.Ticker("^GSPC")
    sp500 = sp500.history(period="max")
    sp500["Tomorrow"] = sp500["Close"].shift(-1)
    sp500["Target"] = (sp500["Tomorrow"] > sp500["Close"]).astype(int)
    sp500 = sp500.loc["1990-01-01":].dropna().copy()
    
    predictors = ["Close", "Volume", "Open", "High", "Low"]
    model = RandomForestClassifier(n_estimators=100, min_samples_split=100, random_state=1)
    
    # Assuming the last 100 rows are for testing, and the rest for training
    train = sp500.iloc[:-100]
    model.fit(train[predictors], train["Target"])
    
    return model, predictors, sp500

# Loading the model and predictors
model, predictors, sp500 = prepare_data_and_model()

@stock_api.route('/predict', methods=['POST'])
def predict():
    json_data = request.get_json(force=True)
    # Ensure you structure your data as a DataFrame with appropriate column names
    input_data = pd.DataFrame([json_data])
    prediction_proba = model.predict_proba(input_data[predictors])
    
    # Assuming that the positive class (1) is the second column of predict_proba
    proba_of_1 = prediction_proba[:, 1] * 100  # Convert to percentage
    return jsonify({'probability of increase': f"{proba_of_1[0]:.2f}%"})


if __name__ == '__main__':
    app.run(debug=True)







