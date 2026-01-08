class Complex_Number():
    def __init__(self, num1:str):
        self.first_number = self.normalized(num1)        
    
    
    def normalized(self, raw_num):
        res = [num.strip('i') for num in sorted(raw_num.split(" + "), key=lambda x: x[::-1])]
        print(res)
        res = [int(x) for x in res]
        print(res)
        return res
        
    def add(self, num2):
        second_number = self.normalized(num2)
        
        return f"{self.first_number[0] + second_number[0]} + {self.first_number[1] + second_number[1]}i"
        
        
    
    def sub(self, num2):
        second_number = self.normalized(num2)
        
        return f"{self.first_number[0] + second_number[0]} + {self.first_number[1] + second_number[1]}i"
    
    def mul(self, num2):
        second_number = self.normalized(num2)
        
        return f"{(self.first_number[0]* second_number[0] - self.first_number[1]* second_number[1])} + {(self.first_number[0]* second_number[1] + self.first_number[1]* second_number[0])}i"
    
a = Complex_Number("2 + -14i")

print(a.add("15i + -5"))

print(a.mul("5i + 9"))