first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
res = []

for i in range(min(first, second), 0, -1):
    if first % i == 0 and second % i == 0:
        res.append(i)

print(max(res))