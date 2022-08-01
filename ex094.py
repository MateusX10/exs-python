princ = list()
dado = dict()
soma = média = 0
while True:
    dado.clear()
    dado = {"nome": str(input('Nome: ')), "idade": int(input('Idade: '))}
    soma += dado["idade"]
    while True:
        dado["sexo"] = str(input('Sexo: [M/F]')).strip().upper()[0]
        if dado["sexo"] in "MF":
            break
        print('\033[1;31mERRO!Digite somente "M" ou "F"!\033[m')
    princ.append(dado.copy())
    while True:
        r = str(input('Continuar? [S/N]')).strip().upper()[0]
        if r in "SN":
            break
        print('\033[1;31mERRO!Digite somente "S" ou "N"!\033[m')
    if r == "N":
        break

média = soma / len(princ)
print(princ)
print('-='*30)
print(f'A) Temos ao todo {len(princ)} pessoas cadastradas')
print(f'B) A média de idade é {média:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for el in princ:
    if el["sexo"] == "F":
        print(f'[{el["nome"]}] ',end='')
print(f'\nLista de pessoas com idade acima da média: ')
for p in princ:
    if p["idade"] > média:
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('\033[1;32m<<< ENCERRADO >>>\033[m')