import turtle

turtle.bgcolor("black")

p = turtle.Pen()
p.pencolor("white")
i = 3

s = 60
while i < 11:
    b = 360 / i  # 120
    d = 180 - b
    x = b + (d / 2)
    p.pencolor('black')
    p.forward(9)  # hidden
    p.pencolor('white')
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