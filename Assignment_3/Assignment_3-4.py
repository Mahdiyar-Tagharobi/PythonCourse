inp = int(input("Enter your number: "))

for i in range(inp):
    if i % 2 == 0:
        print("*", end = "")
    else: 
        print("#", end = "")