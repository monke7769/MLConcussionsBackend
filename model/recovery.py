import numpy as np

# 1 Headache severity, 10
# 2 Neck Pain, 8
# 3 Nausea Severity, 10
# 4 Dizziness, 10
# 5 Blurred Vision, 8
# 6 Sensitivity to light, 6
# 7 Sensitivity to noise, 6
# 8 Memory loss, 8
# 9 Lack of Concentration, 8
# 10 Fatigue, 5
# 11 Confusion, 9
# 12 Drowsiness, 4
# 13 Trouble Falling Asleep, 4
# 14 Irritability, 5
# 15 Nervousness/Anxiety, 5
# 16 Sadness/Depression 5

weights = [10,8,10,10,8,6,6,8,8,5,9,4,4,5,5,5] # on the scale of 0-10
# multiply each weight by severity for symptom indicated by user (0,1,3,5)
# max score = 5*(116 sum of weights) = 580
def recovery(patient):
    print('placeholder')
    return patient