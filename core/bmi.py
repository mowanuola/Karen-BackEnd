def calculateBMI(height, weight):
    BMI = 0
    if height and weight:
        BMI = weight / ((height / 100) * (height / 100))
    return BMI


def getCalorieThreshold(bmi):
    if bmi <= 19: 
        return 500
    elif bmi > 19 or bmi <= 25 :
        return 600
    elif bmi > 25:
        return 200