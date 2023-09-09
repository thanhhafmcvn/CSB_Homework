from turtle import *
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
width(5)
penup()
backward(300)
pendown()
for i in color_list:
    color(i)
    forward(70)
    penup()
    forward(30)
    pendown()
mainloop()