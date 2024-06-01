# polygon, chapter 4, think python:

import turtle

larry = turtle.Turtle()

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

# polygon(larry, 50, 6) 

