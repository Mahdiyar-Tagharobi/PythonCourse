import pyfiglet as fig

PROD = []

def read_from_db():

    file = open("Assignment_7\database.txt", "r")

    for line in file.readlines():
        
        res = line.split(",")
        organized_import = {"code": res[0], "name": res[1], "price": res[2], "count": res[3]}
        PROD.append(organized_import)
    
    file.close()

def menu_show():
    print("1- Add \n2- Edit \n3- Remove \n4- Search \n5- Show List \n6- Buy \n7- Exit")
    print("--------------------------------------------------")       


def add():
    code = input("Enter product code ")
    name = input("Enter product name ")
    price = input("Enter product price ")
    count = input("Enter the number of product is available ")
    codes = [data['code'] for data in PROD]
    if code not in codes:
        imports = {"code": code, "name": name, "price": price, "count": count }
        PROD.append(imports)
        write_data(PROD)
        print("Successfully added! \n")
    else :
        print("This Product code is available, please enter different Product code")
        
    print("--------------------------------------------------")       

def edit():
    r_code = input("Enter product code:")
    r_name = input("Enter product name:")

    for index, product in enumerate(PROD):
        if product["code"] == r_code and product["name"] == r_name:
                code = input("Enter new product code ")
                name = input("Enter new product name ")
                price = input("Enter new product price ")
                count = input("Enter the new number of product is available ")
                PROD[index] = {"code": code, "name": name, "price": price, "count": count }
                write_data(PROD)
                print("Successfully edited! \n")
                return
    print("product not found")
    print("--------------------------------------------------")       
            

def remove():
    r_code = input("Enter product code:")
    r_name = input("Enter product name:")        

    for product in PROD:
        if product["code"] == r_code and product["name"] == r_name:
            PROD.remove(product)
    write_data(PROD)
    print("Successfully removed! \n")
    print("--------------------------------------------------")       

            
def search():
    found = False

    r_code = input("Enter product code:")
    r_name = input("Enter product name:")
    for product in PROD:
        if product["code"] == r_code and product["name"] == r_name:
            print(product["code"], "\t", product["name"], "\t\t", product["price"])
            found = True
    if not found:
        print("Product not found")
            
    print("--------------------------------------------------")       



def show_list():
    print("--------------------------------------------------")       
    print(" code\t  name\t\t price\t   Available\t ")
    for p in PROD:
        if int(p["count"]) > 0:
            print("",p["code"], "\t", p["name"], "\t\t", p["price"], '\t  Available now ')
        else:
            print("",p["code"], "\t", p["name"], "\t\t", p["price"], '\t  Not available ')
    print("--------------------------------------------------")       
def buy():
    continue_s = True
    found = False
    factor_name = []
    factor_count = []
    
    while continue_s:
        r_code = input("Enter product code: ")
        r_count = int(input("Enter product count: "))

        for product in PROD:
            if product["code"] == r_code and int(product["count"]) >= r_count:
                factor_name.append(product["name"])
                index = PROD.index(product)
                
                PROD[index]["count"] = str(int(PROD[index]["count"]) - int(r_count))
                write_data(PROD)
                
                print('SOld!')
                found = True
                
        if not found:
            print("Product not found or isn't available")
            
        
        if input("Do you want to continue shopping?(y/n): ") == "y" :  
            if found:
                factor_count.append(r_count)
            
            found = False
        else :
            if found:
                factor_count.append(r_count)
                                
                print("\nYou bought these items:")
                for i in range(len(factor_name)):
                    print(f"--You bought Product {factor_name[i]} , {factor_count[i]} of this item")
              
            continue_s = False
    print("--------------------------------------------------")       
    
def write_data(datas):
    with open("Assignment_7\database.txt", "w") as file:
        for idx, data in enumerate(datas):
            product =  data['code'] + "," + data['name'] + "," + data['price'] + "," + data['count']
            product = product.strip("\n")
            if (idx != 0):
                product = '\n' + product
            file.write(product)


greetings = fig.figlet_format("Welcome to shop", font="slant")

print(greetings)
read_from_db()

while True:
    menu_show()
    ch = input('Enter your choice: ')

    if ch == '1':
        add()
    elif ch == '2':
        edit()
    elif ch == '3':
        remove()
    elif ch == '4':
        search()
    elif ch == '5':
        show_list()
    elif ch == '6':
        buy()
    elif ch == '7':
        exit()
    else :
        print("please enter number correctly")