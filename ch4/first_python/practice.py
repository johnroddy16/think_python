# practice python file:

import math 
import turtle 

angle = 180

r = 50 

arc_length = 2 * math.pi * r * angle / 360

# print(arc_length)

n = int(arc_length / 3) + 1

# print(n)

step_length = arc_length / n

# print(step_length)

step_angle = angle / n 

# print(step_angle)

larry = turtle.Turtle()

for _ in range(n):
    larry.fd(step_length)
    larry.lt(step_angle)