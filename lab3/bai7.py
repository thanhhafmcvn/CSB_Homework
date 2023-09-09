from turtle import *
from math import *

a = float(input("Enter the first edge of triangle: "))
b = float(input("Enter the second edge of triangle: "))
c = float(input("Enter the third edge of triangle: "))

if a > 0 and b > 0 and c > 0:
    if a + b > c and b + c > 0 and a + c > 0:
        if (
            pow(a, 2) + pow(b, 2) == pow(c, 2)
            or pow(b, 2) + pow(c, 2) == pow(a, 2)
            or pow(a, 2) + pow(c, 2) == pow(b, 2)
        ):
            print("Right triangle")
        elif a == b and b == c:
            print("Equilateral triangle")
            for i in range(3):
                forward(200)
                left(120)
            mainloop()
        else:
            print("Normal triangle")
    else:
        print("3 line segments can not form a triangle")
else:
    print("Error.")
