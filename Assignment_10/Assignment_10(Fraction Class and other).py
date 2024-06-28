
class Fraction():
    #The Fraction line must be / to work correctly
    def __init__(self, text:str):
        self.numerator = int(text.split("/")[0])
        self.denominator = int(text.split("/")[1])
        
    def __str__(self) -> str:
        return f"{self.numerator}/{self.numerator}"
    
    def __mul__(self, second): 
        numerator = self.numerator * second.numerator
        denominator = self.denominator * second.denominator
        return Fraction(f"{numerator}/{denominator}")
    
    def __truediv__(self, second):
        numerator = self.numerator * second.denominator
        denominator = self.denominator * second.numerator
        return Fraction(f"{numerator}/{denominator}")
    
    def __add__(self, second):
        first_numerator = self.numerator * second.denominator
        second_numerator = second.numerator * self.denominator
        denominator = self.denominator * second.denominator
        return Fraction(f"{first_numerator + second_numerator}/{denominator}")
        

    def __sub__(self, second):
        first_numerator = self.numerator * second.denominator
        second_numerator = second.numerator * self.denominator
        denominator = self.denominator * second.denominator
        return Fraction(f"{first_numerator - second_numerator}/{denominator}")


class Time():
    def __init__(self, sec, min, h):
        self.sec = sec
        self.min = min
        self.h = h

    def __add__(self):
        ...
        
    def __sub__(self):
        ...
        

class Date():
    def __init__(self, day, month, year, calender):
        ...
    
    def __add__(self):
        ...
        
    def __sub__(self):
        ...
    
    def convert_calender(self):
        ...

