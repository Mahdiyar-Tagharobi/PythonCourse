import pyfiglet as fig
import gtts

is_write = False

def read_write_from_file(is_write):
    try:
        global words_bank

        if is_write == True:
            #It will run when is_write boolean is true, that means i wanna write in file
            en = input("Enter the English word: ")
            fa = input("Enter the Persian word: ")

            with open("Assignment_8\Translate.txt", "a") as file:
                file.write("\n" + en + "\n" + fa)

                is_write = False
            file.close()    
            print("Successfully added!")

        else :
            #It will run when is_write boolean is false, that means i wanna read from file
            with open("Assignment_8\Translate.txt", "r") as file:
                words_bank = []
                w = file.read().split("\n")
                
                for i in range(0, len(w), 2):
                    dic = {"en": w[i], "fa": w[i + 1]}
                    words_bank.append(dic)
            file.close()  
            
    except:
        print("Couldn't find file")
        exit(120)

def translate(u_choice):
    
    inp = input("enter your sentence you want to translate it: ").strip()
    
    #split by dot for sentences
    u_sentence = inp.split(".")

    #this variable just used for gtts input
    voice = ""

    for u_word in u_sentence:
        #empty output variable for better output
        out = ""
        u_word = u_word.strip()

        #split by space for words
        u_word = u_word.split(' ')
        for u_w in u_word:
            #find input words in word bank file    
            for word in words_bank:

                #choose between translate to english or persian
                if u_choice == 1:

                    #English
                    if u_w == word["en"]:
                        out = out + word["fa"] + ' '
                        break

                elif u_choice == 2:

                    #Persian
                    if u_w == word["fa"]:
                        out = out + word["en"] + ' '
                        break
            else:
                    out = str(out) + str(u_w) + ' ' 

        voice += " " + out
        print(out)


    if u_choice == 1:
        voice = gtts.gTTS(voice, lang='ur', slow=True)
    elif u_choice == 2:
        voice = gtts.gTTS(voice, lang='en', slow=True)
    voice.save("Assignment_8/Voice.mp3")


def add_word():
    while True:
        is_write = True
        read_write_from_file(is_write)
        
        if (input("Do you want add again? (y/n): ")).lower() != "y":
            break
    
def menu():
    print("-------Menu\n 1- English to persian\n 2- Persian to English\n 3- Add new word to database\n 4- Exit")


#start
greetings = fig.figlet_format("Welcome to translator", font="slant")

print(greetings)
while True:
    read_write_from_file(is_write)
    menu()

    u_choice = int(input("Enter your choice: ").strip())

    if u_choice == 1 or u_choice == 2:
        translate(u_choice)
    elif u_choice == 3:
        add_word()
    elif u_choice == 4:
        print("-------Bye! 👋")
        exit(0)
    else: 
        print("Enter number correctly")