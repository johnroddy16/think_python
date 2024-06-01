# arc function, chapter 4, exercise 5:

# arc function will take same parameters as circle and add angle, which will determine what fraction of a circle to draw
# when angle = 360 a complete circle should be drawn:

import turtle

import math

larry = turtle.Turtle()

def arc(t, r, n, angle):
    x = math.pi
    C = 2 * x * r
    length = C / n 
    for _ in range(n//(360//angle)):
        t.fd(length)
        t.lt(360/n)

arc(larry, 100, 50, 360)



