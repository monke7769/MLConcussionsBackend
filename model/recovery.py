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
    
    suggestions = {
        'Headache': "Headache, no screens, no lights, no sound. Do nothing if you have an extreme headache. If persistent you can take aspirin/ibuprofen. If extreme and persistent, visit medical personnel.",
        'Sensitivity to Noise': "Isolate yourself. Wear sunglasses and earmuffs when outdoors.",
        'Sensitivity to Light': "Isolate yourself. Wear sunglasses and earmuffs when outdoors.",
        'Neck Pain': "Rest your head and have minimal movement.",
        'Nausea': "Dramamine tablets and Scopolamine patches are in order.",
        'Blurred Vision': "Rest, if severe and persistent recommended prescription lenses/glasses.",
        'Memory Loss': "If severe/moderate memory, consider getting cognitive therapy.",
        'Fatigue': "Rest, try to avoid doing things and let your brain heal.",
        'Lack of Concentration': "Rest, try to avoid doing things and let your brain heal.",
        'Confusion': "Rest, try to avoid doing things and let your brain heal.",
        'Drowsiness': "Rest, try to avoid doing things and let your brain heal.",
        'Insomnia': "Take supplements before sleep, even if you’re not experiencing headaches, avoid screens at least 1-2 hours before sleep.",
        'Irritability': "Talk to people and do simple, none intensive activities. If it persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        'Nervousness/Anxiety': "Talk to people and do simple, none intensive activities. If it persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        'Dizziness': "Talk to people and do simple, none intensive activities. If it persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world."
    }
    symptomscores = [] # collect a list of all scores for separate symptoms (in order)
    for i in range(len(patient)):
        symptomscores.append(weights[i]*severitymap[patient[i][1]])
    print(symptomscores)
    totalscore = sum(symptomscores)
    # initialize final list to return
    final = [totalscore, []]

    mostsevere = np.argmax(symptomscores)
    print(f"Symptom with the highest score: {patient[mostsevere][0]} (Score: {symptomscores[mostsevere]})")


    if totalscore > 400:
        final[1].append("Please seek immediate medical attention. Your risk level is high.")
        return final
    severecounts = 0
    for i in symptomscores:
        if i >= 20:
            severecounts += 1
    if severecounts == 15:
        final[1].append(":skull:")
        return final
    if severecounts >= 8:
        final[1].append("A visit to the ER is in your future.")
        return final
    
    # the following are thresholds for scores of symptoms to trigger specific recovery methods
    thresholds = [10, 24, 10, 30, 8, 18, 18, 8, 24, 15, 27, 20, 12, 15, 15, 5]
    
    for i in range(len(symptomscores)):
       if symptomscores[i]>=thresholds[i]:
           final[1].append(suggestions[patient[i][0]])
    return final

testlist = [['Headache', 'Mild'], ['Neck Pain', 'Mild'], ['Nausea', 'Mild'], ['Dizziness', 'None'], ['Blurred Vision', 'Mild'], ['Sensitivity to Noise', 'Severe'], ['Sensitivity to Light', 'None'], ['Memory Loss', 'None'], ['Lack of Concentration', 'None'], ['Fatigue', 'None'], ['Confusion', 'None'], ['Drowsiness', 'None'], ['Insomnia', 'None'], ['Irritability', 'None'], ['Nervousness/Anxiety', 'None']]
recovery(testlist)