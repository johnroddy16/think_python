# do_n recursive function:

# do_n will take a function object and a number, n, as params:

import blastoff    

def do_n(func, n):
    func(n)

do_n(blastoff.countdown, 5)