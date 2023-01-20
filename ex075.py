tupla = (int(input("Digite o primeiro valor: ")), int(input('Digite o segundo valor: ')),
        int(input("Digite o terceiro valor: ")), int(input("Digite o quarto valor: ")),
        int(input("Digite o quinto valor: ")))

print(tupla)

print(f"O número 9 apareceu {tupla.count(9)} vezes na tupla")

if 3 in tupla:
    print(f"O primeiro valor 3 foi digitado na posição {tupla.index(3)}")

TotPar = 0
for num in tupla:
    if num % 2 == 0:
        TotPar += 1

print(f"Ao todo, foram digitados {TotPar} números pares") 