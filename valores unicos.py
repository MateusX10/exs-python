continuar = False
valores = []

while not continuar:
    n = int(input("Digite um valor: "))
    if n in valores:
        print("\033[1;31mValor duplicado.Não vou adicioná-lo...\033[m")
        continue
    valores.append(n)
    print("\033[1;32mValor adicionado com sucesso!\033[m")
    while True:
        r = str(input("Quer continuar [S/N]? ")).strip().upper()[0]
        if r in "SsNn":
            break
        print("\033[1;31mOpção inválida.Por favor, considere tentar novamente.\033[m")

    if r == "N":
        continuar = True
print("-=" * 40)
print(sorted(valores))