first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
res = []

for i in range(max(first, second), first * second + 1):
    if i % first == 0 and i % second == 0:
        res.append(i)

print(min(res))