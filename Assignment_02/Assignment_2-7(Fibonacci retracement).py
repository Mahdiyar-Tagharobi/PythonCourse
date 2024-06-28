n = int(input("Enter a number: "))

lst = [0]
num1 = 0
num2 = 0
num3 = 1
new_num = 1
while num1 <= n-2:
    lst.append(new_num)
    num3 = num2
    num2 = new_num
    new_num = num2 + num3
    num1 += 1
print(lst)
