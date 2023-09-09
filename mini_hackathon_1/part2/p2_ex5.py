from turtle import *
edge = int(input('Input number of edges: '))
for i in range(edge):
    forward(100)
    left(180-((edge-2)*180)/edge)

mainloop()