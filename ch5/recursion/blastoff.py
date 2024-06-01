# a simple but affective recursive function:

def countdown(x):
    if x == 0:
        print('blastoff!')
        return True
    else:
        print(x)
        countdown(x-1)

# countdown(4) 