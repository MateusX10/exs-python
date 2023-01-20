pessoas = list()
temp = list()
cont = MaiorPeso = MenorPeso = 0
continuar = ""
while True:
    cont += 1
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if cont == 1:
        MaiorPeso = MenorPeso = temp[1]

    else:
        if temp[1] > MaiorPeso:
            MaiorPeso = temp[1]

        elif temp[1] < MenorPeso:
            MenorPeso = temp[1]

    pessoas.append(temp[:])
    temp.clear()
    while True:
        continuar = str(input("Continuar [S/N]? ")).strip().upper()[0]

        if continuar in "SsNn":
            break
        print("\033[1;31mOpção inválida.Por favor, considere tentar novamente.\033[m")

    if continuar in "Nn":
        break

print("-=" * 40)
print(f"Ao todo, foram cadastradas {cont} pessoas")
print(f"O maior peso lido foi {MaiorPeso:.2f}Kg.Peso de ", end='')
for pessoa in pessoas:
    for peso in pessoa:
        if peso == MaiorPeso:
            print(f"{pessoa[0]}...", end='')
print(f"\nO menor peso lido foi {MenorPeso:.2f}Kg.Peso de ", end='')

for pessoa in pessoas:
    for peso in pessoa:
        if peso == MenorPeso:
            print(f"{pessoa[0]}...", end='')
