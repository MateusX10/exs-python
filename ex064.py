cont = soma = 0


while True:
    n = int(input("Digite um valor (999 interrompe): "))
    if n == 999:
        break
    else:
        cont += 1
        soma += n

print(f"Ao todo, foram digitados {cont} números e soma entre eles vale {soma}")