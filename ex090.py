boletim = dict()

while True:
    boletim["nome"] = str(input("Nome: "))
    boletim["média"] = float(input("Média: "))
    if boletim["média"] >= 7 and boletim["média"] <= 10:
        boletim["situação"] = "\033[1;32mAprovado\033[m"
    elif boletim["média"] >= 5:
        boletim["situação"] = "\033[1;33mRecuperação\033[m"
    else:
        if boletim["média"] < 5:
            boletim["situação"] = "\033[1;31mReprovado\033[m"
        else:
            print("\033[1;32mOpção inválida.Por favor, tente novamente.\033[m")
            continue
    break

print("-=" * 30)

print(boletim)

for k, v in boletim.items():
    print(f"{k} é igual a {v}")