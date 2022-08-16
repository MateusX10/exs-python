n = str(input("Digite um número de 0 a 9999: "))


if len(n) >= 1:
    unidade = n[-1]
    print(f'Unidade: {unidade} ')
if len(n) >= 2:
    dezena = n[-2]
    print(f'dezena: {dezena}') 
if len(n) >= 3:
    centena = n[-3]
    print(f'centena: {centena}') 
if len(n) >= 4:
    milhar = n[-4]
    print(f'milhar: {milhar}')