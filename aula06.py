r = ''
while True:
    n = input("Digite algo: ")
    print(n.isdecimal())
    r = str(input('Continuar [S/N]?')).strip().upper()[0]
    if r == "N":
        break
