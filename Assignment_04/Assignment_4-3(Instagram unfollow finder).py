import instaloader as insta
import getpass


#FWs == Followers(shorter and easier)
first_FWs_file = open("Assignment_4/followers.txt", 'r')
old_FWs = []
for line in first_FWs_file.readlines():
    old_FWs.append(line)
first_FWs_file.close()


usern = input("Enter your username: ")
passw =  getpass.getpass("Enter password: ")

login = insta.Instaloader()
login.login(usern, passw)
print("successful")

targer_p = input("who do you want to see new followers?: ")

data_targer_p = insta.Profile.from_username(login.context, targer_p)


FWs = []
for FW in data_targer_p.get_followers():
    FWs.append(FW)

for FW in old_FWs:
    if FW not in FWs:
        print(FW)
        


        
FWs_file = open("Assignment_4/followers.txt", 'w')
for line in FWs:
    if line not in old_FWs:
        FWs_file.write(f"{line} \n")
FWs_file.close()

