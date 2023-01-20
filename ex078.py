numeros = list()
maior = menor = 0

for n in range(1,6):
    numeros.append(int(input(f"Digite o {n}º valor: ")))
    if n == 1:
        maior = menor = numeros[0]
    else:
        if numeros[n - 1] > maior:
            maior = numeros[n - 1]

        if numeros[n - 1] < menor:
            menor = numeros[n - 1]

for n in numeros:
    print(n)

print(f"O maior valor informado foi: {maior} nas posições ", end="")
for pos, n in enumerate(numeros):
    if n == maior:
        print(f"{pos}...", end='')

print(f"\nO menor valor digitado foi {menor} nas posições ", end='')

for pos,n in enumerate(numeros):
    if n == menor:
        print(f"{pos}...", end='')

