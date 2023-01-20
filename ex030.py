numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f'\033[1;32m{numero} é um número PAR!\033[m')
else:
    print(f"\033[1;31m{numero} é um número ÍMPAR!\033[m")