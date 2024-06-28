def Checkered_board(m, n):
    i = 0
    j = 0    
    
    for i in range(n):
        for j in range(m):
            if i % 2 == 0:
                if j % 2 == 0:
                    print('#', end='  ')
                else:
                    print('*', end='  ') 
            
            else:
                if j % 2 != 0:
                    print('#', end='  ')
                else:
                    print('*', end='  ') 
                    
        print('')

n = int(input("Enter a number for row: "))
m = int(input("Enter a number for column: "))

Checkered_board(m, n)