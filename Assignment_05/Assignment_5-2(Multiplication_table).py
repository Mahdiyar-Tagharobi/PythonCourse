def multiplication_chart(m, n):
    for i in range(n):
        for border in range(n):
            print('——————', end='')
        print('')
        print('| ', end='')
        for j in range(m):
                print((i + 1)  * (j + 1), end=' | ')
        print('')
    
n = int(input("Enter a number for row: "))
m = int(input("Enter a number for column: "))

multiplication_chart(m, n)