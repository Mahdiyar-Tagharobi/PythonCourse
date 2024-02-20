import random as rand

inp = int(input("Enter a number between 0 and 100 for length of your list: "))

if inp < 0 or inp > 100:
    print("Please pay attention to the mentioned range")
    process = False
else :
    process = True

list = []
while len(list) <= inp and process == True:
    rand_nums = rand.randint(0, 100)
    if rand_nums not in list:
        list.append(rand_nums)

if process == True: print(list)