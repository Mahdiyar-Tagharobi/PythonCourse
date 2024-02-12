n = int(input("Enter a number: "))

f = [0]
i = 0
x = 0
y = 1
nn = 1
while i <= n-2:
    f.append(nn)
    y = x
    x = nn
    nn = x + y
    i += 1
    print(f)
