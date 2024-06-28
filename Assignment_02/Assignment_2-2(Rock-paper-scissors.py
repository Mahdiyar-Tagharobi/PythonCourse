import random as rand

while True:
    
    computer = rand.choice(["Rock", "Paper", "Scissors"])
    
    user = input("----{Rock, Paper, Scissors Game!}----\n-Enter your choice!(For leave, Enter other words like exit): ")
    print(f'\nComputer choice is: {computer}\n')
    
    #computer win
    if computer == "Rock" and user == "Scissors" or computer == "Scissors" and user == "Paper" or computer == "Paper" and user == "Rock": print("Computer win :(\n")
    
    #User win    
    elif  computer == "Scissors" and user == "Rock" or computer == "Paper" and user == "Scissors" or computer == "Rock" and user == "Paper": print("You win :)\n")
    
    #Tie
    elif computer == "Scissors" and user == "Scissors" or computer == "Paper" and user == "Paper" or computer == "Rock" and user == "Rock": print("Tie :/\n")
    
    #exit
    else : 
        print("Have a nice day!\n")
        break
        