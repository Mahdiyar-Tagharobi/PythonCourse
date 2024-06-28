import turtle
import random as r

# for randomise color to draw
colors = ["white", "red", "blue", "purple", "cyan" , "yellow", "green"]
c= 0

turtle.bgcolor("black")

p = turtle.Pen()
i = 3

s = 60

while i < 11:
        
    b = 360 / i  #120 degree
    d = 180 - b
    x = b + (d / 2)
    p.pencolor('black')
    p.forward(9)  #change starting position with same color to background
    p.pencolor(colors[r.randint(0, len(colors) - 1)]) #randomise color to draw
    p.left(x)
    for j in range(i):
        p.forward(s)
        if j != i - 1:
            p.left(b)
        else:
            p.right(d / 2)
            s += 3
    i += 1

turtle.done()