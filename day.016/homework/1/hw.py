
from turtle import *

speed(100)
def kvardratis_xazva():
    for i in range(4):
        forward(200)
        left(90)
kvardratis_xazva()

forward(70)
left(90)
forward(100)  
right(90)
forward(60)
right(90)
forward(100)

penup()
goto(200, 200)
pendown()

right(150)
forward(200)
left(120)
forward(200)

penup()
goto(15, 170)
pendown()
left(30)
forward(50)
def window():
    for i in range(3):
        left(90)
        forward(50)
window()

penup()
goto(180, 170)
pendown()
def window_2():
    for i  in range(5):
        forward(50)
        left(90)
window_2()

exitonclick()