import pyfiglet 
import time 


def plate_show():
    for rows in plate:
        for cell in rows:
            print(cell, end=' ')
        print()    

def win(plate, n): 
    count = ""
    #vertical
    for i in range(3):
        for j in range(3):
            count  += plate[i][j]
             
        if count == "OOO" or count == "XXX":
            print(f"\n ----Player {n} wins :))) ")
            return True
            break
            exit()
        else:
            draw = count
            count = ""
    
    #Horizontal
    for i in range(3):
        for j in range(3):
            count  += plate[j][i] 
            
        if count == "OOO" or count == "XXX":
            print(f"\n ----Player {n} wins :))) ")
            return True
            break
        else:
            draw = count
            count = ""
    
    #Diagonal
    if plate[0][0] + plate[1][1] + plate[2][2] == "XXX" or plate[0][2] + plate[1][1] + plate[2][0] == "XXX" or plate[0][0] + plate[1][1] + plate[2][2] == "OOO" or plate[0][2] + plate[1][1] + plate[2][0] == "OOO"  :
        print(f"Player {n} wins :))) ")
        return True
    else : 
        if  "-" not in draw:
            print("\n ----Draw :\ ")     
    return False 


   
    
    
    
greetings = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(greetings)

plate = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

plate_show()
while True:
    print("---Player 1 turn:")
    n = 1
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if plate[row][col] == "-":            
                plate[row][col] = "X"
                plate_show()
                if win(plate, n) == True:
                    exit()
                break
            
            else:
                print("please select an empty cell :/")
        else :
                print("please select avalaible cell")
            

    print("---Player 2 turn:")
    n = 2
    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        
        if 0 <= row <= 2 and 0 <= col <= 2:
            if plate[row][col] == "-":            
                plate[row][col] = "O"
                plate_show()
                if win(plate, n) == True:
                    exit()
                break
            
            else:
                print("please select an empty cell :/")
        else :
                print("please select avalaible cell")
                

