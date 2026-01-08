class fraction():
    def __init__(self, first_fraction:str, second_fraction:str):
        self.first_num = list(map(int, first_fraction.split("/")))
        self.second_num =  list(map(int, second_fraction.split("/")))
        
        
    def multiply(self):
        numerator = self.first_num[0] * self.second_num[0]
        denominator = self.first_num[1] * self.second_num[1]
        return f"{numerator}/{denominator}" 
    
    def add(self):
        pass
    

test = fraction('5/8', '3/2')

print(test.first_num[0])
print(test.second_num)
print(test.multiply())

# x = 5/8
# print(type(x))
# int(x)
# print(type(str(x)))