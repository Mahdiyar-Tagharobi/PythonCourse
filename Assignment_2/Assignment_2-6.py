import random as rand

list  = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0
tryes = 0
input('Please Enter any key to start round:')

while list[9] != 1:
    dice_num = rand.randint(1, 6)
    tryes += 1    
    if dice_num == 6:
        print("---Wow! your dice number is 6!\n---moving your marble one index...\n---Your reward is to roll the dice again...\n")
        list[i] = 0
        i += 1
        list[i] = 1
        print(f"---Your process:{list}---\n")
    else :
        print(f"Your dice number is {dice_num}")
        input('Please Enter any key to start round\n')

print(f"\n\n----You finish the game in {tryes} round!----\n\n")
