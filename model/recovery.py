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
        'Sensitivity to Noise': "Isolate yourself. If symptoms are mild-none wear sunglasses and earmuffs when outdoors.",
        'Sensitivity to Light': "Isolate yourself. If symptoms are mild-none wear sunglasses and earmuffs when outdoors.",
        'Neck Pain': "Rest your head and do minimal movement.",
        'Nausea': "Dramamine tablets and Scopolamine patches.",
        'Blurred Vision': "Rest, if severe and persistent recommended prescription lenses/glasses.",
        'Memory Loss': "If severe/moderate memory, consider getting cognitive therapy.",
        'Fatigue': "Rest, try to avoid doing things and let your brain heal.",
        'Lack of Concentration': "Rest, try to avoid doing things and let your brain heal.",
        'Confusion': "Rest, try to avoid doing things and let your brain heal.",
        'Drowsiness': "Rest, try to avoid doing things and let your brain heal.",
        'Insomnia': "Take supplements before sleep, even if you’re not experiencing headaches, avoid screens at least 1-2 hours before sleep.",
        'Irritability': "Talk to people and do simple, none intensive activities. If it persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        'Nervousness/Anxiety': "Talk to people and do simple, none intensive activities. If it persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        'Sadness/Depression': "Talk to people and do simple, none intensive activities. If it persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world."
    }
    symptomscores = [] # collect a list of all scores for separate symptoms (in order)
    for i in range(len(patient)):
        symptomscores.append(weights[i]*severitymap[patient[i][1]])
    print(symptomscores)
    totalscore = sum(symptomscores)
    # initialize final list to return
    final = [totalscore, []]

    if totalscore>500:
        return "Please seek immediate medical attention."
    # now append suggested recovery methods to final[1]
    # Best recovery methods... Headache, no screens, no lights, no sound. Do nothing if you have an extreme headache. 
    # Never use screens for the first week atleast.
    # Sensivity to light/noise, if mild or lower, wear sunglasses and earmuffs/earplugs all the time. If moderate/severe, stay in your room alone with all the lights off
    # If all sympoms are mild to none, start doing light exercise such as jogging or walking. The sunlight and sligt activity helps bloodflow which can help recovery
    # Mandatory Fish oil supplements no matter what even if youre healed even if you never had a concussion
    # the following conditionals deal with scientifically proven recovery methods
    # remember to research these tmrw in class + do the html/js formatting
    return final

testlist = [['Headache', 'Moderate'], ['Neck Pain', 'Mild'], ['Nausea', 'Mild'], ['Dizziness', 'None'], ['Blurred Vision', 'Mild'], ['Sensitivity to Noise', 'Severe'], ['Sensitivity to Light', 'None'], ['Memory Loss', 'None'], ['Lack of Concentration', 'None'], ['Fatigue', 'None'], ['Confusion', 'None'], ['Drowsiness', 'None'], ['Insomnia', 'None'], ['Irritability', 'None'], ['Nervousness/Anxiety', 'None']]
recovery(testlist)