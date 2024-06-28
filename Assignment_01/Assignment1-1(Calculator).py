import math

print("----Simple Calculator----")

print("--------\n + = sum\n - = sub\n * = mul\n / = dev\n f = fuctorial\n sin\n log\n sqrt\n cos\n tan\n cot\n --------")

op = input("Please enter your desire operator: ")

if op == "+" or op == "-" or op == "*" or op == "/":
    fn = float(input("Enter first number"))
    sn = float(input("Enter second number"))
else :
    fn = float(input("Enter the number"))

if op == "+":
    print(fn + sn)

elif op == "-":
    print(fn - sn)

elif op == "*":
    print(fn * sn)

elif op == "/":
    if sn == 0:
        print("can't divide by zero")
    else:
        print(fn / sn)

elif op == "sin":
    print(math.sin(math.radians(fn)))

elif op == "cos":
    print(math.cos(math.radians(fn)))

elif op == "tan":
    print(math.tan(math.radians(fn)))

elif op == "cot":
    print(1 / math.tan(math.radians(fn)))

elif op == "log":
    print(math.log)

elif op == "sqrt":
    print(math.sqrt)

elif op == "f":
    print(math.factorial(int(fn)))

else :
    print("Your requested operator is not entered correctly")
