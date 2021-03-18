import turtle

t = turtle.Pen()
a=20
t.penup()
for i in range(1,21):
    t.pendown()
    t.circle(a*i)
    t.penup()
    t.goto(0,-i*a)

turtle.done()