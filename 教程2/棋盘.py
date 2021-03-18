import turtle

t=turtle.Pen()
t.penup()
a = 300
b=a/20
for i in range(0,21):
    t.goto(0,a-i*a/20)
    t.pendown()
    t.goto(a,a-i*a/20)
    t.penup()

for i in range(0,21):
    t.goto(a-i*a/20,0)
    t.pendown()
    t.goto(a-i*a/20,a)
    t.penup()
turtle.done()