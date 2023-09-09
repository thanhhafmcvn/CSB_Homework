from turtle import *
from math import *

shape("turtle")
second_square_side = sqrt(pow(150, 2) + pow(150, 2))

for i in range(4):
    forward(200)
    left(90)
penup()
back(50)
left(90)
forward(100)
right(45)
pendown()
for i in range(4):
    forward(second_square_side)
    right(90)
right(45)
penup()
forward(150)
left(90)

mainloop()
