Height = int(input("enter your height in inches: "))
Weight = int(input("enter your weight in lbs: "))

BMI = float((Weight * 703) / (Height * Height))


if (BMI < 16.0):
    print("Severely Underweight ")
elif(16.0 < BMI < 18.4):
    print("Underweight")
elif(18.5 < BMI < 24.9):
    print("Normal")
elif(25.0 < BMI < 29.9):
    print("Overweight")
elif(30.0 < BMI < 34.9):
    print("Moderately Obese")
elif(BMI > 39.9):
    print("Morbidly Obese")
    
    