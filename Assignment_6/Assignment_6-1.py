import pyfiglet 
import time 
from colorama import Fore
import random as r


def plate_show():
    # Just cleaning
    print("\a")
    
    for rows in plate:
        for cell in rows:
            print(cell, end=' ')
        print()    
    
    # Just cleaning
    print("\a")


def win(plate, n): 

    count = ""
    
    # Text win used for if 
    win_P1_text = '\x1b[31mX\x1b[37m' * 3
    win_P2_text = '\x1b[34mO\x1b[37m' * 3
    
    # Vertical
    for i in range(3):
        for j in range(3):
            count  += plate[i][j]
             
        if count == win_P1_text or count == win_P2_text :
            print(f"-_-_Player {n} wins :))) ")
            return True
            break
            exit()
        else:
            draw = count
            count = ""
    # Horizontal
    for i in range(3):
        for j in range(3):
            count  += plate[j][i] 
            
        if count == win_P1_text or count == win_P2_text:
            print(f"-_-_Player {n} wins :))) ")
            return True
            break
        else:
            draw = count
            count = ""
    
    # Diagonal
    if plate[0][0] + plate[1][1] + plate[2][2] == win_P1_text or plate[0][2] + plate[1][1] + plate[2][0] == win_P1_text or plate[0][0] + plate[1][1] + plate[2][2] == win_P2_text or plate[0][2] + plate[1][1] + plate[2][0] == win_P2_text  :
        print(f"-_-_Player {n} wins :))) ")
        return True
    
    # Draw
    else : 
        if  "-" not in draw:
            print("\n ----Draw :\ ")     
    
    # Still in process
    return False  

def timer(start_time): 
    time_now = time.time()
    t = int(time_now - start_time)
    
    m_and_s = t % 3600

    s = m_and_s % 60

    print(f"-_-_Elapsed time: {t // 3600} : {m_and_s // 60} : {s}\a")

# Starting timer
start_time = time.time()   

greetings = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
ch_play = pyfiglet.figlet_format("Select mode : ", font="slant")

print(greetings)
print(ch_play)


plate = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

plate_show()

while True:
    #select mode
    mode = int(input("Enter 1 for 1 v 1 and enter 2 for PC v 1: "))
    
    if mode == 1:
        while True:
            print("---Player 1 turn:")
            n = 1
            while True:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if plate[row][col] == "-":            
                        plate[row][col] = f"{Fore.RED}X{Fore.WHITE}"
                        plate_show()
                        if win(plate, n) == True:
                            
                            #print time
                            timer(start_time)                    
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
                        plate[row][col] = f"{Fore.BLUE}O{Fore.WHITE}"
                        plate_show()
                        if win(plate, n) == True:
                            
                            #Calculating time
                            timer(start_time)
                            
                            exit()
                        break
                    
                    else:
                        print("please select an empty cell :/")
                else :
                        print("please select avalaible cell")
    elif mode == 2:
        while True:
            print("---Player 1 turn:")
            n = 1
            while True:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if plate[row][col] == "-":            
                        plate[row][col] = f"{Fore.RED}X{Fore.WHITE}"
                        plate_show()
                        if win(plate, n) == True:
                            
                            #print time
                            timer(start_time)                    
                            exit()
                        break
                    
                    else:
                        print("please select an empty cell :/")
                else :
                        print("please select avalaible cell")
                    

            print("---Computer's 2 turn:")
            n = Computer
            
            while True:
                row = r.randint(0, 2)
                col = r.randint(0, 2)
                
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if plate[row][col] == "-":            
                        plate[row][col] = f"{Fore.BLUE}O{Fore.WHITE}"
                        plate_show()
                        if win(plate, n) == True:
                            
                            #Calculating time
                            timer(start_time)
                            
                            exit()
                        break
                    
                    else:
                        print("please select an empty cell :/")
                else :
                        print("please select avalaible cell")                        