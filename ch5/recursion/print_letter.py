# another simple but affective recursive function:

def print_s(s, n):
    if n <=0:
        return
    print(s)
    print_s(s, n-1)

print_s('t', 4)