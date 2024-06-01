# turtle module:

import turtle

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

larry = turtle.Turtle()

polygon(larry, 80, 8)

