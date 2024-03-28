'''
Note: this data generation code came from ChatGPT
'''

import numpy as np
import pandas as pd

# random seed for reproducibility
np.random.seed(42)

# sample size
num_samples = 1000

# generate data
data = {
    'sex': np.random.choice([0, 1], size=num_samples),
    'age': np.random.normal(loc=30, scale=10, size=num_samples),
    'ht': np.random.normal(loc=170, scale=10, size=num_samples),
    'wt': np.random.normal(loc=70, scale=10, size=num_samples),
    'smoke': np.random.choice([0, 1], size=num_samples),
    'alcohol': np.random.choice([0, 1], size=num_samples),
    'sleephrs': np.random.normal(loc=7, scale=1, size=num_samples),
    'exercisehrs': np.random.normal(loc=3, scale=2, size=num_samples),  # New feature
    'hitbox': np.random.normal(loc=1.0, scale=0.3, size=num_samples)  # New feature
}

# calculating healtime from generated data according to formula
def calculate_recovery_time(row):
    age_effect = row['age'] / 10  # older ppl may take longer to heal
    bad_habits_effect = row['smoke'] * 2 + row['alcohol'] * 1.5  # smoking + alcohol bad
    sleep_effect = (8 - row['sleephrs']) / 2  # less sleep = slower healing
    exercise_effect = row['exercisehrs'] / 3  # being active = faster healing
    object_weight_effect = (4.5**row['hitbox'])*2.0  # exponential increase in healtime for heavier objects

    # Combine effects and add some random noise
    recovery_time = 10 + age_effect + bad_habits_effect + sleep_effect - exercise_effect + object_weight_effect + np.random.normal(loc=0, scale=3)
    return max(recovery_time, 0)  # Ensure recovery time is non-negative

# Apply the function to generate recovery time
data['healtime'] = [calculate_recovery_time(row) for _, row in pd.DataFrame(data).iterrows()]

# Create DataFrame
df = pd.DataFrame(data)

# Round Age, Height, Weight, Sleep_Hours, Exercise_Hours, Object_Hit_Weight, and Time_to_Heal to 2 decimal places
df = df.round({'age': 2, 'ht': 2, 'wt': 2, 'sleephrs': 2, 'exercisehrs': 2, 'hitbox': 2, 'healtime': 2})

# Save DataFrame to CSV file
df.to_csv('concussion_recovery_data.csv', index=False)

print("CSV file saved successfully.")