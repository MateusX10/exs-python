def Factorial(num, show=True):
    f = 1
    cont = num
    while cont != 0:
        f *= cont
        if show:
            print(f"{cont} x " if cont != 1 else f"{cont} = ", end='')
        cont -= 1
    return f



print(Factorial(6, True))