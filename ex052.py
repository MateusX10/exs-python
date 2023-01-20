QuantDivisivel = 0

n = int(input("Digite um número: "))

for num in range(1, n+1):
    if n % num == 0:
        QuantDivisivel += 1
        print(f'\033[1;31m{num}\033[m  ', end='')
    else:
        print(f'\033[1;32m{num}\033[m  ' , end='')
if QuantDivisivel == 2:
    print(f'\n{n} é um número primo')

else:
    print(f'\n{n} NÃO É um número primo')