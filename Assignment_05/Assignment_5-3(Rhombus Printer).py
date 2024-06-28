def rhombus(rows):
    x = 1

    #increasing
    for i in range(rows):
        
        space = ( ( (rows * 2) - 1) - x) // 2
        print(' ' * space, end='')
        
        for j in range(x):
            print('*', end='')
        
        
        print('')
        x += 2

    #decreasing
    x -= 4

    for i in range(rows):
        
        i += 1    
        star = x - (i * 2)
        space = (x - star) // 2
        print(' ' * space, end='')
        
        for j in range(x):
            print('*', end='')
        
        
        print('')
        x -= 2

rhombus(int(input("Enter a number: ")))
