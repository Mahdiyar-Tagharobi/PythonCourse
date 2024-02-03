name = input("Enter your first and last name: ")

m1 = float(input("Enter first mark: "))
m2 = float(input("Enter second mark: "))
m3 = float(input("Enter third mark: "))

average = (m1 + m2 + m3) / 3

if average >= 17 :
    print(f"Mr.{name}, your status is great :D")
elif (17 > average) and (average >= 12) :
    print(f"Mr.{name}, your status is normal :)")
elif average < 12 :
    print(f"Mr.{name}, your status is failed :(")
