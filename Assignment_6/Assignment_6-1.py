import pyfiglet 

def plate_show():
    for rows in plate:
        for cell in rows:
            print(cell, end=' ')
        print()    

def win : 

greetings = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(greetings)

plate = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

plate_show()
while True:
    print("---Player 1 turn:")
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if plate[row][col] == "-":            
                plate[row][col] = "X"
                plate_show()
                break
            
            else:
                print("please select an empty cell :/")
        else :
                print("please select avalaible cell")
            

    print("---Player 2 turn:")
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if plate[row][col] == "-":            
                plate[row][col] = "O"
                plate_show()
                break
            
            else:
                print("please select an empty cell :/")
        else :
                print("please select avalaible cell")
                
