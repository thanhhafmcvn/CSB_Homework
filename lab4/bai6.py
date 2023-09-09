from turtle import *

number = int(input("Input number of egdes: "))
if number > 2:
    for i in range(number):
        forward(100)
        left(180-((number - 2) * 180) / number)
else:
    print("Invalid input")
mainloop()