import random as rand

rand_n = rand.randint(0, 100)
i = 0
while True: 
    guess = int(input("Enter your guess: "))
    i += 1
    
    if guess == rand_n:
        print(f"That's Right!🕺🏻, you find the number in {i} round\n") 
        
        #Rematch 
        rematch = input("If you want to Rematch, Enter (again) word(to leave enter other words): ")
        
        if rematch == 'again':
            print("Ok let's go!")
            rand_n = rand.randint(0, 100)
            i = 0
        else : 
            print("goodbye!")
            break
        
    elif guess > rand_n:
        print("Go Down 👇🏻")
        
    elif guess < rand_n:
        print("Go Up 👆🏻")