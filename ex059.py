def menu():
    print('''Menu:
[ 1 ] - SOMAR
[ 2 ] - SUBTRAIR
[ 3 ] - MULTIPLICAR
[ 4 ] - DIVIDIR
[ 5 ] - SAIR
''')

def linha():
    print("-=" * 40)




n1 = int(input('Digite o primeiro valor: '))
n2 = int(input("Digite o segundo valor: "))
while True:
    menu()
    while True:
        jogador = int(input("Qual a sua escolha? "))
        if jogador in [1,2,3,4,5]:
            break
        print("\033[1;31mOpção inválida.Por favor, tente novamente.\033[m")

    if jogador == 1:
        print(f"{n1} + {n2} = {n1 + n2}")
    elif jogador == 2:
        print(f"{n1} - {n2} = {n1 - n2}")

    elif jogador == 3:
        print(f"{n1} x {n2} = {n1 * n2}")

    elif jogador == 4:
        print(f"{n1} / {n2} = {(n1 / n2):.0f}")
    else:
        print("\033[1;32mObrigado por usar nosso programa.Volte sempre :)\033[m")
        break

    linha()