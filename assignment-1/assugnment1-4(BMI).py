weight = float(input('Enter your weight : '))
height = float(input("Enter your height : "))

BMI = weight / (height**2)

if BMI < 18.5:
    print('your BMI is Underweight')
elif (BMI >= 18.5) and (BMI <= 24.9):
    print('your BMI is Normal Weight')
elif (BMI >= 25) and (BMI <= 29.9):
    print('your BMI is Overweight')
elif (BMI >= 30) and (BMI <= 34.9):
    print('your BMI is Obesity')
elif (BMI >= 35) and (BMI < 40):
    print('your BMI is Extreme Obesity')