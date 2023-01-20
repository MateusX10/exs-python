abre_expressao = list()

expressao = str(input("Qual a expressão? "))

for simbolo in expressao:
    if simbolo == "(":
        abre_expressao.append("(")

    elif simbolo == ")":
        if len(abre_expressao) > 0:
            abre_expressao.pop()

        else:
            abre_expressao.append(")")


if len(abre_expressao) == 0:
    print("\033[1;32mA sua expressão está correta!\033[m")

else:
    print("\033[1;31mA sua expressão está incorreta!\033[m")

    


# abre_expressao = list()
# fecha_expressao = list()

# expressao = str(input("Expressão: "))

# for simb in expressao:
#     if simb == "(":
#         abre_expressao.append("(")
#     elif simb == ")":
#         fecha_expressao.append(")")

# if len(abre_expressao) != len(fecha_expressao):
#     print("\033[1;31mA sua expressão está errada!\033[m")
# else:
#     print("\033[1;32mA sua expressão está correta!\033[m")
