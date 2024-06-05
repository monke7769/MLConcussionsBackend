# Backend Flask Server for Concussions

run the flask server on 127.0.0.1:8086 through 
python main.py
in the terminal.

main.py file sets up APIs and registers all URIs. This includes Titanic API (Titanic sinking survival simulation), Recovery API (suggestions for recovery), and Concussion API (concussion recovery time predictor).

all .py files in the /api folder handle setting up of API Blueprints and requests from user server (127.0.0.1:4000 if running Concussions Frontend locally)

algorithmic code and ML data cleaning/predictions are all found within /model folder. concussion.py, recovery.py, and titanic.py are the main features in this project and unique to the developers.

# recovery.py (not ML)

1. Severity Mapping: Symptoms are mapped to severity levels such as 'None', 'Mild', 'Moderate', and 'Severe'.

2. Recovery Suggestions: Two sets of recovery suggestions are defined: suggestions for typical cases and extremesuggestions for severe cases.

3. Score Calculation: Each symptom's severity is weighted based on its severity level and summed up to calculate a total score.

4. Thresholds: Thresholds are defined for triggering recovery suggestions based on the calculated score.

5. Final Suggestions: Based on the total score, severity counts, and predefined thresholds, appropriate recovery suggestions are generated. If the score exceeds extreme thresholds, extreme recovery suggestions are provided.

6. Output Formatting: Returns a list containing the total score and a list of recovery suggestions.

# concussion.py (Linear Regression ML)

Libraries:
- numpy for handling numerical data efficiently.
- pandas for data manipulation and analysis.
- train_test_split from sklearn.model_selection to split data into training and testing sets.
- LinearRegression from sklearn.linear_model for training a linear regression model.

ConcussionRegression Class:
- initConcussion: Loads the concussion recovery data from a CSV file, removes negative values, and stores it in a DataFrame.
- runLinearRegression: Trains a linear regression model to predict the healing time based on the available data.

Predict Function:
- predict: Takes input data, preprocesses it, and predicts the healing time using the trained linear regression model.
Initialization and Testing:
- initConcussion: Initializes the concussion regression model and trains it.
- Test data is provided in the file for a hypothetical patient named Andrew Kim (who is Frontend developer of this project), and his healing time is predicted based on his information.
