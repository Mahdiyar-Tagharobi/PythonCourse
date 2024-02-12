weight = float(input('Enter your weight : '))
height = float(input("Enter your height(attention: enter by metre) : "))

BMI = weight / height**2

if BMI < 18.5:
    print('Your BMI is Underweight')
elif (BMI >= 18.5) and (BMI < 25):
    print('Your BMI is Normal Weight')
elif (BMI >= 25) and (BMI < 30):
    print('Your BMI is Overweight')
elif (BMI >= 30) and (BMI < 35):
    print('Your BMI is Obesity')
elif (BMI >= 35) and (BMI < 40):
    print('Your BMI is Extreme Obesity')
else :
    print("Are you sure about the numbers entered? it doesen't seem logical")