def read_from_file():

    words = []

    file = open("Assignment_8\Translate.txt", "r")

    for line in file.readlines():
        
        main_s = line.strip()
        words.append(main_s)
    
    file.close()    

