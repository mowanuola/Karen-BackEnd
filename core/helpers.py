from datetime import datetime, date
from django.core.validators import MaxValueValidator, MinValueValidator

diseases = ["Breast Cancer", "High Blood Pressure",
            "High Cholesterol", "Hepatitis B"]

fuzzyDict = {
    "a": [0.4, 0.25, 0.25, 0.1],
    "b": [0.09, 0.6, 0.3, 0.01],
    "ab": [0.27, 0.04, 0.5, 0.19],
    "o": [0.3, 0.02, 0.28, 0.4]
}


def get_most_likely_disease(bloodtype):
    mostLikely = max(fuzzyDict[bloodtype])
    disease = diseases[fuzzyDict[bloodtype].index(mostLikely)]
    return disease


def calculate_age(birth_date):
    try:
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    except:
        return 0


