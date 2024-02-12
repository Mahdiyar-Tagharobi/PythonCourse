sum_n = 0
n = 0
while True:
    s = input(f'---Please Enter your Score.\n---If you wanna exit, please Enter exit:  ')
    if s == 'exit':
        break
    else:
        sum_n += float(s )
        n += 1
output = sum_n / n
print(f'Your score is : {output}')
