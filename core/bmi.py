def calculateBMI(height, weight):
    BMI = 0
    if height and weight:
        BMI = weight / ((height / 100) * (height / 100))
    return BMI
