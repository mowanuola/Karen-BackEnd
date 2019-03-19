def calculateDCI(height, weight, sex, age, useractivity ):
    BMR = 0
    DCI = 0
    if height and weight and age:    
        if sex == "Female":
            BMR = (9.99 * weight) + (6.25 * height) - (4.92 * age) - 161
        if useractivity == 1:
            DCI = BMR * 1.1
    
        elif useractivity == 2:
            DCI = BMR * 1.35
            
        elif useractivity == 3:
            DCI = BMR * 1.525
        
        elif sex == "Male":
            BMR = (9.99 * weight) + (6.25 * height)-(4.92 * age) + 5
        if useractivity == 1:
            DCI = BMR * 1.2
    
        elif useractivity == 2:
            DCI = BMR * 1.55
          
        elif useractivity == 3:
            DCI = BMR * 1.725           
    return DCI