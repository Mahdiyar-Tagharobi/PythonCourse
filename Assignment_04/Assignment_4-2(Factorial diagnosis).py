inp = int(input("Enter a number: "))

fac = 1
n = 1

while fac < inp:
    n += 1
    fac *= n

if fac == inp:
    print("True")
else:
    print("False")