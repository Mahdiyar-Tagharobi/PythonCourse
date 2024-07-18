import numpy as np

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
    
    def Fraction_to_number(self):
        return self.numerator / self.denominator
    


class Time():
    def __init__(self, hour, minute, second):
        self.h = hour
        self.min = minute
        self.sec = second
        self.fix()

    def __str__(self):
        print(f"{self.h}:{self.min}:{self.sec}")
        
    def __add__(self, other):
        #calc -> calculated
        calc_s = self.sec + other.sec
        calc_m = self.min + other.min
        calc_h = self.h + other.h
        
        final_time = Time(calc_h, calc_m, calc_s)
        final_time.fix()
        
        return final_time
        
    def __sub__(self, other):
        calc_s = self.sec - other.sec
        calc_m = self.min - other.min
        calc_h = self.h - other.h
    
        final_time = Time(abs(calc_h), abs(calc_m), abs(calc_s))
        final_time.fix()
        return final_time
    
    def hours_to_seconds(self):
        self.min += self.h * 60
        self.sec += self.min * 60
        return f"converted time is -> {self.sec}"
    
    def seconds_to_hours(self, other):
        m_and_s = other % 3600
        s = m_and_s % 60
        return f"converted time is -> {other // 3600}:{m_and_s // 60}:{s}"
            
    def fix(self):
        if self.sec >= 60:
            self.sec -= 60
            self.min += 1
            
        if self.min >= 60:
            self.min -= 60
            self.h += 1
            
        if self.sec < 0:
            self.sec += 60
            self.min -= 1
            
        if self.min < 0:
            self.min += 60
            self.sec -= 1

    
def generate_carpet(n):
    
    carpet = np.array([[0] * n] * n)
    
    if n % 2 != 0:
        for i in range(n):
            carpet[i] = 0
            
        return carpet
    else :
        return "this number is even, please enter an odd number"
        
def show(carpet):
    try:
        int(carpet)
        for row in carpet:  
            print(row)
    except:
        print(carpet)
    
c = generate_carpet(5)
show(c)

