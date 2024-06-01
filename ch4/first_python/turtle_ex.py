# chapter 4, think python, exercise 4:

import turtle 

larry = turtle.Turtle()

def square(inst, steps, angle):
    for _ in range(4):
        inst.fd(steps)
        inst.lt(angle)

square(larry, 100, 90)