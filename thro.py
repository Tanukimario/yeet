from turtle import *
plingus = Turtle()
plingus.speed(0)
plingus.penup()
s = Screen()
s.setup(width=1.0, height=1.0)

def throw(pow,grav,id):
    global v
    col = ["red","orange","yellow","green","blue","purple","pink","brown","black"]
    step = 0
    start = plingus.ycor()
    plingus.penup()
    plingus.goto(-900,-300)
    plingus.color(col[id-1])
    while plingus.ycor() > start - 10:
        v = pow - step * grav
        plingus.goto(plingus.xcor() + 5, plingus.ycor() + v)
        plingus.pendown()
        plingus.dot()
        plingus.penup()
        step = step + 1

throw(50,1,1)
s.mainloop()
