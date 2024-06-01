# adding param to square function:

import turtle

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

larry = turtle.Turtle()

square(larry, 20)