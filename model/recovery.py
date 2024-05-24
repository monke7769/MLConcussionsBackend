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
    severitymap = {
        'None': 0,
        'Mild': 1,
        'Moderate': 3,
        'Severe': 5
    }
    symptomscores = [] # collect a list of all scores for separate symptoms (in order)
    for i in range(len(patient)):
        symptomscores.append(weights[i]*severitymap[patient[i][1]])
    print(symptomscores)
    totalscore = sum(symptomscores)
    # initialize final list to return
    final = [totalscore, []]
    # now append suggested recovery methods to final[1]
    # the following conditionals deal with scientifically proven recovery methods
    # remember to research these tmrw in class + do the html/js formatting
    return final

testlist = [['Headache', 'Moderate'], ['Neck Pain', 'Mild'], ['Nausea', 'Mild'], ['Dizziness', 'None'], ['Blurred Vision', 'Mild'], ['Sensitivity to Noise', 'Severe'], ['Sensitivity to Light', 'None'], ['Memory Loss', 'None'], ['Lack of Concentration', 'None'], ['Fatigue', 'None'], ['Confusion', 'None'], ['Drowsiness', 'None'], ['Insomnia', 'None'], ['Irritability', 'None'], ['Nervousness/Anxiety', 'None']]
recovery(testlist)