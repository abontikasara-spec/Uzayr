height = float(input("Enter you height in cm : "))
weight = float(input("Enter you weight in kg : "))

BMI = weight / (height/100)**2

print("Your BMI is ", BMI)

if BMI <= 19.9:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely overweight")
elif BMI <= 39.9:
    print("You are obese")
else:
    print("You are severely obese")