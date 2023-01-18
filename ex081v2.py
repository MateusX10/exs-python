valores = list()
TotNumerosDigitados = QuantValor5 = 0
while True:
    RespostaValida = False
    valores.append(int(input("Digite um valor: ")))
    TotNumerosDigitados += valores[-1]
    if valores[-1] == 5:
        QuantValor5 += 1
    while not RespostaValida:
        r = str(input("Continuar [S/N]? ")).strip().upper()[0]
        if r in "SsNn":
            RespostaValida = True
            continue
        print("\033[1;31mOpção inválida.Por favor, considere tentar mais uma vez.\033[m")
    if r == "N":
        break

print(sorted(valores, reverse=True))
print(f"Ao todo, a soma de todos os valores digitados foi {TotNumerosDigitados}")
if 5 in valores:
    print(f"O número 5 foi digitado {QuantValor5} vezes nas posições: ", end='')
    for posicao, numero in enumerate(valores):
        if numero == 5:
            print(f"{posicao}...", end='')

else:
    print("O número 5 não foi digitado nenhuma vez na lista 'valores'")