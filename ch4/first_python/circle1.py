# importing polygon to use with circle function:

import math  # import math to use pi
import turtle  # import to use the turtle class
from mypolygon import polygon  # import polygon function to use inside circle function 

larry = turtle.Turtle() 

# polygon(larry, 60, 8)

# def polygon(t, length, n):
#     for _ in range(n):
#         t.fd(length)
#         t.lt(360/n)

def circle1(t, r, n):
    x = math.pi
    C = 2 * x * r
    length = C / n
    polygon(t, length, n)

circle1(larry, 100, 50)