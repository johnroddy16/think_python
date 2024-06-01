# ex 3-1 

def right_justify(s):
    x = len(s)
    y = 70 - x
    z = ' ' * y
    print(z + s)
    print(len(z + s)) 
    return True 

right_justify('monty')

