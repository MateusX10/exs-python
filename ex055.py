MaiorPeso = MenorPeso = 0
NomeMaisPesado = NomeMaisLeve = ""

for p in range(1,6):
    nome = str(input(f"Nome da {p}º pessoa: ")).strip().capitalize()
    peso = float(input(f"Peso de {nome}: "))
    if p == 1:
        NomeMaisPesado = NomeMaisLeve = nome
        MaiorPeso = MenorPeso = peso

    elif peso > MaiorPeso:
        NomeMaisPesado = nome
        MaiorPeso = peso

    elif peso < MenorPeso:
        NomeMaisLeve = nome
        MenorPeso = peso


print(f'''O maior peso registrado foi de {MaiorPeso:.2f}Kg.Peso de {NomeMaisPesado}
O menor peso registrado foi de {MenorPeso:.2f}Kg.Peso de {NomeMaisLeve}''')
    