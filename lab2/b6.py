from turtle import *
from math import *
shape('turtle')
for i in range(2):
    forward(200)
    right(90)
    forward(150)
    right(90)
left(90)
back(150)
pencolor('#de5246')
pensize(20)
forward(150)
right(130)
forward((sqrt(pow(150,2)+ pow(200,2)))/2)
left(80)
forward((sqrt(pow(150,2)+ pow(200,2)))/2)
right(130)
forward(150)

mainloop()
