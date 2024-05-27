import numpy as np

# Define the weights for each symptom on a scale of 0-10
weights = [10, 8, 10, 10, 8, 6, 6, 8, 8, 5, 9, 4, 4, 5, 5, 5]

def recovery(patient):
    severitymap = {
        'None': 0,
        'Mild': 1,
        'Moderate': 3,
        'Severe': 5
    }
    extremes = [50,40,50,50,40,30,30,40,40,25,36,20,20,25,25,25]

    extremesuggestions = {
        "Headache": "Sleep, do not expose yourself to any light or noise, make sure to take pain medications and supplements. Stay extra hydrated and rest. If it continues seek medical advice from a professional.",
        "Sensitivity to Noise": "Isolate yourself. Do not go outdoors and do not listen to any music.",
        "Sensitivity to Light": "Isolate yourself Do not go outdoors and do not look at any screens, if it persists seek prescription lenses.",
        "Neck Pain": "If extreme neck pain, go to a clinic.",
        "Nausea": "Dramamine tablets and Scopolamine patches are in order.",
        "Blurred Vision": "Rest. If severe and persistent blurred vision, recommended prescription lenses/glasses.",
        "Memory Loss" : "If severe/moderate memory loss, consider getting cognitive therapy.",
        "Fatigue": "Rest. Try to avoid doing things and let your brain heal.",
        "Lack of Concentration": "Rest. Try to avoid doing things and let your brain heal.",
        "Confusion": "Rest. Try to avoid doing things and let your brain heal.",
        "Drowsiness": "Rest. let your brain heal.",
        "Insomnia": "Take supplements before sleep. Avoid screens at least 1-2 hours before sleep. If you are unable to sleep, you may need to a CT scan.",
        "Irritability": "Talk to people and do simple, non-intensive activities. If irritable state persists, get therapy and talk to medical professionals. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        "Nervousness/Anxiety": "Talk to people and do simple, non-intensive activities. If nervousness persists, get therapy. You don't need to push yourself to come back right away, a couple weeks to make sure you come back strong is better than rushing your way to permenant brain damage.",
        "Sadness/Depression": "Talk to people and do simple, non-intensive activities. If sadness persists, get therapy. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        "Dizziness": "If you are unable to do anything without feeling dizzy, you may need to get a CT scan."}
            
    suggestions = {
        'Headache': "Headache, no screens, no lights, no sound. If persistent headache you can take aspirin/ibuprofen.",
        'Sensitivity to Noise': "Isolate yourself. Wear sunglasses when outdoors.",
        'Sensitivity to Light': "Isolate yourself. Wear earmuffs when outdoors.",
        'Neck Pain': "Rest your head and have minimal movement.",
        'Nausea': "Rest in silence but make you still eat food.",
        'Blurred Vision': "Rest, avoid all screens",
        'Memory Loss': "Keep track of your mental fog, if it continues seek medical opinion.",
        'Fatigue': "Rest, try to avoid doing things and let your brain heal.",
        'Lack of Concentration': "Rest, try to avoid doing things and let your brain heal.",
        'Confusion': "Rest, try to avoid doing things and let your brain heal.",
        'Drowsiness': "Rest, let your brain heal.",
        'Insomnia': "Take supplements before sleep, even if you’re not experiencing headaches, avoid screens at least 1-2 hours before sleep.",
        'Irritability': "Talk to people and do simple, non-intensive activities. It is common to feel depressed after a traumatic head injury because it cuts you off from the rest of the world.",
        'Nervousness/Anxiety': "Talk to people and do simple, non-intensive activities.",
        'Sadness/Depression': "Talk to people and do simple, non-intensive activities. This will quicken you're recovery process.",
        'Dizziness': "Rest, avoid screens and lights."
    }
    
    symptomscores = []  # Collect a list of all scores for separate symptoms (in order)
    for i in range(len(patient)):
        symptomscores.append(weights[i] * severitymap[patient[i][1]])
    
    print(symptomscores)
    totalscore = sum(symptomscores)
    
    # Initialize final list to return
    final = [totalscore, []]

    if totalscore >=1 :
        final[1].append("Please take Fish Oil, Lion's Mane, Curcumin, Vitamin C and E in order to hasten your recovery. Be sure to get plenty of rest")

    mostsevere = np.argmax(symptomscores)
    print(f"Symptom with the highest score: {patient[mostsevere][0]} (Score: {symptomscores[mostsevere]})")
    
    if totalscore > 400:
        final[1].append("Please seek immediate medical attention. Your risk level is high.")
        return final
    
    severecounts = 0
    for score in symptomscores:
        if score >= 20:
            severecounts += 1
    
    if severecounts == 15:
        final[1].append(":skull:")
        return final
    
    if severecounts >= 8:
        final[1].append("A visit to the ER is in your future.")
        return final
    
    # The following are thresholds for scores of symptoms to trigger specific recovery methods
    thresholds = [10, 24, 10, 30, 8, 18, 18, 8, 24, 15, 27, 20, 12, 15, 15, 5]
    
    for i in range(len(symptomscores)):
       if symptomscores[i]>= extremes[i]:
           final[1].append(extremesuggestions[patient[i][0]])

       elif symptomscores[i] >= thresholds[i]:
           final[1].append(suggestions[patient[i][0]])
    
    # Remove duplicates from the final list
    final[1] = list(set(final[1]))
    
    return final

# Test the function with a sample list
testlist = [['Headache', 'Mild'], ['Neck Pain', 'Mild'], ['Nausea', 'Mild'], ['Dizziness', 'None'], ['Blurred Vision', 'Mild'], ['Sensitivity to Noise', 'Severe'], ['Sensitivity to Light', 'None'], ['Memory Loss', 'None'], ['Lack of Concentration', 'None'], ['Fatigue', 'None'], ['Confusion', 'None'], ['Drowsiness', 'None'], ['Insomnia', 'None'], ['Irritability', 'None'], ['Nervousness/Anxiety', 'None'], ['Sadness/Depression', 'None']]
result = recovery(testlist)
print(result)
