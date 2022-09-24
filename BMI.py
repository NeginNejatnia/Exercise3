weight = float(input('Enter your Weight Kg: '))
Height = float(input('Enter your Height cm: '))
BMI = weight / (Height/100)**2
print('Your BMI is :',BMI)

if BMI <= 18.5:
    print('You are Underweight.')
elif BMI <= 24.9:
    print('You are Normal.')
elif BMI <= 29.9:
    print('You are Over weight.')
elif BMI <= 34.9:
    print('You are Severely over weight.')
elif BMI >= 35:
    print('You are Obese.')
else:
    print('You are Extremely obese.')
