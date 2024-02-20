import random as rand

vocab = ["birD", "PurPle", "JohN", "monkEy", "Green", "smAll", "toWer"]
rand_vocab_word = rand.randint(0, len(vocab) - 1)
rand_word = vocab[rand_vocab_word]

true_guess = []
false_guess = []
u_chance = 6

while u_chance > 0:
    win = True
    for i in range(len(rand_word)):
        if rand_word[i].lower() in true_guess:
            print(rand_word[i].lower(), end = "")
        else:
            print(" - ", end = "")
            win = False
    print("\t")
    
    if  win:
        break    
    u_guess = input("Etner you guess: ").lower()
    if len(u_guess) == 1 and str:
        if u_guess in rand_word.lower():
            true_guess.append(u_guess)
            print("that's right! ")
        else:
            u_chance -= 1
            
            false_guess.append(u_guess)
            print("oh! not true :( ")
    else:
        print("Enter a character correctly")

if win:
    print(f"\n---You win! :)\t the word is {rand_word.lower()}")
else:
    print(f"\n---You lose :(\t the word is {rand_word.lower()}")
