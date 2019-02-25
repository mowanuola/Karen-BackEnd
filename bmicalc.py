userWeight = float(input("Please Enter your Weight" ))
userHeight = float(input("Please Enter your Height" ))
userBMI = userWeight/((userHeight/100)*(userHeight/100))

if userBMI< 15:
    print("A person with a BMI of " +str(userBMI)+" is very severely underweight" )
elif userBMI< 16:
    print("A person with a BMI of " +str(userBMI)+" is severely underweight" )
elif userBMI< 18.5:
    print("A person with a BMI of " +str(userBMI)+" is underweight" )
elif userBMI> 18.5 and userBMI< 25  :
    print("A person with a BMI of " +str(userBMI)+" is normal" )
elif userBMI> 25 and userBMI< 30:
    print("A person with a BMI of " +str(userBMI)+" is overweight" )
elif userBMI> 30 and userBMI< 35:
    print("A person with a BMI of " +str(userBMI)+" is Moderately Obese (Obese Class I)" )
elif userBMI> 35 and userBMI< 40:
    print("A person with a BMI of " +str(userBMI)+" is Severly Obese (Obese Class II)" )
elif userBMI> 40 and userBMI< 45:
    print("A person with a BMI of " +str(userBMI)+" is Very Severely Obese (Obese Class III)" )
elif userBMI> 45 and userBMI< 50:
    print("A person with a BMI of " +str(userBMI)+" is Morbidly Obese (Obese Class IV)" )
elif userBMI> 50 and userBMI< 60:
    print("A person with a BMI of " +str(userBMI)+" is Super Obese (Obese Class V)" )
else:
    (print("A person with a BMI of " +str(userBMI)+" is Hyper Obese (Obese ClassVI)" ))