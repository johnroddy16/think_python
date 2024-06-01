# chapeter 3, exercise 3-2:

def do_twice(f, x):
    f(x)
    f(x)

def print_twice(bruce):
    print(bruce)
    print(bruce)

def print_spam():
    print('spam')

# do_twice(print_spam)

do_twice(print_twice, 'spam')

def do_four(x, y):
    do_twice(x, y)
    do_twice(x, y)


    

