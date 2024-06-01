# we will import check_fermat and use it to check whether user input breaks the laws of Fermat:

from check_fermat import check_fermat

def user_fermat():
    while True:
        
        a = input('enter a number for a or enter lower case quit to exit the program:\n')
        
        if a == 'quit':
            break
        
        b = input('enter b:\n')
        c = input('enter c:\n')
        n = input('enter n:\n')
        
        try:
            a, b, c, n = int(a), int(b), int(c), int(n)
        except:
            print('you can only enter numbers for a, b, c, and n.')
            continue

        check_fermat(a, b, c, n)

user_fermat()