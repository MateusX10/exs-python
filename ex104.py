def LeiaInt(txt):
    while True:
        v = str(input(txt))
        if v.isnumeric():
            v = int(v)
            break

        else:
            print("\033[1;31mErro.Informe um número inteiro válido!\033[m")
            continue

    return v

num = LeiaInt("Digite um valor: ")
print(F"Você digitou o número {num}")