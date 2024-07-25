

height = float(input("Enter your Height in meters "))
weight = int(input("Enter your Weight in kg "))
bmi = weight / (height * height)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight. ")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have normal weight. ")
elif bmi < 30:
    print( f"Your BMI is {bmi}, you are slightly overweight. " )
elif bmi < 35:
    print( f"Your BMI is {bmi}, you are obese. " )


