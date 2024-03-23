'''
Note: this data generation code came from ChatGPT
'''

import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 1000

# Generate data
data = {
    'Gender': np.random.choice([0, 1], size=num_samples),
    'Age': np.random.normal(loc=30, scale=10, size=num_samples),
    'Height': np.random.normal(loc=170, scale=10, size=num_samples),
    'Weight': np.random.normal(loc=70, scale=10, size=num_samples),
    'Smoke': np.random.choice([0, 1], size=num_samples),
    'Alcohol': np.random.choice([0, 1], size=num_samples),
    'Sleep_Hours': np.random.normal(loc=7, scale=1, size=num_samples),
    'Exercise_Hours': np.random.normal(loc=3, scale=2, size=num_samples),  # New feature
    'Object_Hit_Weight': np.random.normal(loc=1.0, scale=0.3, size=num_samples)  # New feature
}

# Define function to calculate recovery time
def calculate_recovery_time(row):
    age_effect = row['Age'] / 10  # Older individuals may take longer to heal
    bad_habits_effect = row['Smoke'] * 2 + row['Alcohol'] * 1.5  # Smoking and alcohol may delay healing
    sleep_effect = (8 - row['Sleep_Hours']) / 2  # Less sleep may delay healing
    exercise_effect = row['Exercise_Hours'] / 3  # Exercise may promote faster healing
    object_weight_effect = row['Object_Hit_Weight'] * 2  # Heavier object may prolong healing

    # Combine effects and add some random noise
    recovery_time = 35 + age_effect + bad_habits_effect + sleep_effect - exercise_effect + object_weight_effect + np.random.normal(loc=0, scale=3)
    return max(recovery_time, 0)  # Ensure recovery time is non-negative

# Apply the function to generate recovery time
data['Time_to_Heal'] = [calculate_recovery_time(row) for _, row in pd.DataFrame(data).iterrows()]

# Create DataFrame
df = pd.DataFrame(data)

# Round Age, Height, Weight, Sleep_Hours, Exercise_Hours, Object_Hit_Weight, and Time_to_Heal to 2 decimal places
df = df.round({'Age': 2, 'Height': 2, 'Weight': 2, 'Sleep_Hours': 2, 'Exercise_Hours': 2, 'Object_Hit_Weight': 2, 'Time_to_Heal': 2})

# Save DataFrame to CSV file
df.to_csv('concussion_recovery_data.csv', index=False)

print("CSV file saved successfully.")