def Factorial(num, show=False):
    '''
    --> Calculates the factorial of a number
    :param num: number to be calculated the factorial
    :param show: (optional parameter) show or not show the calculation
    :return: returns the number that the factorial was calculated
    '''
    f = 1
    cont = num
    while cont != 0:
        f *= cont
        if show:
            print(f"{cont} x " if cont != 1 else f"{cont} = ", end='')
        cont -= 1
    return f

def Factorial2(n, show=False):
    '''--> Calculates the factorial of a number
    :param n: number to be calculated the factorial
    :param show: (optional parameter) show or not show the calculation
    :return: returns the number that the factorial was calculated
    '''
    cont = n
    f = 1
    for v in range(cont, 0, -1):
        print(f"{v} x " if v > 1 else f"{v} = "  , end='')
        f *= v

    return f

print(Factorial(6, True))
#print(Factorial2(6, True))

#help(Factorial)
#help(Factorial2)