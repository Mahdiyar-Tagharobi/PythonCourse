def read_from_file():

    words = []

    file = open("Assignment_8\Translate.txt", "r")

    w = file.read().split("\n")
    
    for i in range(0, len(w), 2):
        dic = {"en": w[i], "fa": w[i + 1]}
        words.append(dic)
        
    
    file.close()    

def en_to_per():
    ...

def per_to_en():
    ...

def menu():
    print("1- English to persian\n 2- Persian to English\n 3- Add new word to database\n 4- Exit")
    



inp = input("enter your sentence you want to translate it")

for i in words:
    ...