soma = cont = 0

for num in range(0,6):
    num = int(input(f"Digite o {num+1}º valor: "))
    if num % 2 == 0:
        cont += 1
        soma += num

print(f"A soma de todos os {cont} valores pares digitados foi {soma}")