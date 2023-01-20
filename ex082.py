lista_original = list()
lista_de_pares = list()
lista_de_impares = list()

while True:
    r = ""
    lista_original.append(int(input('Digite um valor: ')))
    while True:
        r = str(input("Quer continuar [S/N]? ")).strip().upper()[0]

        if r in "SsNn":
            break
        print("\033[1;31mOpção inválida.Considere tentar novamente\033[m")
    if r == "N":
        break

for numero in lista_original:
    print(numero)
    if numero % 2 == 0:
        lista_de_pares.append(numero)
    else:
        lista_de_impares.append(numero)

print("Lista original: {}".format(lista_original))
print("Lista com os valores pares: {}".format(lista_de_pares))
print("Lista com os valores ímpares: {}".format(lista_de_impares))