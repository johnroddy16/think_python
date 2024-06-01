# circle function from chapter 4, exercise 4:

# circle will take t, a turtle object, and r, radius, as arguments and create a circle with radius r:

# C = 2πr 



import math 

import turtle

larry = turtle.Turtle()



def circle(t, r, n):
    x = math.pi
    C = 2 * x * r
    length = C / n
    for _ in range(n):
        t.fd(length)
        t.lt(360/n)

circle(larry, 100, 50)

# print(x)