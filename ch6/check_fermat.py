# a function to test Fermat's theorem:

# Fermat's theorom: there are no positive integers a, b, and c such that a**n + b**n = c**n for any values of n greater than 2:

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print('Holy smokes, Fermat was wrong!')
        return
    print('No, that does not work')
    return 



# check_fermat(5, 5, 8, 3) 